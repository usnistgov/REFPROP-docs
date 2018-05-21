"""
A module with some scripts for automatic documentation generation

By Ian Bell, NIST, 2016-
"""

from __future__ import print_function
from io import StringIO
import glob, os, json, six, sys, textwrap, time

name_remapping = {'CCRIT':'CSTAR',
                  'SATPEST':'SATEST',
                  'SATTEST':'SATEST'}

fallback_arguments = {'GERG04dll': 'GERG08', 'THERM2dll': ['THERMdll','THERM3dll','AG','DERVPVTdll']}

FLSH_funcs = [k+'FLSHdll' for k in ['DE','DH','DS','ES','HS','PD','PE','PH','PQ','PS','TD','TE','TH','TP','TQ','TS','DQ']]
FLSH_funcs += [k+'FL1dll' for k in ['DE','DH','DS','ES','HS','PD','PE','PH','PQ','PS','TD','TE','TH','TP','TQ','TS','DQ']]
FLSH_funcs += [k+'FL2dll' for k in ['DE','DH','DS','ES','HS','PD','PE','PH','PQ','PS','TD','TE','TH','TP','TQ','TS','DQ']]
FLSH_funcs += ['ENTHALdll','ENTROdll','CVCPdll']

FLSH_other_input_args = ['Z','DMIN','DMAX']
FLSH_args = {
    'P': 'Pressure [kPa]',
    'Q': 'Vapor quality [mol/mol]',
    'T': 'Temperature [K]',
    'E': 'Internal energy [J/mol]',
    'H': 'Enthalpy [J/mol]',
    'S': 'Entropy [J/mol-K]',
    'D': 'Density [mol/K]',
    'DL': 'Molar density of the liquid phase [mol/L]',
    'DV': 'Molar density of the vapor phase [mol/L]',
    'CV': 'Isochoric heat capacity [J/mol-K]',
    'CP': 'Isobaric heat capacity [J/mol-K]',
    'W': 'Speed of sound [m/s]',
    'HJT': 'Isenthalpic Joule-Thomson coefficient [K/kPa]',
    'HERR': 'Error string (character*255)',
    'IERR': 'Error code (no error if ierr==0)',
    'Z': 'Bulk Composition (array of mole fractions)',
    'X': 'Composition of the liquid phase (array of mole fractions)',
    'Y': 'Composition of the vapor phase (array of mole fractions)',
    'DMIN': 'Lower bound on density [mol/L]',
    'DMAX': 'Upper bound on density [mol/L]'
}

High_Level_Header = """

.. This file was auto-generated on {datetime:s}. DO NOT(!!!!) modify this file directly.  Modify the generator script in the scripts folder.

.. _high_level_api:

**************
High-Level API
**************

"""

Legacy_Header = """

.. This file was auto-generated on {datetime:s}. DO NOT(!!!!) modify this file directly.  Modify the generator script in the scripts folder.

**********
Legacy API
**********

.. warning::

    The functions in this legacy application program interface (API) have all been deprecated and will be removed in some future release.  Please use the :ref:`high_level_api`:

"""

