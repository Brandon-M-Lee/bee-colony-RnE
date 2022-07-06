import os
import csv

dir_path = "./data/states"
states_list = list()

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        temp = file_path[file_path.index("\\"):]
        states_list.append(file_path)
print(states_list)
correct = list()
incorrect = list()
for file in states_list:
    f = open(file, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    years = len(list(rdr))
    if years == 31:
        correct.append(file[file.index("\\")+1 : file.index("csv")-1])
    else:
        incorrect.append(file[file.index("\\")+1 : file.index("csv")-1])
    f.close()  

print(correct)
print("else:")
print(incorrect)