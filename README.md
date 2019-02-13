# Electrical-Outage-Data-Scraping

This python code pulls electrical outage data from CenterPoint, an electricity provider in Houston, Texas. <br/>
This data has location of outage, number of affected customers, and a device ID that indicates what failed. <br/>
Real time data must be collected, because historical data is not avaliable. <br/>
<br/>
If this script is run by itself, the data is collected.<br/>
This script could be imported into another script, and the function <br/>
OutageDataRealTime() <br/>
can be used on its own. <br/>
<br/>
Data collected from here: <br/>
http://gis.centerpointenergy.com/outagetracker/ <br/>
using the API: <br/>
http://gis.centerpointenergy.com/ArcGIS/rest/services/Outage/OUTAGE_TRACKER_OEP/MapServer/0/query <br/>
<br/>
Each Output file is ~25 KB (high end estimate for normal baseline outages) <br/>
If collected every 5 minutes, 7.2 MB of storage are needed every day. <br/>
2.628 GB is needed every year, excluding high intensity events. <br/>

###<br/>
Code Written by:<br/>
Kyle Shepherd, at Rice University (Version 1)<br/>
kas20@rice.edu<br/>
Claire Casey, at Rice University (Version 2)<br/>
clc9@rice.edu<br/>
Translated to Python by Kyle Shepherd<br/>
Oct 24, 2018<br/>
###<br/>