High_level_functions = ['REFPROPdll','REFPROP1dll','REFPROP2dll','ALLPROPSdll','ALLPROPS0dll','ALLPROPS1dll','ABFLSHdll','GETENUMdll','ERRMSGdll','SETFLUIDSdll','SETMIXTUREdll','SETPATHdll','FLAGSdll']

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
            for j in range(10000):
                if i+j == len(lines): break
                if "ritten by" in lines[i+j] or 'original version' in lines[i+j]:
                    break
                elif ' include \'' in lines[i+j] and not lines[i+j].strip().startswith('c '):
                    break
                elif lines[i+j] == ' ':
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

    def line_decomment(line):
        if line == 'c': return ''
        if line.startswith('c '):
            return line[1::]
        else:
            return line.strip()

    def line_startswith(s, search, EOL = None):
        o = None
        for iline, line in enumerate(s):
            decomm = line_decomment(line).lstrip()
            if EOL is not None:
                if decomm.startswith(search) and decomm.strip().endswith(EOL):
                    return iline
            else:
                if decomm.startswith(search):
                    return iline
        return o

    def line_containing(s, search):
        o = None
        for iline, line in enumerate(s):
            if search in line:
                return iline
        return o


    def deconstruct_parameters(lines):
        # Find the lines that have '--' in them, and add another at the end
        seps = [iline for iline, line in enumerate(lines) if '--' in line] + [len(lines)]
        args, flags = {}, {}
        # Get all the arguments
        for j in range(len(seps)-1):
            istart,iend = seps[j],seps[j+1]
            # Get the argument based on the first line
            try:
                arg, desc = line_decomment(lines[istart]).strip().split('--')
                if ':' in desc:
                    desc = desc.split(':')[0]
            except ValueError as VE:
                print(line_decomment(lines[istart]).strip())

            # If the line has a ': in it, then the stuff that follows is a list of flags, otherwise, the following lines are glommed together
            if ':' in line_decomment(lines[istart]).strip():
                otherlines = [lines[istart].split(':')[1]] + lines[istart+1:iend]
                if otherlines and iend > istart+1:
                    if len(otherlines) == 1 and not line_decomment(otherlines[0]).strip():
                        # Empty line, don't do anything
                        continue
                    else:
                        lastkey = None
                        info = {}
                        for line in otherlines:
                            cleaned = line_decomment(line).strip()
                            if ' - ' not in cleaned:
                                # if lastkey is None:
                                #     print(lines, info, line)
                                print(lastkey, info, cleaned)
                                if cleaned:
                                    info[lastkey] += ' ' + cleaned
                                # else:
                                #     print('BAD!!!: ', cleaned, '<--', line)
                            else:
                                k,v = cleaned.split(' - ',1)
                                info[k.strip()] = v.strip()
                                lastkey = k.strip()
                        flags[arg.strip().lower()] = info
            else:
                # Keep on glomming the rest in, with spaces between lines
                otherlines = lines[istart+1:iend]
                desc += ' '+ ' '.join([line_decomment(l).strip() for l in otherlines])

            args[arg.strip().lower()] = desc
            # print('OOOOOOOOOOOOOOOOO', lines[istart-1], '||', otherlines, info)
        return args, flags

    # Find the line that contains "Input" and "Output"
    iInputs = line_startswith(contents, 'Input', EOL=':') or line_startswith(contents, 'Inputs', EOL=':')
    iOutput = line_startswith(contents, 'Output', EOL=':') or line_startswith(contents, 'Outputs', EOL=':')

    print(iInputs, iOutput)

    class struct(object): pass
    info = struct()
    info.doc_block = '\n\n'+ ' '*4+'XXXXXXXXXXXXXXXXXXXX  CANNOT GET DOCS\n\n'
    info.in_args, info.in_flags = {},{}
    info.out_args, info.out_flags = {},{}
    def indent(lines, n):
        return '\n'.join([' '*n + l for l in lines])
    
    if iInputs is None and iOutput is None:
        info.doc_block = indent(textwrap.dedent('\n'.join([line_decomment(line) for line in contents[1::]])).split('\n'), 4)

    if iInputs is not None or iOutput is not None:
        iMax = iInputs if iInputs is not None else iOutput
        info.doc_block = indent(textwrap.dedent('\n'.join([line_decomment(line) for line in contents[1:iMax]])).split('\n'), 4)

        if iInputs is not None:
            if iOutput is not None:
                info.in_args, info.in_flags = deconstruct_parameters(contents[iInputs+1:iOutput])
            else:
                info.in_args, info.in_flags = deconstruct_parameters(contents[iInputs+1::])
        if iOutput is not None:
            info.out_args, info.out_flags = deconstruct_parameters(contents[iOutput+1::])
    # print(info.in_args)
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

    sout_high, sout_legacy = '', ''
    funcs_legacy = 'Function Listing\n----------------\n\n'
    funcs_high = 'Function Listing\n----------------\n\n'
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
        print(func, info.__dict__)

        args_string = ''
        if func+'dll' in function_dict:
            args = function_dict[func+'dll']['argument_list']
            for arg in args:
                # arg is (name, type, length) or (name, type)
                docs = None
                inout = ''
                argname = arg[0].lower()
                if argname in info.in_args:
                    inout = ' [in]'
                    docs = info.in_args[argname]
                if argname in info.out_args:
                    inout = ' [out]'
                    docs = info.out_args[argname]
                if docs is None: 
                    badx = 'XXXXXXXXXX'
                    docs = badx
                    if func+'dll' in fallback_arguments:
                        # Get docs from fallback(s)
                        fb_names = fallback_arguments[func+'dll']
                        if not isinstance(fb_names, list):
                            fb_names = [fb_names]

                        for fb_name in fb_names:
                            fallinfo = deconstruct_function_info(contents[fb_name].split('\n'))

                            if argname in fallinfo.in_args:
                                inout = ' [in]'
                                docs = fallinfo.in_args[argname]
                            if argname in fallinfo.out_args:
                                inout = ' [out]'
                                docs = fallinfo.out_args[argname]

                            if docs != badx:
                                break

                            # print(func, argname, docs, fallinfo.in_args)

                    elif func+'dll' in FLSH_funcs:
                        if argname.upper() in FLSH_args:
                            docs = FLSH_args[argname.upper()]
                            if argname.upper() in func[0:2] or argname.upper() in FLSH_other_input_args:
                                inout = ' [in]'
                            else:
                                inout = ' [out]'

                        # print(func, argname, docs, fallinfo.in_args)
                    
                size = ''
                if len(arg) == 3 and int(arg[2]) > 0:
                    size = '(' + str(arg[2]) + ')'
                # print(argname)
                
                args_string += ' '*4 + ':p {type:s} {name:s}{size:s}{inout:s}: {docs:s}\n'.format(name = arg[0].strip(), type = arg[1].strip('*').strip(), size =size, inout = inout, docs= docs)

            if dll_functions:
                for arg in function_dict[func+'dll']['string_arguments']:
                    args_string += ' '*4 + ':p int ' + arg[0] + ': length of variable ``' + arg[0].replace('_length','') + '`` (default: '+str(arg[1])+')\n'
        else:
            print('Cannot find function arguments for:', func+'dll')
            continue

        flags_string = ''
        if info.in_flags or info.out_flags:
            flags_string = ' '*4 + ':Flags: \n\n'
            #if info.out_flags: raise ValueError('IMPOSSIBLE:'+str(info.out_flags))
            def spit_out_flags(flags):
                s = ''
                for flag,data in six.iteritems(flags):
                    s += ' '*8 + '``' + flag + '`` flags\n\n'
                    for k,v in six.iteritems(data):
                        s += ' '*8 + ':' + k + ': ' + v + '\n'
                    s += '\n'
                return s

            flags_string += spit_out_flags(info.in_flags)
            flags_string += spit_out_flags(info.out_flags)


        sout = ''
        # This is the definition of the function prototype
        theargs = ', '.join([a[0] for a in function_dict[func+'dll']['argument_list']])
        # Add on the arguments at the end with the string lengths if you are documenting the DLL
        if dll_functions:
            theargs += ', ' + ', '.join([a[0] for a in function_dict[func+'dll']['string_arguments']])
        sout += '.. f:subroutine:: {func:s} ({args:s})\n\n'.format(func=func+'dll', args = theargs)

        # The block of documentation
        sout += info.doc_block#.replace('*','\*')

        # The list of arguments to the function
        sout += '\n' + args_string + '\n'

        # The list of flags to the function
        sout += '\n' + flags_string + '\n'

        if func+'dll' in High_level_functions:
            sout_high += sout
            funcs_high += '- :f:func:`' + func+'dll' + '`\n'
        else:
            sout_legacy += sout
            funcs_legacy += '- :f:func:`' + func+'dll' + '`\n'

    funcs_high += '\n\nFunction Documentation\n----------------------\n'
    funcs_legacy += '\n\nFunction Documentation\n----------------------\n'

    return (High_Level_Header.format(datetime=time.strftime("%d %b %Y %H:%M:%S", time.localtime())) + funcs_high + sout_high, 
           Legacy_Header.format(datetime=time.strftime("%d %b %Y %H:%M:%S", time.localtime())) + funcs_legacy + sout_legacy)

