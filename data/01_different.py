import codecs, os, re

tags = set()
for ann in os.listdir(os.getcwd()):
    if ann.endswith('.ann'):
	with open(ann) as f:
	    for line in f:
		if re.search('^T', line) is not None and 'pos_' not in line:
		    try:
			tag = re.search('^T[0-9]+\t([^ ]*)', line).group(1)
			tags.add(tag)
		    except:
			continue
print len(tags)