"""
A module with some scripts for automatic documentation generation

By Ian Bell, NIST, 2016-
"""

from __future__ import print_function
from cStringIO import StringIO
import glob, os, json, six, sys

name_remapping = {'CCRIT':'CSTAR',
                  'SATPEST':'SATEST',
                  'SATTEST':'SATEST'}

def generate_manual_content(FOR_path, JSON_ofname = None):
    """
    Generate a dictionary mapping from function name to documentation

    FOR_path: string
        Path to the folder containing the .FOR files
    JSON_ofname: string, optional
        If provided, the file to which the content will be written in JSON format    
    """

    # Get all the fortran files
    for_files = []
    for ending in ['*.FOR','*.for']:
        for_files += glob.glob(os.path.join(FOR_path, ending))
    assert(len(for_files) > 0)

    # Join all the files into one big string
    joined = ''
    for for_file in for_files:
        with open(for_file,'r') as fp:
            joined += fp.read() + '\n'  

    # Munge function arguments as needed to replace arguments that span lines
    isubstart = 0 
    while isubstart > -1:
        isubstart = joined.find('subroutine',isubstart)
        
        isubopen = joined.find('(', isubstart)
        isubclose = joined.find(')', isubopen)
        iEOL = joined.find('\n', isubstart)
        
        # Skip ones with newline between end of subroutine and (
        if iEOL < isubopen:
            isubstart += 1 # go to next instance of subroutine
            continue

        # Skip ones that are in the comments block
        ipreEOL = joined.rfind('\n', 0, isubstart) # Find preceding EOL

        if joined[ipreEOL+1:ipreEOL+3].startswith('c '):
            isubstart = isubclose
            continue

        if '\n' in joined[isubstart:isubclose+1]:
            old = joined[isubstart:isubclose+1]
            new = old.replace('\n','').replace('&','')
            joined = joined.replace(old, new)
            isubstart += 1
            continue

        isubstart = joined.find('subroutine',isubclose)
        if isubstart < 0:
            break

    ####### Uncomment next lines to see what it did
    with open('joined.txt','w') as fp:
        fp.write(joined)

    objects = {}

    lines = joined.split('\n')
    for i in range(len(lines)):
        
        if lines[i].strip().startswith('subroutine') or lines[i].strip().startswith('function'):

            objname = lines[i].split('(')[0].replace('subroutine ','').replace('function ','').strip()
            objlines = []
            for j in range(100):
                if i+j == len(lines): break
                if "ritten by" in lines[i+j] or ' include ' in lines[i+j] or lines[i+j] == ' ':
                    break
                else:
                    objlines.append(lines[i+j])

            objects[objname] = '\n'.join(objlines)

            i += j

    if JSON_ofname:
        with open(JSON_ofname,'w') as fp:
            json.dump(objects, fp, indent =2)
    return objects

def deconstruct_function_info(contents):

    def line_containing(s, search):
        o = None
        for iline, line in enumerate(s):
            if search in line:
                return iline
        return o
    def line_decomment(line):
        if line == 'c': return ''
        if line.startswith('c '):
            return line[2::].strip()
        else:
            return line.strip()

    # Determine how many lines correspond to the string information about the function
    # Things that end this block are: *written*

    # Find the line that contains Input and written lines
    iInputs = line_containing(contents, 'Input')
    iOutput = line_containing(contents, 'Output')

    class struct(object): pass
    info = struct()
    info.doc_block = '\n\n'+ ' '*4+'XXXXXXXXXXXXXXXXXXXX  CANNOT GET DOCS\n\n'
    info.in_args = {}
    info.out_args = {}
    if iInputs is not None and iOutput is not None:
        info.doc_block = '\n'.join([' '*4+line_decomment(line) for line in contents[1:iInputs]])
        for line in contents[iInputs+1:iOutput]:
            if '--' in line:
                arg, desc = line_decomment(line).strip().split('--')
                info.in_args[arg.strip().lower()] = desc
        for line in contents[iOutput+1::]:
            if '--' in line:
                arg, desc = line_decomment(line).strip().split('--')
                info.out_args[arg.strip().lower()] = desc
    print(info.in_args)
    return info

