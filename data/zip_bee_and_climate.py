import os
import shutil

state_list = ['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'FLORIDA', 'GEORGIA', 
 'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
 'MAINE', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 
 'NEW JERSEY', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OREGON', 'PENNSYLVANIA',
 'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 
 'WEST VIRGINIA', 'WISCONSIN', 'WYOMING']

for state in state_list:
    if not os.path.exists('data/states/'+state):
        os.makedirs('data/states/'+state)

def copy_bee_data():
    for bee_data in os.listdir('data/bee/states'):
        state = bee_data[:-4]
        shutil.copy('data/bee/states/'+bee_data, 'data/states/'+state+'/'+state+'_bee.csv')
    shutil.rmtree('data/bee/states/')

def copy_climate_date():
    for file in os.listdir('data/climate/daily summury'):
        state = file.split('_')[0].upper()
        shutil.copy('data/climate/daily summury/'+file, 'data/states/'+state+'/'+state+'_climate.csv')
    os.remove('data/climate/daily summury/'+file)
    shutil.rmtree('data/climate/daily summury')

# copy_bee_data()
copy_climate_date()