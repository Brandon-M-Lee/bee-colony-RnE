import os

pearson_lst = [0 for i in range(9)]
spearman_lst = [0 for i in range(9)]
kendall_lst = [0 for i in range(9)]

for state in os.listdir('data/correlation'):
    if state == 'upper 0.7' or state == 'useful data' or state == 'pearson_plus_minus.txt' or state == 'graph':
        continue
    with open(f'data/correlation/{state}', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        pearson_lines = lines[2:11]
        spearman_lines = lines[13:22]
        kendall_lines = lines[24:33]
        for idx in range(9):
            pearson_line = pearson_lines[idx]
            if float(pearson_line[:-1].split(' ')[-1]) > 0.7:
                pearson_lst[idx] += 1
            spearman_line = spearman_lines[idx]
            if float(spearman_line[:-1].split(' ')[-1]) > 0.7:
                spearman_lst[idx] += 1
            kendall_line = kendall_lines[idx]
            if float(kendall_line[:-1].split(' ')[-1]) > 0.7:
                kendall_lst[idx] += 1

print(pearson_lst)
print(spearman_lst)
print(kendall_lst)