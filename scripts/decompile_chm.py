from __future__ import print_function
import re, glob, os, subprocess, shutil, sys, six

RENAME_MAP = {
    '1omg8vc': 'filesave',
    '5.hj_.e': 'renamewindow',
    '12gcbn.': 'saturationpointsbubbledew',
    'hs2': 'welcometorefprop',
    'hs7': 'copyrightdisclaimer',
    'hs814': 'faq',
    'lyey_o': 'saturationpointsequilibrium'
}
RENAME_MAP_inverted = {v:k for k,v in six.iteritems(RENAME_MAP)}

INDEX_FILES = {
    './Menu Commands/Options Menu':'options.rst',
    './Menu Commands/Edit Menu':'editmenu.rst',
    './Menu Commands/File Menu':'filemenu.rst',
    './Menu Commands/Help Menu':'helpmenu.rst',
    './Menu Commands/Plot Menu':'plotmenu.rst',
    './Menu Commands/Window Menu':'windowmenu.rst',
    './Menu Commands/Calculate Menu':'calculate.rst',
    './Menu Commands/Substance Menu':'substance.rst',
    './Programming':'dll_s.rst',
    }

# Extracted in the #IVB variable with FAR
# Could also open CHM with 7zip (it's just an archive anyway)
IVB = """hs2.htm  2  
aboutrefprop.htm  3  
statusline.htm  5  
cautions.htm  6  
hs7.htm  7  
filemenu.htm  100
opensession.htm  101
1omg8vc.htm  102
closesession.htm  103
savetables.htm  104
printsetup.htm  105
editmenu.htm  200
copytabledata.htm  201
copyplot.htm  202
paste.htm  203
readdata.htm  204
selectall.htm  205
deleterow.htm  206
saveplotdatapoints.htm  207
options.htm  300
units.htm  301
reference.htm  302
properties.htm  303
propertyorder.htm  304
preferences.htm  305
savecurrentoptions.htm  306
retrieveoptions.htm  307
substance.htm  400
purefluid.htm  401
predefinedmixture.htm  402
definenewmixture.htm  403
fluidinformation.htm  404
specifycomposition.htm  405
viewmixingparameters.htm  406
pseudopurefluid.htm  407
specifyfluidset.htm  408
fluidsearch.htm  409
calculate.htm  500
saturationtables.htm  501
isopropertytables.htm  502
specifiedstatepoints.htm  503
lyey_o.htm  504
12gcbn..htm  505
tables.htm  550
formatcolumnposition.htm  551
plotmenu.htm  600
newplot.htm  601
overlayplot.htm  602
modifyplot.htm  603
addlabel.htm  604
diagrams.htm  605
zooming.htm  606
plotwindow.htm  650
windowmenu.htm  700
tile.htm  701
cascade.htm  702
5.hj_.e.htm  703
closewindow.htm  704
helpmenu.htm  800
helpindex.htm  801
firsttimeusers.htm  813
hs814.htm  814
dll_s.htm  823
excel_spreadsheets.htm  833
sample_visual_basic_code.htm  843
sample_fortran_code.htm  853
sample_c_code.htm  863
progamming_with_delphi.htm  873
sample_matlab_code.htm  883
samplelabviewcode.htm  893"""

page_indices = {}
for line in IVB.split('\n'):
    k,v = [l for l in line.split(' ') if l]
    page_indices[k] = int(v)

def rename(s):
    for old,new in six.iteritems(RENAME_MAP):
        s = s.replace(old, new)
    return s

