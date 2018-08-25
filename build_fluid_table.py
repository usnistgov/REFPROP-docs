"""
Use Python to generate a quick and dirty HTML table of list of fluids for injection into FAQ

Ian Bell, NIST, 2018
"""
import glob, pandas, six
from ctREFPROP.ctREFPROP import REFPROPFunctionLibrary

okeys = ['FLDNAME','NAME','SYNONYM','CHEMFORM']

RP = REFPROPFunctionLibrary('D:/REFPROP')
RP.SETPATHdll('D:/REFPROP')
infos = []
for fld in glob.glob('D:/REFPROP/FLUIDS/*.FLD'):
    info = {}
    for k in okeys:
        info[k] = RP.REFPROPdll(fld,'',k,0,0,0,0,0,[1]).hUnits
    infos.append(info)
df = pandas.DataFrame(infos)
df.to_csv('fluid_info.csv')

df = df.sort_values(by='FLDNAME')

aliases = dict(FLDNAME='Fluid File',NAME='Name',SYNONYM='Synonym',CHEMFORM='Chemical Formula')
o = '<table>\n'

o += '<tr>\n'
aa = ''
for k in okeys:
    aa += '<td><b>' + aliases[k] + '</b></td>'
o += aa + '\n'
o += '</tr>\n'

for ir, row in df.iterrows():
    o += '<tr>\n'
    aa = ''
    for k in okeys:
        aa += '<td>' + row[k] + '</td>'
    o += aa + '\n'
    o += '</tr>\n'
o += '</table>'
print(o)