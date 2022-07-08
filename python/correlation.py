import os
os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np
import scipy.stats as stats

for state in os.listdir('data/states'):
    climate_df = pd.read_csv(f'data/states/{state}/{state}_climate.csv')
    bee_arr = np.array(pd.read_csv(f'data/states/{state}/{state}_bee.csv')[' Value'])

    average_temp_high = list()
    average_temp_low = list()
    average_dew_point_high = list()
    average_dew_point_low = list()
    average_wind_speed_max = list()
    average_wind_speed_min = list()
    average_precipitation = list()
    average_pressure_altimeter_max = list()
    average_pressure_altimeter_min = list()

    for year in range(1987, 2018):
        fdf = climate_df['Date (String)'] < str(year+1)
        sliced_df = climate_df[fdf]
        average_temp_low.append(np.mean(sliced_df['Temperature Sampled Low (°F)'].values))
        average_temp_high.append(np.mean(sliced_df['Temperature Sampled High (°F)'].values))
        average_dew_point_low.append(np.mean(sliced_df['Dew Point Sampled Low (°F)'].values))
        average_dew_point_high.append(np.mean(sliced_df['Dew Point Sampled High (°F)'].values))
        average_wind_speed_max.append(np.mean(sliced_df['Wind Speed Max (mph)'].values))
        average_wind_speed_min.append(np.mean(sliced_df['Wind Speed Min (mph)'].values))
        average_precipitation.append(np.mean(sliced_df['Precipitation (in)'].values))
        average_pressure_altimeter_max.append(np.mean(sliced_df['Pressure Altimeter Min (in Hg)'].values))
        average_pressure_altimeter_min.append(np.mean(sliced_df['Pressure Altimeter Max (in Hg)'].values))

    average_temp_high = np.array(average_temp_high)
    average_temp_low = np.array(average_temp_low)
    average_dew_point_high = np.array(average_dew_point_high)
    average_dew_point_low = np.array(average_dew_point_low)
    average_wind_speed_max = np.array(average_wind_speed_max)
    average_wind_speed_min = np.array(average_wind_speed_min)
    average_precipitation = np.array(average_precipitation)
    average_pressure_altimeter_max = np.array(average_pressure_altimeter_max)
    average_pressure_altimeter_min = np.array(average_pressure_altimeter_min)
    