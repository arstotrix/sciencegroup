##with open('filenames.txt','r',encoding='utf-8-sig') as f:
##    filenames = f.read().split()
##    names = set([x.split('_')[0] for x in filenames])
##    print('\n'.join(names))


codes = {
'Naumov':'INa',
'AAliutova':'AAl',
'Melnik':'AMe',
'PAsalskaya':'EPa',
'MGromov':'MGr',
'INaumo':'INa',
'INaumov':'INa',
'VInogradov':'VVi',
'AStepanova':'ASt',
'MTsygunova':'MTsy',
'Dzubova':'DZu',
'Gromov':'MGr',
'LPasalskaya':'EPa',
'Ershova':'AEr',
'TYakusheva':'TYak',
'Vinogradov':'VVi',
'Tyakusheva':'TYak',
'Polyanskaya':'LPo',
'DZubova':'DZu',
'Pasalsaya':'EPa',
'Khromalenkova':'AKhr',
'Melniik':'AMe',
'Zakhrova':'EZa',
'Pasalsya':'EPa',
'Stukanov':'ASt',
'DArsentyev':'DAr',
'Zakharova':'EZa',
'EEmelyanova':'EEm',
'Pechnikova':'VPe',
'ZEvdaeva':'ZEv',
'Pasalskaya':'EPa',
'EEmelyaova':'EEm',
'KKolosova':'KKo',
'Shatova':'ESha',
'Pasalakaya':'EPa',
'Ogneva':'MOg',
'Degtyar':'ADe',
'Bibaeva':'MBi',
'VKovalevskaya':'VKo'
}

import os
files = os.listdir()
with open('new_filenames.csv','w',encoding='utf-8-sig') as f:
    for file in files:
        if file.split('_')[0] in codes:
            splfile = file.split('_')
            new_filename = codes[splfile[0]]+'_'+'_'.join(splfile[1:])
            os.rename(file,new_filename)
            f.write(file+';'+new_filename+'\n')
            
        
