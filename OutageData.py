'''
This code pulls Outage data from CenterPoint
This data has location of outage, number of affected customers, and a
device ID that indicates what failed
Real time data must be collected, because historical data is not avaliable

If this script is run by itself, the data is collected.
This script could be imported into another script, and the function
OutageDataRealTime()
can be used on its own

Data collected from here:
http://gis.centerpointenergy.com/outagetracker/
using the API:
http://gis.centerpointenergy.com/ArcGIS/rest/services/Outage/OUTAGE_TRACKER_OEP/MapServer/0/query

Each Output file is ~25 KB (high end estimate for normal baseline outages)
If collected every 5 minutes, 7.2 MB of storage are needed every day
2.628 GB is needed every year, excluding high intensity events

###
Code Written by:
Kyle Shepherd, at Rice University (Version 1)
kas20@rice.edu
Claire Casey, at Rice University (Version 2)
clc9@rice.edu
Translated to Python by Kyle Shepherd
Oct 24, 2018
###
'''

#### Import BLock ####
# the import block imports needed modules, and spits out a json file with
# version numbers so the code can be repeatable
file = open("OutageDataModuleVersions.json", 'w')
modules = {}

import os
import datetime

import sys
modules['Python'] = dict([('version', sys.version_info)])

import json
modules['json'] = dict([('version', json.__version__)])

import requests
modules['requests'] = dict([('version', requests.__version__)])

json.dump(modules, file, indent=4, sort_keys=True)
file.close()
#### END Import Block ####

def OutageDataRealTime():
    '''
This function does the data import
It imports data from the entire CenterPoint service area.
No inputs required.
The code outputs one file deliminated by |, with the outage data
###
Headers:
Time of creation
OBJECT ID|DEV_ID|DEV_TYPE|ETR|LAMGRID|CKT_SECT_ID|CKTID|NUMAFFECT|OEID|LATITUDE|LONGITUDE|X|Y
###
By tracking OBJECT ID across time, the actual time of restoration can be determined
'''
    if not os.path.exists('RealTimeOutageData'):
        os.makedirs('RealTimeOutageData') # creates data folder if it does not exist
    # the GET request call
    r=requests.get('http://gis.centerpointenergy.com/ArcGIS/rest/services/Outage/OUTAGE_TRACKER_OEP/MapServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=*&outSR=102100')
    text=r.json()
    #gets the Date Response header to get the of the data
    time=datetime.datetime.strptime(r.headers['Date'],'%a, %d %b %Y %H:%M:%S %Z')
    #opens file to save data in
    f=open('RealTimeOutageData/OutageData%04d-%02d-%02dT%02d%02d%02d' % (time.year,time.month,time.day,time.hour,time.minute,time.second),'w')
    #headers
    f.write('%04d-%02d-%02dT%02d%02d%02d\n' % (time.year,time.month,time.day,time.hour,time.minute,time.second))
    f.write('OBJECT ID|DEV_ID|DEV_TYPE|ETR|LAMGRID|CKT_SECT_ID|CKTID|NUMAFFECT|OEID|LATITUDE|LONGITUDE|X|Y\n')
    #gets the data by json parsing
    for data in text["features"]:
        attributes=data["attributes"]
        f.write(str(attributes["OBJECTID"])+'|')
        f.write(str(attributes["DEV_ID"])+'|')
        f.write(str(attributes["DEV_TYPE"])+'|')
        f.write(str(attributes["ETR"])+'|')
        f.write(str(attributes["LAMGRID"])+'|')
        f.write(str(attributes["CKT_SECT_ID"])+'|')
        f.write(str(attributes["CKT_ID"])+'|')
        f.write(str(attributes["CUST_AFFECTED"])+'|')
        f.write(str(attributes["OE_ID"])+'|')
        f.write(str(attributes["LATITUDE"])+'|')
        f.write(str(attributes["LONGITUDE"])+'|')
        geometry=data["geometry"]
        f.write(str(geometry["x"])+'|')
        f.write(str(geometry["y"])+'\n')

if __name__ == "__main__":
    OutageDataRealTime()
