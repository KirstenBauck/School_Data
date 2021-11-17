import csv
import os
import pandas as pd
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go
from numpy import mean

state_fips = {'AL':['01000', '02000'], 'AK':['02000', '02300'], 'AZ':['04000', '05000'],
            'AR':['05000', '06000'], 'CA':['06000', '08000'], 'CO':['08000', '09000'],
            'CT':['09000', '10000'], 'DE':['10000', '12000'], 'FL':['12000', '13000'],
            'GA':['13000', '15000'], 'HI':['15000', '16000'], 'ID':['16000', '17000'],
            'IL':['17000', '18000'], 'IN':['18000', '19000'], 'IA':['19000', '20000'],
            'KS':['20000', '21000'], 'KY':['21000', '22000'], 'LA':['22000', '23000'],
            'ME':['23000', '24000'], 'MD':['24000', '25000'], 'MA':['25000', '26000'],
            'MI':['26000', '27000'], 'MN':['27000', '28000'], 'MS':['28000', '29000'],
            'MO':['29000', '30000'], 'MT':['30000', '31000'], 'NE':['31000', '32000'],
            'NV':['32000', '33000'], 'NH':['33000', '34000'], 'NJ':['34000', '35000'],
            'NM':['35000', '36000'], 'NY':['36000', '37000'], 'NC':['37000', '38000'],
            'ND':['38000', '39000'], 'OH':['39000', '40000'], 'OK':['40000', '41000'],
            'OR':['41000', '42000'], 'PA':['42000', '44000'], 'RI':['44000', '45000'],
            'SC':['45000', '46000'], 'SD':['46000', '47000'], 'TN':['47000', '48000'],
            'TX':['48000', '49000'], 'UT':['49000', '50000'], 'VT':['51000', '52000'],
            'VA':['52000', '53000'], 'WA':['53000', '54000'], 'WV':['54000', '55000'],
            'WI':['55000', '56000'], 'WY':['56000', '57000']}

state = ''
while len(state) != 2:
    state = input("Which state would you like a map of? (Enter the two letter abbreviation): ").upper()

school_file = os.path.join('data', 'Postsecondary_School_Locations_2021.csv')
population_file = os.path.join('data', f'{state}_Population_Density_2021.csv')

df = pd.read_csv(school_file)
state_only = df[df["STATE"] == state]

population_df = pd.read_csv(population_file)

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Get the List of county names from the population density data
county_names = []
for name in population_df['CTYNAME']:
    county_names.append(' '.join(name.split()[:-1]))

# Itterate through to get only the counties in specific state
features = []
fips_list = []
pop_list = []
for county in range(len(counties['features'])):
    county_name = counties['features'][county]['properties']['NAME']
    if county_name in county_names:
        features.append(counties['features'][county])
        # Get the fips id
        fips_id = counties['features'][county]['id']
        if int(fips_id) > int(state_fips[state][0]) and int(fips_id) < int(state_fips[state][1]):
            fips_list.append(fips_id)
            # Get the density
            index = population_df[population_df['CTYNAME']==f'{county_name} County'].index.values[0]
            pop_density = population_df.iloc[index]['popDensity']
            pop_list.append(pop_density)

# Replace the current county features with only the features for specific state
counties['features'] = features
# Create dataframe of fips and coresponding population density
df = pd.DataFrame({'fips': fips_list, 'pop': pop_list})

# Plot county population density data in specific state
# Question: Should the plot bar take the maximum  density, or the mean density?
fig = px.choropleth(df, geojson=counties, locations='fips', color='pop',
                           color_continuous_scale="Viridis",
                           range_color=(0, round(mean(pop_list), 0)),
                           labels={'pop':'Population Density',
                                  'fips' : 'FIPS'},
                           title = "Population Density vs College and Trade School Locations"
                          )
# Fit to only the counties that we drew
fig.update_geos(fitbounds="locations", visible=False)

#Add scatter plot of school districts
fig.add_trace(go.Scattergeo(
        lon = state_only["X"],
        lat = state_only["Y"],
        mode = 'markers',
        hovertext = state_only["NAME"],
        marker_color = 'rgb(0, 0, 0)'
        ))

if not os.path.exists("maps"):
    os.makedirs("maps")
fig.write_image(os.path.join("maps", f"{state}_pop_density_vs_higher_education.jpeg"))
print(f"{state} map created in 'maps' directory") 
fig.show()
