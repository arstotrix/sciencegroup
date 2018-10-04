import os

start_path = "data"
for root, dirs, files in os.walk(start_path):
    #print(root)
    #print(dirs)
    for file in files:
        if file.endswith('.ann'):
            print(file)
            print(root)
