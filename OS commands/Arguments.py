import os
import sys

dir = sys.argv[1]
words = sys.argv[2:]
output = {}
for i in words:
    output[i] = 0
for (path, folder_names, folder_files) in os.walk(dir):
    for file_name in folder_files:
        with open(os.path.join(path, file_name)) as file:
            mytext = file.read()
            for w in words:
                output[w] = output[w]+mytext.count(w)

print(output)