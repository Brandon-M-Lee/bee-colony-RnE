import os
os.system('pip3 install -r requirements.txt')
import folium
import pandas as pd

class FoliumTest:
    def __init__(self):
        self._context = './data/'

    def hook(self):
        self.show_map()

    def show_map(self):
        state_geo = self._context + "us-states.json"
        state_unemployment = self._context + 'US.csv'
        state_data = pd.read_csv(state_unemployment)
        m = folium.Map(location=[37, -102], zoom_start=5)
        m.choropleth(
            geo_data = state_geo,
            name='choropleth',
            data=state_data,
            columns=['State','Unemployment'],
            key_on = 'feature.id',
            fill_color = 'YlGn',
            fill_opacity=0.7,
            line_opacity=0.2,
            legent_name='Unemployment Rate (%)'
        )
        folium.LayerControl().add_to(m)
        m.save('./USA.html')