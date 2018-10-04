import os

for f in os.listdir('.'):
    if f.endswith('.ann') or f.endswith('.txt'):
	os.rename(f, '1_' + f)