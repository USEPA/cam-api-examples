import requests
import sys
from datetime import datetime
import pandas as pd
import warnings

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all hourly emissions data for more than one month
#######

# Below are examples of querying hourly and annual emissions data.

# Set your API key here
API_KEY = 'YOUR_API_KEY'

####### Streaming services API #######
# This is an example of how to use the streaming services API to get hourly emissions data.

# Use this API for continuous data streams and avoiding paging through results.

# api parameters for the streaming emissions/apportioned/hourly endpoint
parameters = {
    'api_key': API_KEY,
    'beginDate': '2021-01-01',
    'endDate': '2021-01-02',
    'programCodeInfo': 'CSOSG2|CSOSG3',
}

date_format = "%Y-%m-%d"
beginDate = datetime.strptime(parameters['beginDate'], date_format)
endDate = datetime.strptime(parameters['endDate'], date_format)
if (endDate - beginDate).days > 31:
    warnings.warn("The request you're making could be too large for the streaming services API and may result in a bad request. Please consider using the bulk data api endpoint instead. An example can be found in the bulk_data_demo.py file.")

# making get request using the emissions/apportioned/hourly endpoint
streamingUrl = "https://api.epa.gov/easey/streaming-services/emissions/apportioned/hourly"
streamingResponse = requests.get(streamingUrl, params=parameters)

# printing the response error message if the response is not successful
print("Status code: "+str(streamingResponse.status_code))
if (int(streamingResponse.status_code) > 399):
    sys.exit("Error message: "+streamingResponse.json()['error']['message'])

print("Field Mappings: "+str(streamingResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
streamingResponse_df = pd.DataFrame(streamingResponse.json())
print(streamingResponse_df)

####### Emissions mgmt API #######
# This is an example of how to use the emissions mgmt API to get annual emissions data.

# Use this API for getting data in pages.

import math

# api parameters for the annual emissions
parameters = {
    'api_key': API_KEY,
    'year': 2021,
    'programCodeInfo': 'CSOSG2|CSOSG3',
    'page': 1,
    'perPage': 100
}

# making get request
emissionsUrl = "https://api.epa.gov/easey/emissions-mgmt/emissions/apportioned/annual"
emissionsResponse = requests.get(emissionsUrl, params=parameters)

print("Status code: "+str(emissionsResponse.status_code))
if (int(emissionsResponse.status_code) > 399):
    sys.exit("Error message: "+emissionsResponse.json()['error']['message'])

# Note: the x-total-count header is the total number of records in the query (not influenced by paging).
totalCount = emissionsResponse.headers['X-Total-Count']
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
emissionsResponse_df = pd.DataFrame(emissionsResponse.json())
print(emissionsResponse_df)

# print other pages of the data if it's available
if math.ceil(int(totalCount)/int(parameters['perPage'])) > 1:
    for x in range(math.ceil(int(totalCount)/int(parameters['perPage']))-1):
        parameters['page'] += 1
        emissionsResponse = requests.get(emissionsUrl, params=parameters)
        emissionsResponse_df = pd.DataFrame(emissionsResponse.json())
        print(emissionsResponse_df)
