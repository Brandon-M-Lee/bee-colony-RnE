import os

from sympy import rotations
os.system('pip3 install -r requirements.txt')
import matplotlib.pyplot as plt

for state in os.listdir('data/correlation'):
    if state == 'upper 0.7' or state == 'useful data' or state == 'pearson_plus_minus.txt' or state == 'graph':
        continue
    with open(f'data/correlation/{state}', 'r', encoding='utf-8') as f:
        x = ['Temperature Sampled High', 'Temperature Sampled Low', 'Dew Point Sampled High', 'Dew Point Sampled Low', 'Wind Speed Max', 'Wind Speed Min', 'Precipitation', 'Pressure Altimeter Max', 'Pressure Altimeter Min']
        y = [float(line[:-1].split(' ')[-1]) for line in f.readlines()[2:11]]
        plt.bar(x, y)
        plt.axhline(y=0.7, color='r', linewidth=1)
        plt.axhline(y=-0.7, color='r', linewidth=1)
        plt.title(state[:-4])
        plt.xticks(rotation=15, fontsize=7)
        plt.ylabel('pearson correlation coefficient')
        plt.savefig(f'data/correlation/graph/{state[:-4]}.png')
        plt.clf()