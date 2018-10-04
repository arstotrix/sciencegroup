import os
import json
from ielts.parse_ielts import def_sex
from transliterate import translit, get_available_language_codes
from collections import OrderedDict
import re

with open('new_filenames_googledoc.csv','r',encoding='utf-8-sig') as f:
    alignment = {x.strip().split('\t')[1]:x.strip().split('\t')[0]
                 for x in f.readlines()}

with open('Копия IELTS Essays - Лист1.csv','r',encoding='utf-8-sig') as f:
    meta = {x.strip().split(',')[0]:x.strip().split(',')[1:]
            for x in f.readlines()}

#filename,Grade,Name,Date,Campus,Faculty,"Room, Time",Variant,Task
files = {x[:-4].strip('.') for x in os.listdir()}
authors_names = OrderedDict()
with open('names.csv','w',encoding='utf-8-sig') as n:
    for file in files:
        parts = '_'.join(file.split('_')[:2])
        metadata_to_write = {}
        if file in alignment:
            metadata = meta[alignment[file]]
            name = translit(metadata[1],'ru')
            if name != metadata[1]:
                name = name.replace('ыа','я').replace('иа','ия').replace('ии','ий')
                name = name[:-1] + 'й' if name[-1] == 'ы' else name
            n.write(';'.join([file,metadata[1],name,def_sex(name)])+'\n')
            metadata_to_write = OrderedDict([('sex',def_sex(name)),
                                 ('mark',str(metadata[0]).strip()),
                                 ('study_year','2'),
                                 ('date',str(metadata[2]).strip()),
                                 ('department',metadata[3].strip()+', '+metadata[4].strip()),
                                 ('ielts',"True"),
                                 ('work_type', 'exam'),
                                 ('text_type', 'graph description' if file.endswith('_1') else 'opinion essay')])
        elif parts in alignment:
            metadata = meta[alignment[parts]]
            authors_names['data/IELTS/IELTS2015/'+file+'.json'] = metadata[1]
            name = translit(metadata[1],'ru')
            if name != metadata[1]:
                name = name.replace('ыа','я').replace('иа','ия').replace('ии','ий')
                name = name[:-1] + 'й' if name[-1] == 'ы' else name
            n.write(';'.join([file,metadata[1],name,def_sex(name)])+'\n')
            metadata_to_write = OrderedDict([('sex',def_sex(name)),
                                 ('mark',str(metadata[0]).strip()+' (overall)'),
                                 ('study_year','2'),
                                 ('date',str(metadata[2]).strip()),
                                 ('department',metadata[3].strip()+', '+metadata[4].strip()),
                                 ('ielts',"True"),
                                 ('work_type', 'exam'),
                                 ('text_type', 'graph description' if file.endswith('_1') else 'opinion essay')])
        if metadata_to_write:
            with open(file+'.json','w',encoding='utf-8') as f:
                s = json.dumps(metadata_to_write,ensure_ascii=False)
                f.write(s)

with open('authors_names.json','w',encoding='utf-8') as f:
    f.write(json.dumps(authors_names,ensure_ascii=False))

