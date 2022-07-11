import os

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

with open('heat map/data/regression/ridge.csv', 'w') as f:
    f.write('State,Unemployment\n')
with open('heat map/data/regression/lasso.csv', 'w') as f:
    f.write('State,Unemployment\n')

for state in os.listdir('data/states/'):
    if state in ["NEW JERSEY", "NEW YORK", "WEST VIRGINIA", "COLORADO", "MINNESOTA", "MISSISSIPPI"]:
        continue
    with open(f'data/states/{state}/{state}_regression_1.txt', 'r') as f:
        lines = f.readlines()
        with open('heat map/data/regression/ridge.csv', 'a') as f2:
            f2.write(f"{state_symbol[state[0]+(state[1:].lower())]},{float(lines[2][:-1].split(':')[-1])}\n")
        with open('heat map/data/regression/lasso.csv', 'a') as f3:
            f3.write(f"{state_symbol[state[0]+(state[1:].lower())]},{float(lines[11][:-1].split(':')[-1])}\n")