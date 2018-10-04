import os

def openfile(f, root, dct):
    name = os.path.join(root,f)
    with open(name, encoding = 'utf-8') as f:
        text = f.read().split('\n')
    #print(text[:100])
        for t in text:
            t = t.split('\t')
            #print(t)
            if t[0].startswith('T'):
                print(t)
    return dct

dct = {}


start_path = "data"
for root, dirs, files in os.walk(start_path):
    #print(root)
    #print(dirs)
    #print(files)
    for f in files:
        if f.endswith('.ann'):
            dct = openfile(f, root, dct)

        
