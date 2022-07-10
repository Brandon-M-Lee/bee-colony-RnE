import os
os.system('pip install -r requirements.txt')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = 'data/states'
for state in os.listdir(path):
    bee_data = pd.read_csv(f'{path}/{state}/{state}_bee.csv')
    plt.title(f'Changes in the number of bee colonies in {state}')
    plt.xlabel('Year')
    plt.ylabel('Number of bee colonies')
    plt.plot(list(reversed(list(bee_data['Year']))), list(reversed(list(bee_data[' Value']))))
    plt.savefig(f'{path}/{state}/{state}_bee.png')
    plt.clf()