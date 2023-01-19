import sys
import io
import requests
import pandas as pd
import json
import os

# The bulk data api allows you to download prepackaged data sets. There are two endpoints for obtainging bulk data.
# The first is the /bulk-files endpoint which returns a metadata about files. This metadata includes the path to the
# file.  The second is the /easey/bulk-files endpoint which along with the path, returns the actual file.

API_KEY = 'YOUR_API_KEY'
# S3 bucket url base + s3Path (in get request) = the full path to the files
BUCKET_URL_BASE = 'https://api.epa.gov/easey/bulk-files/'

parameters = {
    'api_key': API_KEY
}

# executing get request
response = requests.get("https://api.epa.gov/easey/camd-services/bulk-files", params=parameters)

# printing status code
print("Status code: "+str(response.status_code))

# converting the content from json format to a data frame
resjson = response.content.decode('utf8').replace("'", '"')
data = json.loads(resjson)
s = json.dumps(data, indent=4)
jsonread = pd.read_json(s)
pddf = pd.DataFrame(jsonread)
bulkFiles = pd.concat([pddf.drop(['metadata'], axis=1), pddf['metadata'].apply(pd.Series)], axis=1)

####### Compliance Files #######
# filter by csapr compliance files
csaprComplianceFiles = bulkFiles[(bulkFiles['dataType']=="Compliance") & (bulkFiles['programCode'].str.contains('CS'))]
#print(csaprComplianceFiles)

# initialize data frame
complianceData = pd.DataFrame()
for s3Path in csaprComplianceFiles['s3Path']:
    url = BUCKET_URL_BASE+s3Path
    print('Full path to file on S3: '+url)
    # converting response to data frame and adding rows to dailyEmissions
    res = requests.get(url).content
    df = pd.read_csv(io.StringIO(res.decode('utf-8')))
    complianceData = pd.concat([complianceData,df])

#print(complianceData.head())
print("Number of records for CSAPR Compliance: "+str(complianceData.shape[0]))

####### Emission Files #######
# filter by daily emission by the quarter for 2020
quarterDailyEmissionFiles = bulkFiles[bulkFiles['filename'].str.contains('emissions-daily-2020-q')]

# initialize data frame
dailyEmissions = pd.DataFrame()

# iterate over s3 paths for each file and add to dailyEmissions
for s3Path in quarterDailyEmissionFiles['s3Path']:
    url = BUCKET_URL_BASE+s3Path
    print('Full path to file on S3: '+url)
    # converting response to data frame and adding rows to dailyEmissions
    res = requests.get(url).content
    df = pd.read_csv(io.StringIO(res.decode('utf-8')))
    dailyEmissions = pd.concat([dailyEmissions,df])

# print out head and number of rows
#print(dailyEmissions.head())
print("Number of records for 2020 daily emissions: "+str(dailyEmissions.shape[0]))

####### XML Files #######
import zipfile
# reduce down to get the XML files for Alabama
mpXmlEdrFiles = bulkFiles[(bulkFiles['dataType']=="XML") & (bulkFiles['dataSubType']=="Monitoring Plan")]

# get Alabama XML files
alabamaXmlFiles = mpXmlEdrFiles[mpXmlEdrFiles['stateCode'] =="AL"]
#print(alabamaXmlFiles)

# make directory for XML files
currentDirectory = os.getcwd()
alabamaDirPath = os.path.join(currentDirectory,'AlabamaXML')
if not os.path.exists(alabamaDirPath):
    os.mkdir(alabamaDirPath)

# Download XML files and place them in alabamaDirPath directory
for index, row in alabamaXmlFiles.iterrows():
    s3Path = row['s3Path']
    filename = row['filename']
    url = os.path.join(BUCKET_URL_BASE,s3Path)
    print('Full path to file on S3: '+url)
    zipFilePath = os.path.join(alabamaDirPath,filename)
    response = requests.get(url)
    open(zipFilePath, "wb").write(response.content)
    with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
        zip_ref.extractall(alabamaDirPath)
