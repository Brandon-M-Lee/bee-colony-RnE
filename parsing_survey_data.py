import os
os.system('pip3 install -r requirements.txt')
import pandas as pd

data = pd.read_csv('data/Bee Colony Survey Data by State.csv')

for line in data.loc:
    path = f"data/{data.loc[line, 'State']}.csv"
    if data.loc[line, 'Period'] == 'MARKETING YEAR':
        with open(path, 'w') as f:
            f.write((data.loc[line, 'Year'], data.loc[line, 'Data Item'], data.loc[line, 'Value']))