import requests
import sys
from datetime import datetime
import pandas as pd
import warnings

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all facility data for more than one year.
#######

# Below are examples of querying facility attribute data.

# Set your API key here
API_KEY = 'YOUR_API_KEY'

####### Streaming services API #######
# This is an example of how to use the streaming services API to get facility attribute data.

# Use this API for continuous data streams and avoiding paging through results.

# api parameters for the streaming facility/attributes endpoint
parameters = {
    'api_key': API_KEY,
    'year': '2020|2021',
    'unitFuelType': 'Coal|Natural Gas'
}

if len(parameters['year'].split("|")) > 1: 
    warnings.warn("The request you're making could be too large for the streaming services API and may result in a bad request. Please consider using the bulk data api endpoint instead. An example can be found in the bulk_data_demo.py file.")

# making get request using the facilities/attributes endpoint
streamingUrl = "https://api.epa.gov/easey/streaming-services/facilities/attributes"
streamingResponse = requests.get(streamingUrl, params=parameters)

# printing the response error message if the response is not successful
print("Status code: "+str(streamingResponse.status_code))
if (int(streamingResponse.status_code) > 399):
    sys.exit("Error message: "+streamingResponse.json()['error']['message'])

print("Field Mappings: "+str(streamingResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
streamingResponse_df = pd.DataFrame(streamingResponse.json())
print(streamingResponse_df)

####### Facilities mgmt API #######
# This is an example of how to use the facilities mgmt API to get facility attribute data.

# Use this API for getting data in pages.

import math

# api parameters for the facility attributes endpoint
parameters = {
    'api_key': API_KEY,
    'year': 2020,
    'unitFuelType': 'Coal|Natural Gas',
    'page': 1,
    'perPage': 100
}

# making get request
facilitiesUrl = "https://api.epa.gov/easey/facilities-mgmt/facilities/attributes"
facilitiesResponse = requests.get(facilitiesUrl, params=parameters)

print("Status code: "+str(facilitiesResponse.status_code))
if (int(facilitiesResponse.status_code) > 399):
    sys.exit("Error message: "+facilitiesResponse.json()['error']['message'])

# Note: the x-total-count header is the total number of records in the query (not influenced by paging).
totalCount = facilitiesResponse.headers['X-Total-Count']
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
facilitiesResponse_df = pd.DataFrame(facilitiesResponse.json())
print(facilitiesResponse_df)

# print other pages of the data if it's available
if math.ceil(int(totalCount)/int(parameters['perPage'])) > 1:
    for x in range(math.ceil(int(totalCount)/int(parameters['perPage']))-1):
        parameters['page'] += 1
        facilitiesResponse = requests.get(facilitiesUrl, params=parameters)
        facilitiesResponse_df = pd.DataFrame(facilitiesResponse.json())
        print(facilitiesResponse_df)
