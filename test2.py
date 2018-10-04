dct = {}
def openfile(dct):
    with open('esl_00013.ann', encoding = 'utf-8') as f:
        text = f.readlines()
        print(text)
    for line in text:
        line = line.split('\t')
        if line[0].startswith('T'):
            if line[1] in dct:
                dct[line[1]] +=1
            else:
                dct[line] = 1
print(dct)
