##with open('filenames.txt','r',encoding='utf-8-sig') as f:
##    filenames = f.read().split()
##    names = set([x.split('_')[0] for x in filenames])
##    print('\n'.join(names))


import os
files = os.listdir()
studnames = []
with open('new_filenames.csv','w',encoding='utf-8-sig') as f:
    for file in files:
      if file.endswith('.txt') or file.endswith('.json') or file.endswith('.ann'):
        if '_' in file:
          splfile = file.split('_')
          if splfile[0] not in studnames:
            studnames.append(splfile[0])
          splfile[0] = str(studnames.index(splfile[0])+31)
          splfile[1] = splfile[1].replace('tsk','')
          new_filename = '_'.join(splfile)
        else:
          splfile = file.split('.')

          new_filename = splfile[0] + '_' + splfile[1] + '.' + splfile[2]
        os.rename(file,new_filename)
        f.write(file+';'+new_filename+'\n')
          
