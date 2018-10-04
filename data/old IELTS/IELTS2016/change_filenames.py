##with open('filenames.txt','r',encoding='utf-8-sig') as f:
##    filenames = f.read().split()
##    names = set([x.split('_')[0] for x in filenames])
##    print('\n'.join(names))

codes = {
'Zubova': 'DZu',
'MTsigunova': 'MTsy',
'MTSigunova': 'MTsy',
'Emelyanova': 'EEm',
'Kuzmenko': 'EKu',
'NM': 'NMa',
'Shalganova': 'TSha',
'Kazakova': 'LKa'
}

def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

import re
import os
files = os.listdir()
studnames = []
with open('new_filenames.csv','w',encoding='utf-8-sig') as f:
    for file in files:
        splfile = file.split('_')
        if splfile[0] in codes:
            if len(splfile) == 2:
                secpart = re.findall('^([A-Za-z]+)(.*)',splfile[1])[0]
                splfile[1] = secpart[0]
                splfile.append(secpart[1])
            if not isint(splfile[1]):
                if splfile[1] not in studnames:
                    studnames.append(splfile[1])
                splfile[1] = str(studnames.index(splfile[1])+1)
            new_filename = codes[splfile[0]]+'_'+'_'.join(splfile[1:])
            os.rename(file,new_filename)
            f.write(file+';'+new_filename+'\n') 
