#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 09:27:13 2022

@author: benja
"""

### NOTE: use CMD+1 to comment out/in. Use F9 to run current line (and only that line)



# # Demo file for Spyder Tutorial
# # Hans Fangohr, University of Southampton, UK

# def hello():
#     """Print "Hello World" and return None."""
#     print("Hello World")

# #Main program starts here
# hello()


import os
abspath = os.path.abspath('/Users/benja/Library/CloudStorage/Box-Box/Big_Projects/Carib_Habitat/Python_Bathymetry_TIFF-to-netCDF') ## String which contains absolute path to the script file
os.chdir(abspath) ## Setting up working directory
# os.getcwd() #print current wd

#https://gis.stackexchange.com/questions/226321/no-module-named-osgeo
# pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==`gdal-config --version`

cd /Users/benja/Documents/Carib_Habitat/Bathy_merged_BF/
#https://nsidc.org/data/user-resources/help-center/how-do-i-convert-geotiff-netcdf-file
from osgeo import gdal
#Change the following variables to the file you want to convert (inputfile) and
#what you want to name your output file (outputfile).
inputfile = 'final_merge_6Oct2022_zeros-for-land.tif'
outputfile = 'final_merge_6Oct2022_zeros-for-land.nc'
#Do not change this line, the following command will convert the geoTIFF to a netCDF
ds = gdal.Translate(outputfile, inputfile, format='NetCDF')

# #for this error: 'Warning 1: creating geographic file without lon/lat values!'
# https://gis.stackexchange.com/questions/272184/netcdf-layer-nc-appears-flipped-and-rotated-in-qgis
