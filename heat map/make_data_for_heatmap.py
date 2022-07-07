import pandas as pd

data = pd.read_csv('./merge_states.csv')
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

for year in range(1987, 2018):
    with open(f'heat map/data/{year}.csv', 'a') as f:
        f.write('State, Unemployment\n')
        try:
            for line in data.loc:
                if line['Year'] == year:
                    state = line['State'].lower()
                    state = state[0].upper() + state[1:]
                    f.write(f'{state_symbol[state]},{line["Value"]}\n')
        except:
            pass
