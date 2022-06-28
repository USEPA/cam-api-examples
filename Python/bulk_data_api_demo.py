import sys
import io
import requests
import pandas as pd

API_KEY = 'YOUR_API_KEY'
# S3 bucket url base - s3Path in get requests along with this base url
# is the full path to the files
BUCKET_URL_BASE = 'https://api.epa.gov/easey/dev/bulk-files/'

parameters = {
    'api_key': API_KEY
}

# executing get request
response = requests.get("https://api.epa.gov/easey/dev/camd-services/bulk-files", params=parameters)

# printing status code
print("Status code: "+str(response.status_code))

# initialize data frame
dailyEmissions = pd.DataFrame()

# look through json objects of the request
for obj in response.json():
    # store metadata of the file
    objMeta = obj["metadata"]
    # look for 'year', 'quarter', 'datatype', 'datasubtype' in key names
    if all(x in objMeta.keys() for x in ['year', 'quarter', 'datatype', 'datasubtype']):
        # collect only 2021 daily emission files (quarter files at this point)
        if (objMeta['year'] == '2021') & (objMeta['datatype'] == 'Emissions') & (objMeta['datasubtype'] == 'Daily'):
            # print url, get content and concatenate to dailyEmissions
            url = BUCKET_URL_BASE+obj["s3Path"]
            print("Full path to file on S3: "+url)
            r = requests.get(url).content
            df = pd.read_csv(io.StringIO(r.decode('utf-8')))
            dailyEmissions = pd.concat([dailyEmissions,df])

# print head of data frame and number of rows
print(dailyEmissions.head())
print("Number of records for 2021 daily emissions: "+str(dailyEmissions.shape[0]))