def decompile_chm():
    # Make sure that REFPROP.chm is in this directory
    assert(os.path.exists('REFPROP.chm'))
    subprocess.check_call('Hh -decompile _output REFPROP.CHM')

    a = re.compile(r'<A HREF=\"(.*?)\">')
    def get_all_link_href():
        hrefs = []
        for file in glob.glob('html/*.htm'):
            with open(file, 'r') as fp:
                refs = re.findall(a, fp.read())
                #print file, refs
                hrefs += refs
        return list(set(hrefs))

    link_href = get_all_link_href()

    #print link_href
    if os.path.exists('rst'):
        shutil.rmtree('rst')
    os.mkdir('rst')
    for file in glob.glob('_output/html/*.htm'):
        with open(file) as fp:
            #print file, [href for href in re.findall(a, fp.read()) if 'html\\'+href not in glob.glob('html/*.htm')]

            fnameroot = os.path.split(rename(file))[1].split('.')[0]

            html_contents = fp.read()
            title = re.findall(r'<TITLE>(.*?)</TITLE>', html_contents)
            assert(len(title) == 1)
            title = title[0]
            
            body = re.findall(r'<BODY.*?>(.+?)</BODY>', html_contents, re.DOTALL)
            assert(len(body) == 1)
            body = body[0]

            # Fix each of the paragraphs to strip out font specifications
            def repl(para):
                for i in range(5):
                    para = re.sub(r'<FONT FACE="MS Sans Serif".*?>(.*?)</FONT>', r'\1', para, re.DOTALL)
                return para
            
            for m in reversed([_ for _ in re.finditer(r'<P.*?>(.*?)</P>', body, re.DOTALL)]):
                body = body[:m.start()] + repl(m.groups()[0]) + body[m.end():]

            # Fix hyperlinks and references
            def repl(m):
                href, caption = m.groups()
                if '<FONT' in caption:
                    caption = re.sub('<FONT.*?>(.*?)</FONT>',r'\1', caption)
                if 'http://' not in href and href.endswith('.htm'): 
                    href = href.replace('.htm','')
                out = '`{caption:s} <{href:s}>`'.format(caption = caption, href = rename(href))
                if 'http://' not in href:
                    return ':ref:' + out + ' '
                else:
                    return out + '_'

            body = body.replace(r'<B>Welcome to REFPROP&nbsp;&nbsp; </FONT><FONT FACE="Arial" COLOR="#800000" SIZE="5"><IMG SRC="../images/REFPROP.png" WIDTH="64" HEIGHT="64" BORDER="0"></B>','**Welcome to REFPROP GUI documentation**\n\n.. image:: _static/refprop.png\n\n')

            body = re.sub(r'<A HREF="(.*?)">(.*?)</A>', repl, body) 

            body = body.replace('&nbsp;','')

            # Fix bold headings
            body = re.sub(r'<B>(.*?)</B>', r'**\1**', body)
            # Fix italics
            body = re.sub(r'<I>(.*?)</I>', r'*\1*', body)
            # "Fix" underline (make it bold)
            body = re.sub(r'<U>(.*?)</U>', r'**\1**', body)
            body = re.sub(r'<FONT FACE="Arial" SIZE="3">(.*?)</FONT>', r'\1\n', body, re.DOTALL)
            body = re.sub(r'<SPAN STYLE="margin-left:-17pt;text-indent:0pt;width: 17pt">(.*?)</span>', r'\1', body, re.DOTALL)

            # Try again with the font
            for pattern in [r'<FONT FACE="Arial".*?>(.*?)</FONT>',r'<FONT FACE="MS Sans Serif".*?>(.*?)</FONT>']:
                for m in reversed([_ for _ in re.finditer(pattern, body, re.DOTALL)]):
                    body = body[:m.start()] + m.groups()[0] + body[m.end():]

            with open('rst/'+ fnameroot +'.rst','w') as fpo:
                
                fpo.write('.. _{target:s}: \n\n'.format(target = fnameroot))
                fpo.write('*'*len(title)+'\n')
                fpo.write(title+'\n')
                fpo.write('*'*len(title)+'\n')

                if '</' in body:
                    print('</ in body:', fnameroot)
                
                body = rename(body)

                fpo.write(body)

    aliases_info = {}

    def relocate_files():
        """ parse hhc to figure out folder layout and move files to the appropriate locations """

        with open(glob.glob('_output/*.hhc')[0]) as fp:
            hhc = fp.read()

        os.makedirs('rst/_static')
        shutil.copy2('_output/images/REFPROP.png','rst/_static')
        
        match_top = re.search(r'<UL>(.*)</UL>', hhc, re.DOTALL)

        from lxml import html
        tree = html.fromstring(match_top.groups()[0])
        class DataCollector(object):
            nodes = []
            directories = []
        dc = DataCollector()

        def add_folder(dc, root, kid):
            name, title = kid.getchildren()[0].values()
            assert name == 'Name'
            newtitle = root + '/' + title
            dc.directories.append((newtitle))
            return newtitle

        def add_terminal(dc, root, node):
            if len(node.getchildren()) != 2:
                print('Huh??')
            else:
                filepath = node[1].attrib['value']
                dc.nodes.append(dict(path=root, fname = filepath))

        def parser(tree, root, dc):
            for kid in tree.getchildren():
                #print(kid.tag, kid.values(), kid.getchildren(), tree.values())
                if len(kid.getchildren()) == 2 and kid[1].tag == 'ul' and kid[0].tag == 'object':
                    newroot = add_folder(dc, root, kid[0])
                    parser(kid[1], newroot, dc)
                elif len(kid.getchildren()) == 1 and kid[0].tag == 'object':
                    add_terminal(dc, root, kid[0])
                else:
                    print(len(kid), kid.tag, kid.values())

        parser(tree, '.', dc)

        for direc in dc.directories:
            os.makedirs(os.path.join('rst',direc))

        for node in dc.nodes:
            oldfname = rename(node['fname']).replace('html/','').replace('.htm','.rst')
            if not oldfname.endswith('.rst'):
                oldfname += '.rst'
            oldpath = os.path.join('rst', oldfname)
            
            newpath = os.path.join('rst', node['path'], oldfname)
            if not os.path.exists(oldpath):
                if not os.path.exists(newpath):
                    print('FILE MISSING: ', oldpath)
            else:
                
                old_filename = oldfname.replace('.rst', '.htm')
                mapid = page_indices.get(old_filename, None)
                if mapid is None:
                    old_filename2 = RENAME_MAP_inverted[old_filename.split('.')[0]] + '.htm'
                    mapid = page_indices.get(old_filename2, None)

                # print(old_filename, mapid, )
                aliases_info[newpath.replace('rst\\./','').replace('.rst','.html')] = mapid
                print('Moving', oldpath, 'to', newpath)
                shutil.move(oldpath, newpath)

        # Landing page
        shutil.move('rst/General Information/welcometorefprop.rst', 'rst/index.rst')
        index = open('rst/index.rst').read()
        index += '\n\n.. toctree::\n   :maxdepth: 2\n\n'
        for directory in ['General Information','Menu Commands','Programming','Windows']:
            index += '   ' + directory + '/index.rst\n'
        with open('rst/index.rst','w') as fp:
            fp.write(index)

        os.remove('rst/contents.rst')

        # Construct the index pages for each directory
        for direc in dc.directories:
            new_file = os.path.join('rst', direc, 'index.rst')
            if direc in INDEX_FILES:
                old_filename = INDEX_FILES[direc]
                old_path = os.path.join('rst',old_filename)
                mapid = page_indices.get(old_filename.replace('.rst','.htm'), None)
                if mapid is None:
                    old_filename2 = RENAME_MAP_inverted[old_filename.split('.')[0]] + '.htm'
                    mapid = page_indices.get(old_filename2, None)

                # print(old_filename, mapid, )
                aliases_info[new_file.replace('rst\\./','').replace('.rst','.html')] = mapid
                print('[INDEX]Moving', old_path, 'to', new_file)
                shutil.move(old_path, new_file)
            else:
                # Touch the file
                with open(new_file,'w') as fp:
                    this_direc = direc.replace('\\','/').rsplit('/',1)[1]
                    fp.write('*'*len(this_direc)+'\n')
                    fp.write(this_direc+'\n')
                    fp.write('*'*len(this_direc)+'\n')

            contents = open(new_file).read()
            contents += '\n\n.. toctree::\n   :maxdepth: 2\n\n'
            for file in glob.glob(os.path.join('rst',direc,'*.rst')):
                if 'index.rst' not in file:
                    contents += '   ' + file.replace('\\','/').rsplit('/',1)[1].split('.')[0] + '\n'
            for directory in os.listdir(os.path.abspath(os.path.join('rst',direc))): # See http://stackoverflow.com/a/973492
                if os.path.isdir(os.path.join('rst',direc,directory)):
                    contents += '   ' + directory + '/index\n'

            # Write back
            with open(new_file,'w') as fp:
                fp.write(contents)

        for fname in ['conf.py','Makefile','make.bat']:
            shutil.copy2('template/'+fname, 'rst/'+fname)

    def generate_aliases():

        o = '[MAP]\n'
        def to_key(s):
            return s.upper().replace('\\','_').replace('/','_').replace('.HTML','').replace(' ','_')
        for k,v in six.iteritems(aliases_info):
            o += '#define ' + to_key(k) + ' ' + str(v) + '\n'
        o += '\n\n[ALIAS]\n'
        for k,v in six.iteritems(aliases_info):
            o += to_key(k) + '=' + k.replace('/','\\') + '\n'

        return o

    relocate_files()
    chunk = generate_aliases()
    with open('aliases_backpack.txt','w') as fp:
        fp.write(chunk)

    values = [v for k,v in six.iteritems(aliases_info)]
    for k,v in six.iteritems(page_indices):
        if v not in values:
            print(v)

    # Clean up after ourselves
    shutil.rmtree('_output')

