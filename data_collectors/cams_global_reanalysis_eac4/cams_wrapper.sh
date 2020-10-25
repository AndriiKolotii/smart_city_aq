#!/bin/bash
python3 download.py -s $1  -e $2
python3 download_pm.py -s $1  -e $2
mkdir 
for i in `ls| grep nc`; do gdal_translate -a_srs EPSG:4326 -of GTiff -ot Float64  $i cropped/`basename $i .nc`.tif; done
rm *.nc
for i in `ls | grep tif`; do gdalwarp   $i cropped/`basename $i .tif`_cropped.tif  -s_srs  EPSG:4326 -t_srs EPSG:32636; done
for i in `ls cropped/*carbon_monoxide*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/carbon_monoxide/; done
for i in `ls cropped/*nitrogen_dioxide*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/nitrogen_dioxide/; done
for i in `ls cropped/*nitrogen_monoxide*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/nitrogen_monoxide/; done
for i in `ls cropped/*sulphur_dioxide*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/sulphur_dioxide/; done
for i in `ls cropped/*particulate_matter_10um*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/particulate_matter_10um/; done
for i in `ls cropped/*particulate_matter_2.5um*.tif`; do aws s3 cp $i   s3://smart-city-aq/data/raster/cams_global_reanalysis_eac4/particulate_matter_2.5um/; done
rm cropped/*.tif

