import os
os.system('pip install -r requirements.txt')
import pandas as pd
import numpy as np
import scipy.stats as stats

for state in os.listdir('data/states'):
    if state == 'NEW JERSEY' or state == 'NEW YORK' or state == 'WEST VIRGINIA':
        continue
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
        try:
            average_temp_low.append(np.mean(sliced_df['Temperature Sampled Low (°F)'].values))
            average_temp_high.append(np.mean(sliced_df['Temperature Sampled High (°F)'].values))
            average_dew_point_low.append(np.mean(sliced_df['Dew Point Sampled Low (°F)'].values))
            average_dew_point_high.append(np.mean(sliced_df['Dew Point Sampled High (°F)'].values))
            average_wind_speed_max.append(np.mean(sliced_df['Wind Speed Max (mph)'].values))
            average_wind_speed_min.append(np.mean(sliced_df['Wind Speed Min (mph)'].values))
            average_precipitation.append(np.mean(sliced_df['Precipitation (in)'].values))
            average_pressure_altimeter_max.append(np.mean(sliced_df['Pressure Altimeter Min (in Hg)'].values))
            average_pressure_altimeter_min.append(np.mean(sliced_df['Pressure Altimeter Max (in Hg)'].values))
        except:
            print(f'{state} {year}')

    average_temp_high = np.array(average_temp_high)
    average_temp_low = np.array(average_temp_low)
    average_dew_point_high = np.array(average_dew_point_high)
    average_dew_point_low = np.array(average_dew_point_low)
    average_wind_speed_max = np.array(average_wind_speed_max)
    average_wind_speed_min = np.array(average_wind_speed_min)
    average_precipitation = np.array(average_precipitation)
    average_pressure_altimeter_max = np.array(average_pressure_altimeter_max)
    average_pressure_altimeter_min = np.array(average_pressure_altimeter_min)
    
    if os.path.exists(f'data/correlation/{state}.txt'):
        os.remove(f'data/correlation/{state}.txt')

    with open(f'data/correlation/{state}.txt', 'a', encoding='utf-8') as f:
        f.write(f'{state}주의 봉군 데이터와 기후 데이터의 상관 관계\n')

        f.write('pearson 상관계수\n')
        f.write(f'평년 최고 기온: {stats.pearsonr(average_temp_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 기온: {stats.pearsonr(average_temp_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 이슬점: {stats.pearsonr(average_dew_point_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 이슬점: {stats.pearsonr(average_dew_point_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 풍속: {stats.pearsonr(average_wind_speed_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 풍속: {stats.pearsonr(average_wind_speed_min, bee_arr)[0]}\n')
        f.write(f'평년 강수량: {stats.pearsonr(average_precipitation, bee_arr)[0]}\n')
        f.write(f'평년 최고 기압: {stats.pearsonr(average_pressure_altimeter_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 기압: {stats.pearsonr(average_pressure_altimeter_min, bee_arr)[0]}\n\n')

        f.write('spearman 상관계수\n')
        f.write(f'평년 최고 기온: {stats.spearmanr(average_temp_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 기온: {stats.spearmanr(average_temp_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 이슬점: {stats.spearmanr(average_dew_point_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 이슬점: {stats.spearmanr(average_dew_point_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 풍속: {stats.spearmanr(average_wind_speed_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 풍속: {stats.spearmanr(average_wind_speed_min, bee_arr)[0]}\n')
        f.write(f'평년 강수량: {stats.spearmanr(average_precipitation, bee_arr)[0]}\n')
        f.write(f'평년 최고 기압: {stats.spearmanr(average_pressure_altimeter_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 기압: {stats.spearmanr(average_pressure_altimeter_min, bee_arr)[0]}\n\n')

        f.write('kendall tau\n')
        f.write(f'평년 최고 기온: {stats.kendalltau(average_temp_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 기온: {stats.kendalltau(average_temp_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 이슬점: {stats.kendalltau(average_dew_point_high, bee_arr)[0]}\n')
        f.write(f'평년 최저 이슬점: {stats.kendalltau(average_dew_point_low, bee_arr)[0]}\n')
        f.write(f'평년 최고 풍속: {stats.kendalltau(average_wind_speed_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 풍속: {stats.kendalltau(average_wind_speed_min, bee_arr)[0]}\n')
        f.write(f'평년 강수량: {stats.kendalltau(average_precipitation, bee_arr)[0]}\n')
        f.write(f'평년 최고 기압: {stats.kendalltau(average_pressure_altimeter_max, bee_arr)[0]}\n')
        f.write(f'평년 최저 기압: {stats.kendalltau(average_pressure_altimeter_min, bee_arr)[0]}\n')