# Example block for 
"""
[MAP]
#define CALCULATE 500
#define FILE_SAVE 101

[ALIAS]
CALCULATE=calculate.html
FILE_SAVE=MenuCommands\FileMenu\filesave.html
"""

if __name__ == '__main__':

    # Unpack the old chm file
    decompile_chm()

    # # Move the RST compilation files into the right place
    # for _file in glob.glob('template/*.*'):
    #     shutil.copy2(_file, 'GUI_rst')
    # if os.path.exists('sphinx/GUIdocs'):
    #     shutil.rmtree('sphinx/GUIdocs')
    # shutil.copytree('rst','sphinx/GUIdocs')

    # subprocess.check_call('make html', shell = True, cwd = 'rst', stdout = sys.stdout, stderr = sys.stderr)
    # subprocess.check_call('make latexpdf', shell = True, cwd = 'sphinx', stdout = sys.stdout, stderr = sys.stderr)
    subprocess.check_call('make htmlhelp', shell = True, cwd = 'rst', stdout = sys.stdout, stderr = sys.stderr)

    hhp_path = 'rst/_build/htmlhelp/REFPROPdoc.hhp'
    hhp_out = 'rst/_build/htmlhelp/REFPROPdoc-aliases.hhp'
    aliases = open('aliases_backpack.txt').read()
    with open(hhp_path) as fp:
        hhp = fp.read()
    with open(hhp_out,'w') as fp:
        fp.write(hhp+'\n'+aliases)

    cmns = dict(shell = True, cwd = 'rst/_build/htmlhelp', stdout = sys.stdout, stderr = sys.stderr, universal_newlines=True)
    
    # Compile the CHM file
    subprocess.call(r'"C:\Program Files (x86)\HTML Help Workshop\hhc.exe" REFPROPdoc-aliases.hhp', **cmns)

    # Re-decompile again to see what is inside
    subprocess.check_call('Hh -decompile ../built_CHM_output REFPROPdoc.CHM', **cmns)

    # Launch the CHM at the given MAPID
    subprocess.check_call('Hh  -mapid 800 REFPROPdoc.CHM', **cmns)