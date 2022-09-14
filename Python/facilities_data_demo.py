import requests
import pandas as pd

# These are examples of querying facility data.

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

API_KEY = 'YOUR_API_KEY'

# api parameters for the streaming facility/attributes endpoint
parameters = {
    'api_key': API_KEY,
    'year': 2020,
    'unitFuelType': 'Coal|Natural Gas'
}

# making get request using the facilities/attributes endpoint
streamingUrl = "https://api.epa.gov/easey/streaming-services/facilities/attributes"
streamingResponse = requests.get(streamingUrl, params=parameters)

# printing useful info from the response
print("Status code: "+str(streamingResponse.status_code))
print("Field Mappings: "+str(streamingResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
streamingResponse_df = pd.DataFrame(streamingResponse.json())
print(streamingResponse_df)

####### Facilities mgmt API #######
# This is example shows how to page through results.

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

# Note: the x-total-count header is the total number of records in the response.
# You can use this to determine if you need to make another request to get all the records.
totalCount = facilitiesResponse.headers['X-Total-Count']
print("Status code: "+str(facilitiesResponse.status_code))
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
