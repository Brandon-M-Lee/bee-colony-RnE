import os
os.system('pip3 install -r requirements.txt')
import pandas as pd

data = pd.read_csv('data/bee/Bee Colony Survey Data by State.csv')

states_list = ['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'FLORIDA', 'GEORGIA', 
 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
 'MAINE', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MONTANA', 'NEBRASKA', 
 'NEW JERSEY', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OREGON', 'PENNSYLVANIA',
 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 
 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']

for state in states_list:
    if not os.path.exists('data/bee/states/'):
        os.makedirs('data/bee/states/')
    with open(f'data/bee/states/{state}.csv', 'w') as f:
        f.write('Year, Data Item, Value\n')

for line in data.loc:
    if line['Period'] == 'MARKETING YEAR' and line['State'] in states_list:
        if not os.path.exists('data/bee/states'):
            os.makedirs('data/bee/states')
        path = f"data/bee/states/{line['State']}.csv"
        with open(path, 'a') as f:
            f.write(f"{line['Year']}, {line['Data Item']}, {line['Value'].replace(',', '')}\n")