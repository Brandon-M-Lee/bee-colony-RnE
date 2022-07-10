import pandas as pd


state_symbol = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New hampshire': 'NH',
    'New jersey': 'NJ',
    'New mexico': 'NM',
    'New york': 'NY',
    'North carolina': 'NC',
    'North dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode island': 'RI',
    'South carolina': 'SC',
    'South dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}

def colony_by_year():
    data = pd.read_csv('./merge_states.csv')
    for year in range(1987, 2018):
        with open(f'heat map/data/year/{year}.csv', 'a') as f:
            f.write('State, Unemployment\n')
            try:
                for line in data.loc:
                    if line['Year'] == year:
                        state = line['State'].lower()
                        state = state[0].upper() + state[1:]
                        f.write(f'{state_symbol[state]},{line["Value"]}\n')
            except:
                pass

def pearson_plus_minus():
    with open('data/correlation/pearson_plus_minus.txt', 'r', encoding='utf-8') as f:
        plus = 1000000
        minus = 10
        lines = f.readlines()
        with open('heat map/data/pearson/temp_high.csv', 'a') as f_temp_high:
            f_temp_high.write('State,Unemployment\n')
            temp_high_plus = eval(lines[2])
            temp_high_minus = eval(lines[29])
            for state in temp_high_plus:
                state = state[0] + state.lower()[1:]
                f_temp_high.write(f'{state_symbol[state]},{plus}\n')
            for state in temp_high_minus:
                state = state[0] + state.lower()[1:]
                f_temp_high.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/temp_low.csv', 'a') as f_temp_low:
            f_temp_low.write('State,Unemployment\n')
            temp_low_plus = eval(lines[5])
            temp_low_minus = eval(lines[32])
            for state in temp_low_plus:
                state = state[0] + state.lower()[1:]
                f_temp_low.write(f'{state_symbol[state]},{plus}\n')
            for state in temp_low_minus:
                state = state[0] + state.lower()[1:]
                f_temp_low.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/dew_high.csv', 'a') as f_dew_high:
            f_dew_high.write('State,Unemployment\n')
            dew_high_plus = eval(lines[8])
            dew_high_minus = eval(lines[35])
            for state in dew_high_plus:
                state = state[0] + state.lower()[1:]
                f_dew_high.write(f'{state_symbol[state]},{plus}\n')
            for state in dew_high_minus:
                state = state[0] + state.lower()[1:]
                f_dew_high.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/dew_low.csv', 'a') as f_dew_low:
            f_dew_low.write('State,Unemployment\n')
            dew_low_plus = eval(lines[11])
            dew_low_minus = eval(lines[38])
            for state in dew_low_plus:
                state = state[0] + state.lower()[1:]
                f_dew_low.write(f'{state_symbol[state]},{plus}\n')
            for state in dew_low_minus:
                state = state[0] + state.lower()[1:]
                f_dew_low.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/wind_high.csv', 'a') as f_wind_high:
            f_wind_high.write('State,Unemployment\n')
            wind_high_plus = eval(lines[14])
            wind_high_minus = eval(lines[41])
            for state in wind_high_plus:
                state = state[0] + state.lower()[1:]
                f_wind_high.write(f'{state_symbol[state]},{plus}\n')
            for state in wind_high_minus:
                state = state[0] + state.lower()[1:]
                f_wind_high.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/wind_low.csv', 'a') as f_wind_low:
            f_wind_low.write('State,Unemployment\n')
            wind_low_plus = eval(lines[17])
            wind_low_minus = eval(lines[44])
            for state in wind_low_plus:
                state = state[0] + state.lower()[1:]
                f_wind_low.write(f'{state_symbol[state]},{plus}\n')
            for state in wind_low_minus:
                state = state[0] + state.lower()[1:]
                f_wind_low.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/rain.csv', 'a') as f_rain:
            f_rain.write('State,Unemployment\n')
            rain_plus = eval(lines[20])
            rain_minus = eval(lines[47])
            for state in rain_plus:
                state = state[0] + state.lower()[1:]
                f_rain.write(f'{state_symbol[state]},{plus}\n')
            for state in rain_minus:
                state = state[0] + state.lower()[1:]
                f_rain.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/pressure_high.csv', 'a') as f_pressure_high:
            f_pressure_high.write('State,Unemployment\n')
            pressure_high_plus = eval(lines[23])
            pressure_high_minus = eval(lines[50])
            for state in pressure_high_plus:
                state = state[0] + state.lower()[1:]
                f_pressure_high.write(f'{state_symbol[state]},{plus}\n')
            for state in pressure_high_minus:
                state = state[0] + state.lower()[1:]
                f_pressure_high.write(f'{state_symbol[state]},{minus}\n')
        with open('heat map/data/pearson/pressure_low.csv', 'a') as f_pressure_low:
            f_pressure_low.write('State,Unemployment\n')
            pressure_low_plus = eval(lines[26])
            pressure_low_minus = eval(lines[53])
            for state in pressure_low_plus:
                state = state[0] + state.lower()[1:]
                f_pressure_low.write(f'{state_symbol[state]},{plus}\n')
            for state in pressure_low_minus:
                state = state[0] + state.lower()[1:]
                f_pressure_low.write(f'{state_symbol[state]},{minus}\n')

if __name__ == '__main__':
    pearson_plus_minus()