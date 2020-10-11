# smart_city_aq
NDFU smart city project repository
# Status 
1. CAMS downloader and aggregator (done)
Downloader is based on new CDS API that is state-of-the-art interfate for CAMS since June 2020. To be able launch downloader it's necessary to register at https://ads.atmosphere.copernicus.eu/api-how-to and get key
1.1. Set up CDS following creds into $HOME/.cdsapirc  of current user
url: https://ads.atmosphere.copernicus.eu/api/v2
key: {uid}:{api-key}

1.2 Install CDS API via pip/pip3  (library should work for Python2 and Python 3 as well but within the project Python3 implementation was used)
pip install cdsapi

1.3 Launch wrapper cams_wrapper.sh with command (it's necessary to add +x right for this file via chmod 764 cams_wrapper.sh
./cams_wrapper.sh start_date end_date

1.4 Script will download daily 24 band products for the territory of Ukraine and store them to s3://smart-city-aq/data/raster/cams_european_aq_analysis/ (each product in seperate folder). Following pollutants are selected at the moment - pollutants = ['ammonia', 'carbon_monoxide', 'nitrogen_dioxide', 'nitrogen_monoxide', 'particulate_matter_10um', 'particulate_matter_2.5um','sulphur_dioxide']
