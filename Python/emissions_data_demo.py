import requests
import pandas as pd

# These are examples of querying annual emissions data.

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

API_KEY = 'YOUR_API_KEY'

# api parameters for the streaming facility/attributes endpoint
parameters = {
    'api_key': API_KEY,
    'year': 2021,
    'programCodeInfo': 'CSOSG2|CSOSG3',
}

# making get request using the emissions/apportioned/annual endpoint
streamingUrl = "https://api.epa.gov/easey/streaming-services/emissions/apportioned/annual"
streamingResponse = requests.get(streamingUrl, params=parameters)

# printing useful info from the response
print("Status code: "+str(streamingResponse.status_code))
print("Field Mappings: "+str(streamingResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
streamingResponse_df = pd.DataFrame(streamingResponse.json())
print(streamingResponse_df)

####### Emissions mgmt API #######
# This is example shows how to page through results.

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

# Note: the x-total-count header is the total number of records in the response.
# You can use this to determine if you need to make another request to get all the records.
totalCount = emissionsResponse.headers['X-Total-Count']
print("Status code: "+str(emissionsResponse.status_code))
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
