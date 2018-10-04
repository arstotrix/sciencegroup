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
                #print(t)
                if len(t) > 1:
                    if not t[1].lower().startswith('pos'):
                        t[1] = t[1].split(' ')
                        if t[1][0] in dct:
                            dct[t[1][0]] += 1
                        else:
                            dct[t[1][0]] = 1
        
                    #print(t[1][0],dct[t[1][0]])
    return dct

def filewriter(dct):
    with open ('results.csv', w, encoding = 'utf-8') as f:
        for d in dct:
            f = f.write("{},{}".format(d,dct[d]))

def main():
    dct = {}
    start_path = "data"
    for root, dirs, files in os.walk(start_path):
        #print(root)
        #print(dirs)
        #print(files)
        for f in files:
            if f.endswith('.ann'):
                dct = openfile(f, root, dct)
  
        
if __name__ == "__main__":
    main()
