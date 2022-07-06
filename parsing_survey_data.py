import os
os.system('pip3 install -r requirements.txt')
import pandas as pd

data = pd.read_csv('data/Bee Colony Survey Data by State.csv')

for line in data.loc:
    if line['Period'] == 'MARKETING YEAR':
        path = f"data/{line['State']}.csv"
        with open(path, 'a') as f:
            f.write(f"{line['Year']}, {line['Data Item']}, {line['Value'].replace(',', '')}\n")