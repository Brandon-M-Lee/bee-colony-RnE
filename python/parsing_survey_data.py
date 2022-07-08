import os
os.system('pip3 install -r requirements.txt')
import pandas as pd

data = pd.read_csv('data/Bee Colony Survey Data by State.csv')

states_list = ['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'FLORIDA', 'GEORGIA', 
 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
 'MAINE', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 
 'NEW JERSEY', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OREGON', 'PENNSYLVANIA',
 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 
 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']

for state in states_list:
    with open(f'data/states/{state}.csv', 'w') as f:
        f.write('Year, Data Item, Value\n')

for line in data.loc:
    if line['Period'] == 'MARKETING YEAR' and line['State'] in states_list:
        path = f"data/states/{line['State']}.csv"
        with open(path, 'a') as f:
            f.write(f"{line['Year']}, {line['Data Item']}, {line['Value'].replace(',', '')}\n")