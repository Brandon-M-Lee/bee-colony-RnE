import os
#os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np
#import scipy.stats as stats

for state in os.listdir('data/states'):
    texts = list()
    print(state)
    try:
        with open(f'data/correlation/{state}.txt', 'r', encoding='utf-8') as f:
            string = f.readlines()
            
            for i in string:
                if i.find('상관계수') != -1 or i.find('tau') != -1:
                    texts.append(i)
                    continue
                temp = i.split()
                try:
                    if abs(float(temp[-1])) > 0.7:
                        texts.append(i)
                except:
                    pass
        with open('data/correlation/upper 0.7/' + state + '.txt', 'w', encoding='utf-8') as f:
            for i in texts:
                f.write(i)
    except:
        print(f'{state} is NOT found')