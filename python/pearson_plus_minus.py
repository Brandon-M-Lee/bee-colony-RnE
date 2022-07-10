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
    if state == 'upper 0.7' or state == 'useful data':
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

print('temp_high_plus:', temp_high_plus)
print('temp_high_minus:', temp_high_minus)
print('temp_low_plus:', temp_low_plus)
print('temp_low_minus:', temp_low_minus)
print('dew_high_plus:', dew_high_plus)
print('dew_high_minus:', dew_high_minus)
print('dew_low_plus:', dew_low_plus)
print('dew_low_minus:', dew_low_minus)
print('wind_high_plus:', wind_high_plus)
print('wind_high_minus:', wind_high_minus)
print('wind_low_plus:', wind_low_plus)
print('wind_low_minus:', wind_low_minus)
print('rain_plus:', rain_plus)
print('rain_minus:', rain_minus)
print('pressure_high_plus:', pressure_high_plus)
print('pressure_high_minus:', pressure_high_minus)
print('pressure_low_plus:', pressure_low_plus)
print('pressure_low_minus:', pressure_low_minus)