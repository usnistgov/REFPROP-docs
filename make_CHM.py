import subprocess, sys

cmns = dict(shell = True, stdout = sys.stdout, stderr = sys.stderr, universal_newlines=True)

# Build the HTML Help
subprocess.check_call('make htmlhelp', cwd = 'doc', **cmns)

# Inject the map id into the .hhp file
hhp = open('doc/_build/htmlhelp/REFPROPdoc.hhp').read()
aliases = open('aliases_backpack.txt').read().replace('=','=GUI\\')
with open('doc/_build/htmlhelp/REFPROPdoc.hhp','w') as fp:
    fp.write(hhp + '\n\n' + aliases)

# Compile the CHM file from the htmlhelp 
subprocess.call(r'"C:\Program Files (x86)\HTML Help Workshop\hhc.exe" REFPROPdoc.hhp', cwd = 'doc/_build/htmlhelp', **cmns)

# Compile the CHM file from the htmlhelp 
subprocess.call(r'Hh -mapid 700 REFPROPdoc.chm', cwd = 'doc/_build/htmlhelp', **cmns)