if __name__=='__main__':
    # This path is hardcoded, change as needed
    FOR_path = 'FORTRAN'

    # Use the script in REFPROP-headers repo to generate a dictionary of function parameter data
    # from the functions defined in the PASS_FTN.FOR file
    # ------------------------------------------------------------------------------------------
    sys.path.append('../externals/REFPROP-headers')
    import generate_header
    generate_header.generate_interface_file(os.path.join(FOR_path,'PASS_FTN.FOR'), 'REFPROP.pyf')
    function_dict = generate_header.generate_function_dict('REFPROP.pyf')
    # Write to file for debugging if desired/needed:
    with open('functions.json','w') as fp: fp.write(json.dumps(function_dict, indent =2))

    # Parse the .FOR files and extract docs; write to joined.json file
    # ----------------------------------------------------------------
    objects = generate_manual_content(FOR_path, JSON_ofname = 'joined.json')

    # print(objects['ALLPROPS0'])
    # print(deconstruct_function_info(objects['ALLPROPS0'].split('\n')).__dict__)
    # sys.exit()

    # Generate the RST string
    # -----------------------
    rst_high, rst_legacy = parse_manual_contents(objects, function_dict, True)
    
    # Write RST bits to file
    # ----------------------
    docs_path = os.path.join('sphinx') 
    for fname, rst in [('high_level.rst',rst_high),('legacy.rst',rst_legacy)]:
        rst_file = os.path.join(docs_path, fname)
        with open(rst_file, 'w') as fp:
            fp.write(rst)
        this_dir = os.path.dirname(__file__)
        with open(os.path.join(this_dir, '..', 'doc', 'DLL', fname), 'w') as fp:
            fp.write(rst)

    import subprocess
    for i in range(3):
        try:
            subprocess.check_call('activate py36 && make html', cwd='sphinx', shell = True, stdout = sys.stdout, stderr = sys.stderr)
            break
        except:
            continue
    for i in range(3):
        try:
            subprocess.call('activate py36 && make latex', cwd='sphinx', shell = True, stdout = sys.stdout, stderr = sys.stderr)
            break
        except:
            continue
    for i in range(3):
        subprocess.call('pdflatex REFPROP.tex', cwd='sphinx/_build/latex', shell = True, stdout = sys.stdout, stderr = sys.stderr)