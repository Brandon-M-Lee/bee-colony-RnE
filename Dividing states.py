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
    if years == 32: #이거 변동있을수 있음
        correct.append(file[file.index("\\")+1 : file.index("csv")-1])
    else:
        incorrect.append(file[file.index("\\")+1 : file.index("csv")-1])
    f.close()  

print(correct)
print("else:")
print(incorrect)


merge_states = list()
for file in correct:
    f = open("./data/states\\"+file+".csv", "r", encoding = 'utf-8')
    rdr = list(csv.reader(f))
    # print(file, list(rdr)[:3])
    for i in range(len(rdr)):
        rdr[i].insert(0, file)
    merge_states += rdr
    f.close()

for i in merge_states:
    with open("data/states/merge_states.csv", 'w') as f:
        temp = str(i[0])
        for _ in i[1:]:
            temp += ","+_
        f.write(temp+"\n")