def parse_manual_contents(contents, function_dict, dll_functions):
    """
    Write the RST data needed by the sphinx-fortran package
    """
    def chop_dll(s):
        if s.endswith('dll'):
            return s[0:-3]
        else:
            return s
    # Functions that end with dll in the PASS_FTN.FOR file
    has_dll = [funcname for funcname, lines in six.iteritems(contents) if funcname.endswith('dll')]
    # 
    missing = [chop_dll(func) for func in has_dll if chop_dll(func) not in contents]

    sout = ''
    for func in sorted(has_dll):

        # Get remapped name, or the same dll-stripped name back again otherwise
        func = name_remapping.get(chop_dll(func), chop_dll(func))

        # Format the output
        something_outputted = False

        # Skip missing functions
        if func in missing: 
            print('skipping missing function:', func)
            continue

        info = deconstruct_function_info(contents[func].split('\n'))

        args_string = ''
        if func+'dll' in function_dict:
            args = function_dict[func+'dll']['argument_list']
            for arg in args:
                # arg is (name, type, length) or (name, type)
                docs = None
                if arg[0] in info.in_args:
                    docs = '[INPUT] ' + info.in_args[arg[0]]
                if arg[0] in info.out_args:
                    docs = '[OUTPUT] ' + info.out_args[arg[0]]
                if docs is None: 
                    docs = 'XXXXXXXXXX'
                if len(arg) == 3 and arg[2] > 0:
                    args_string += ' '*4 + ':p ' + arg[1].strip('*') + arg[0] + '(' + str(arg[2]) + '): '+docs+'\n'
                else:
                    args_string += ' '*4 + ':p ' + arg[1].strip('*') + arg[0] + ': '+docs+'\n'
            if dll_functions:
                for arg in function_dict[func+'dll']['string_arguments']:
                    args_string += ' '*4 + ':p int ' + arg[0] + ': length of variable ``' + arg[0].replace('_length','') + '`` (default: '+str(arg[1])+')\n'
        else:
            print('Cannot find function arguments for:', func+'dll')
            continue

        # This is the definition of the function prototype
        theargs = ', '.join([a[0] for a in function_dict[func+'dll']['argument_list']])
        # Add on the arguments at the end with the string lengths if you are documenting the DLL
        if dll_functions:
            theargs += ', ' + ', '.join([a[0] for a in function_dict[func+'dll']['string_arguments']])
        sout += '.. f:subroutine:: {func:s} ({args:s})\n\n'.format(func=func+'dll', args = theargs)

        # The block of documentation
        sout += info.doc_block

        # The list of 

        sout += '\n'
        sout += args_string
        sout += '\n\n'
        
    return sout

if __name__=='__main__':
    FOR_path = 'R:\\914FILES'

    # Use the script in REFPROP-headers repo to generate a dictionary of function parameter data
    # from the functions defined in the PASS_FTN.FOR file
    # ------------------------------------------------------------------------------------------
    sys.path.append('../externals/REFPROP-headers')
    import generate_header
    generate_header.generate_interface_file(os.path.join(FOR_path,'PASS_FTN.FOR'), 'REFPROP.pyf')
    function_dict = generate_header.generate_function_dict('REFPROP.pyf')
    # Write to file for debugging if needed:
    # with open('functions.json','w') as fp: fp.write(json.dumps(function_dict, indent =2))

    # Parse the .FOR files and extract docs; write to joined.json file
    # ----------------------------------------------------------------
    objects = generate_manual_content(FOR_path, JSON_ofname = 'joined.json')

    # Generate the RST string
    # -----------------------
    rst = parse_manual_contents(objects, function_dict, True)
    
    # Write RST to file
    # -----------------
    with open('for_docs.rst','w') as fp:
       fp.write(rst)

    import subprocess
    subprocess.call('make html', cwd='sphinx', shell = True, stdout = sys.stdout, stderr = sys.stderr)
    subprocess.call('make latex', cwd='sphinx', shell = True, stdout = sys.stdout, stderr = sys.stderr)
    for i in range(3):
        subprocess.call('pdflatex REFPROP.tex', cwd='sphinx/_build/latex', shell = True, stdout = sys.stdout, stderr = sys.stderr)