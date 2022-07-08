import os
os.system('pip install -r requirements.txt')
import pandas as pd
import shutil

def merge_data():
    data_list = list()
    for state in os.listdir('data/climate'):
        if state.endswith('.py') or state.endswith('.md') or state != 'Arkansas':
            continue
        for file in os.listdir('data/climate/'+state+'/daily summury'):
            if not os.path.exists('data/climate/'+state+'/all reports/'+file):
                data_list.append(pd.read_csv('data/climate/'+state+'/daily summury/'+file, error_bad_lines=False).loc[:, [
                    'Date (String)',
                    'Temperature Sampled Low (°F)',
                    'Temperature Sampled High (°F)',
                    'Dew Point Sampled Low (°F)',
                    'Dew Point Sampled High (°F)',
                    'Wind Speed Min (mph)',
                    'Wind Speed Max (mph)',
                    'Precipitation (in)',
                    'Pressure Altimeter Min (in Hg)',
                    'Pressure Altimeter Max (in Hg)'
                ]].fillna(0))

        result = pd.concat(data_list, ignore_index=True)
        result.to_csv('data/climate/'+state+'/daily summury merged.csv', index=False)

def copy_merged_to_other_directory():
    for state in os.listdir('data/climate'):
        if state.endswith('.py') or state.endswith('.md') or state == 'daily summury' or state != 'Arkansas':
            continue
        shutil.copy('data/climate/'+state+'/daily summury merged.csv', 'data/climate/daily summury/'+state+'_daily summury.csv')
        os.remove('data/climate/'+state+'/daily summury merged.csv')

merge_data()
copy_merged_to_other_directory()