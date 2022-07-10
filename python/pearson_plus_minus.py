import os

temp_high_plus = list()
temp_high_minus = list()
temp_low_plus = list()
temp_low_minus = list()
dew_high_plus = list()
dew_high_minus = list()
dew_low_plus = list()
dew_low_minus = list()
wind_high_plus = list()
wind_high_minus = list()
wind_low_plus = list()
wind_low_minus = list()
rain_plus = list()
rain_minus = list()
pressure_high_plus = list()
pressure_high_minus = list()
pressure_low_plus = list()
pressure_low_minus = list()

temp_high_plus.append(0)
temp_high_minus.append(0)
temp_low_plus.append(0)
temp_low_minus.append(0)
dew_high_plus.append(0)
dew_high_minus.append(0)
dew_low_plus.append(0)
dew_low_minus.append(0)
wind_high_plus.append(0)
wind_high_minus.append(0)
wind_low_plus.append(0)
wind_low_minus.append(0)
rain_plus.append(0)
rain_minus.append(0)
pressure_high_plus.append(0)
pressure_high_minus.append(0)
pressure_low_plus.append(0)
pressure_low_minus.append(0)

idx = 0

for state in os.listdir('data/correlation'):
    if state == 'upper 0.7' or state == 'useful data' or state == 'pearson_plus_minus.txt':
        continue
    with open(f'data/correlation/{state}', 'r', encoding='utf-8') as f:
        for line in f.readlines()[2:11]:
            if float(line[:-1].split(' ')[-1]) > 0:
                if idx%9 == 0:
                    temp_high_plus[0] += 1
                    temp_high_plus.append(state[:-4])
                elif idx%9 == 1:
                    temp_low_plus[0] += 1
                    temp_low_plus.append(state[:-4])
                elif idx%9 == 2:
                    dew_high_plus[0] += 1
                    dew_high_plus.append(state[:-4])
                elif idx%9 == 3:
                    dew_low_plus[0] += 1
                    dew_low_plus.append(state[:-4])
                elif idx%9 == 4:
                    wind_high_plus[0] += 1
                    wind_high_plus.append(state[:-4])
                elif idx%9 == 5:
                    wind_low_plus[0] += 1
                    wind_low_plus.append(state[:-4])
                elif idx%9 == 6:
                    rain_plus[0] += 1
                    rain_plus.append(state[:-4])
                elif idx%9 == 7:
                    pressure_high_plus[0] += 1
                    pressure_high_plus.append(state[:-4])
                elif idx%9 == 8:
                    pressure_low_plus[0] += 1
                    pressure_low_plus.append(state[:-4])
            else:
                if idx%9 == 0:
                    temp_high_minus[0] += 1
                    temp_high_minus.append(state[:-4])
                elif idx%9 == 1:
                    temp_low_minus[0] += 1
                    temp_low_minus.append(state[:-4])
                elif idx%9 == 2:
                    dew_high_minus[0] += 1
                    dew_high_minus.append(state[:-4])
                elif idx%9 == 3:
                    dew_low_minus[0] += 1
                    dew_low_minus.append(state[:-4])
                elif idx%9 == 4:
                    wind_high_minus[0] += 1
                    wind_high_minus.append(state[:-4])
                elif idx%9 == 5:
                    wind_low_minus[0] += 1
                    wind_low_minus.append(state[:-4])
                elif idx%9 == 6:
                    rain_minus[0] += 1
                    rain_minus.append(state[:-4])
                elif idx%9 == 7:
                    pressure_high_minus[0] += 1
                    pressure_high_minus.append(state[:-4])
                elif idx%9 == 8:
                    pressure_low_minus[0] += 1
                    pressure_low_minus.append(state[:-4])
            idx += 1

with open('data/correlation/pearson_plus_minus.txt', 'a', encoding='utf-8') as f:
    f.write('temp_high_plus\n')
    f.write(f'{temp_high_plus[0]}\n{temp_high_plus[1:]}\n')
    f.write('temp_low_plus\n')
    f.write(f'{temp_low_plus[0]}\n{temp_low_plus[1:]}\n')
    f.write('dew_high_plus\n')
    f.write(f'{dew_high_plus[0]}\n{dew_high_plus[1:]}\n')
    f.write('dew_low_plus\n')
    f.write(f'{dew_low_plus[0]}\n{dew_low_plus[1:]}\n')
    f.write('wind_high_plus\n')
    f.write(f'{wind_high_plus[0]}\n{wind_high_plus[1:]}\n')
    f.write('wind_low_plus\n')
    f.write(f'{wind_low_plus[0]}\n{wind_low_plus[1:]}\n')
    f.write('rain_plus\n')
    f.write(f'{rain_plus[0]}\n{rain_plus[1:]}\n')
    f.write('pressure_high_plus\n')
    f.write(f'{pressure_high_plus[0]}\n{pressure_high_plus[1:]}\n')
    f.write('pressure_low_plus\n')
    f.write(f'{pressure_low_plus[0]}\n{pressure_low_plus[1:]}\n')
    f.write('temp_high_minus\n')
    f.write(f'{temp_high_minus[0]}\n{temp_high_minus[1:]}\n')
    f.write('temp_low_minus\n')
    f.write(f'{temp_low_minus[0]}\n{temp_low_minus[1:]}\n')
    f.write('dew_high_minus\n')
    f.write(f'{dew_high_minus[0]}\n{dew_high_minus[1:]}\n')
    f.write('dew_low_minus\n')
    f.write(f'{dew_low_minus[0]}\n{dew_low_minus[1:]}\n')
    f.write('wind_high_minus\n')
    f.write(f'{wind_high_minus[0]}\n{wind_high_minus[1:]}\n')
    f.write('wind_low_minus\n')
    f.write(f'{wind_low_minus[0]}\n{wind_low_minus[1:]}\n')
    f.write('rain_minus\n')
    f.write(f'{rain_minus[0]}\n{rain_minus[1:]}\n')
    f.write('pressure_high_minus\n')
    f.write(f'{pressure_high_minus[0]}\n{pressure_high_minus[1:]}\n')
    f.write('pressure_low_minus\n')
    f.write(f'{pressure_low_minus[0]}\n{pressure_low_minus[1:]}\n')