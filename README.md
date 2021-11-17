# College/Trade School Locations vs Population Density by County

### Raw Data Used
* To access College/Trade School Locations data as a CSV go [here](https://catalog.data.gov/dataset/postsecondary-school-locations-current). This data is for the current year (2021). To access previous years data go [here](https://catalog.data.gov/dataset?q=Postsecondary+School+Locations&sort=views_recent+desc&as_sfid=AAAAAAX9ZMkaz7eiQfOekNnbhdEYJ_8itjie6jAn8b2wxPtQNnjA1ZHKpgjP79FznBsyOcfT4vEF0CTn_bwNzuzZdmMbiIMGPh8wZhAH0Va2HUsHBVOHADouCXxnhMUClXtNRlk%3D&as_fid=dc61e39c8c5d32aa7c8ccced6c5d89d606bd0f3d&ext_location=Flagstaff%2C+AZ+%2886001%29&ext_bbox=-112.1337%2C34.9758%2C-111.2645%2C36.0102&ext_prev_extent=-114.2578125%2C33.65120829920497%2C-109.1162109375%2C37.23032838760387)
* To access population data by county as a CSV go [here](https://worldpopulationreview.com/us-counties/states/az). This data is for the current year (2021).

### Packages Used
* Creating [Choropleth Maps](https://plotly.com/python/choropleth-maps/) using Plotly to create base map
* Using [ScatterGeo](https://plotly.com/python/reference/scattergeo/) from Plotly to layer maps
* Using urlopen from [urllib.request](https://docs.python.org/3/library/urllib.request.html) to load county fips
* Reading csv files using [pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

### Other
* What are [FIPS](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards) anyways?


# Accessing the Project
1. To access this project you will need to have certain packages in python. It is recomened you create a virtual environment.
    1. To create a virtual environment for Windows:
        1. Install anaconda: To check if anaconda is installed run `conda -V`
        2. Create a virtual environment by running: `conda create -n yourenvname python=x.x anaconda` where you replace "yourenvname" and "x.x". Use python 3.7 for this project.
        3. Activate virtual environment: `activate yourenvname `
        4. Install requirements.txt. First make sure pip is installed by running `pip --version`. If it is not installed run `conda install -c anaconda pip`. Then run `pip install -r requirements.txt`
    2. To create a virtual environment for Mac:
        1. Install virtualenv `pip install virtualenv`
        2. To create virtual environment: `python3 -m venv venv`
        3. Activate virtual environment: `source venv/bin/activate`
        4. Install requirements.txt `pip install -r requirements.txt`
2. After you have the packages run `python individual_states.py` within your virtual environment. From here, you can choose which state you would like to see a map of by typing the [two letter code](https://www.ssa.gov/international/coc-docs/states.html) into the command line.

# Notes on Method
* For the curation of this map, the mean is used for the max of the colorbar. This is because many states have counties on the very low end population density and only a couple at the high end of population density. As such, if the max of the colorbar was set to the max population density, one would not be able to see population density differences in most counties.

# Next Steps for Project
1. Expanding data sets to cover the whole United States
2. Expanding data sets across time
3. Analyzing schools in historically underrepresented communities
4. Drawing conclusions from maps
