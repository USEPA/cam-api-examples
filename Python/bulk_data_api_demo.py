import requests
import json
import sys
from datetime import datetime
from datetime import date
import os

# The bulk data api allows you to download prepackaged data sets. There are two endpoints for obtaining bulk data.
# The first is the /bulk-files endpoint which returns metadata about files. This metadata includes the path to the
# file.  The second is the /easey/bulk-files endpoint which along with the path, returns the actual file.

# Set your API key here
API_KEY = 'YOUR_API_KEY'
# S3 bucket url base + s3Path (in get request) = the full path to the files
BUCKET_URL_BASE = 'https://api.epa.gov/easey/bulk-files/'

parameters = {
    'api_key': API_KEY
}

# change this to the date you want to start downloading files from
# all files after this date and time will be downloaded
dateToday = date.today()
month, year = (dateToday.month-1, dateToday.year) if dateToday.month != 1 else (12, dateToday.year-1)
prevMonth = dateToday.replace(day=1, month=month, year=year)
timeOfLastDownload = datetime.fromisoformat(str(prevMonth)+"T00:00:00.000Z"[:-1] + '+00:00')

# executing get request
response = requests.get("https://api.epa.gov/easey/camd-services/bulk-files", params=parameters)

# printing the response error message if the response is not successful
print("Status code: "+str(response.status_code))
if (int(response.status_code) > 399):
    sys.exit("Error message: "+response.json()['error']['message'])

# converting the content from json format to a data frame
resjson = response.content.decode('utf8').replace("'", '"')
bulkFiles = json.loads(resjson)

####### Meta Data #######

# print out unique data types in the bulk data files
print('Unique data types in the bulk data files:')
print(set([fileObj['metadata']['dataType'] for fileObj in bulkFiles]))

# select Mercury and Air Toxics Emissions (MATS) files
matsFiles = [fileObj for fileObj in bulkFiles if (fileObj['metadata']['dataType']=="Mercury and Air Toxics Emissions (MATS)")]

# print out unique data sub types in the bulk data files
print('Unique data sub types in the bulk data files:')
print(set([fileObj['metadata']['dataSubType'] for fileObj in matsFiles]))

# check if state groupings exist in any of the files
print('State groupings in the bulk data files:')
print(set([fileObj['metadata']['stateCode'] for fileObj in matsFiles if ('stateCode' in fileObj['metadata'].keys())]))

# check if quarterly groupings exist in any of the files
print('Quarterly groupings in the bulk data files:')
print(set([fileObj['metadata']['quarter'] for fileObj in matsFiles if ('quarter' in fileObj['metadata'].keys())]))

####### Hourly Emissions Files #######

# filter by emissions files
emissionsFiles = [fileObj for fileObj in bulkFiles if (fileObj['metadata']['dataType']=="Emissions")]

# filter by hourly virginia emissions files
hourlyEmissionsFiles = [fileObj for fileObj in emissionsFiles if (fileObj['metadata']['dataSubType']=="Hourly")]
virginiaHourlyEmissionsFiles = [fileObj for fileObj in hourlyEmissionsFiles if ('stateCode' in fileObj['metadata'].keys() and fileObj['metadata']['stateCode'] == 'VA')]

# filter files since last download (timeOfLastDownload)
filesToDownload = [fileObj for fileObj in virginiaHourlyEmissionsFiles if datetime.fromisoformat(fileObj['lastUpdated'][:-1] + '+00:00') > timeOfLastDownload]
print('Number of files to download: '+str(len(filesToDownload)))

# print the size of all files to download
downloadMB = sum(int(fileObj['megaBytes']) for fileObj in filesToDownload)
print('Total size of files to download: '+str(downloadMB)+' MB')

# make a data folder if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

if len(filesToDownload) > 0:
    # loop through all files and download them
    for fileObj in filesToDownload:
        url = BUCKET_URL_BASE+fileObj['s3Path']
        print('Full path to file on S3: '+url)
        # download and save file
        response = requests.get(url)
        # save file to disk in the data folder
        with open('data/'+fileObj['filename'], 'wb') as f:
            f.write(response.content)
else:
    print('No files to download')
