import os
os.system('pip3 install -r requirements.txt')
import folium
import pandas as pd

class FoliumTest:
    def __init__(self):
        self._context = 'heat map/data/'

    def hook(self):
        self.show_map()

    def show_map(self, climate):
        state_geo = self._context + "us-states.json"
        state_unemployment = self._context + f"pearson/{climate}.csv"
        state_data = pd.read_csv(state_unemployment)
        m = folium.Map(location=[37, -102], zoom_start=5)
        m.choropleth(
            geo_data = state_geo,
            name='choropleth',
            data=state_data,
            columns=['State','Unemployment'],
            key_on = 'feature.id',
            fill_color = 'BrBG',
            fill_opacity=0.7,
            line_opacity=0.2,
            legent_name='Unemployment Rate (%)'
        )
        folium.LayerControl().add_to(m)
        m.save(f'heat map/map/html/pearson/{climate}.html')

# for year in range(1987, 2018):
#     FoliumTest().show_map(year)
#     print(f'{year} done')

for climate in ['temp_high', 'temp_low', 'dew_high', 'dew_low', 'wind_high', 'wind_low', 'rain', 'pressure_high', 'pressure_low']:
    FoliumTest().show_map(climate)
    print(f'{climate} done')
    