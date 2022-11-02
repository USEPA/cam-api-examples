import requests
import pandas as pd

# These are examples of querying account data.

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

## Example 1

API_KEY = 'YOUR_API_KEY'

# api parameters for the streaming account holdings endpoint
parameters = {
    'api_key': API_KEY,
    'accountType': 'Facility Account|General Account',
    'programCodeInfo': 'CSOSG3',
    'exclude': 'epaRegion'
}

# making get request using the account holdings endpoint
accountHoldingsUrl = "https://api.epa.gov/easey/streaming-services/allowance-holdings"
accountHoldingsResponse = requests.get(accountHoldingsUrl, params=parameters)

# printing useful info from the response
print("Status code: "+str(accountHoldingsResponse.status_code))
print("Field Mappings: "+str(accountHoldingsResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
accountHoldingsResponse_df = pd.DataFrame(accountHoldingsResponse.json())
print(accountHoldingsResponse_df)

## Example 2

# api parameters for the streaming allowance compliance endpoint
parameters = {
    'api_key': API_KEY,
    'programCodeInfo': 'ARP',
    'year': '|'.join(str(y) for y in range(2010,2021))
}

# making get request using the account compliance endpoint
accountComplianceUrl = "https://api.epa.gov/easey/streaming-services/allowance-compliance"
accountComplianceResponse = requests.get(accountComplianceUrl, params=parameters)

# printing useful info from the response
print("Status code: "+str(accountComplianceResponse.status_code))
print("Field Mappings: "+str(accountComplianceResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
accountComplianceResponse_df = pd.DataFrame(accountComplianceResponse.json())
print(accountComplianceResponse_df)

####### Account mgmt API #######
# This is example shows how to page through results.

## Example 1

# api parameters for the account holdings endpoint
parameters = {
    'api_key': API_KEY,
    'accountType': 'Facility Account|General Account',
    'programCodeInfo': 'CSOSG3',
    'exclude': 'epaRegion',
    'page': 1,
    'perPage': 10
}

# making get request
accountHoldingsPageUrl = "https://api.epa.gov/easey/account-mgmt/allowance-holdings"
accountHoldingsPageResponse = requests.get(accountHoldingsPageUrl, params=parameters)

# Note: the x-total-count header is the total number of records in the response.
# You can use this to determine if you need to make another request to get all the records.
totalCount = accountHoldingsPageResponse.headers['X-Total-Count']
print("Status code: "+str(accountHoldingsPageResponse.status_code))
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
accountHoldingsPage_df = pd.DataFrame(accountHoldingsPageResponse.json())
print(accountHoldingsPage_df)

## Example 2

# api parameters for the account compliance endpoint
parameters = {
    'api_key': API_KEY,
    'programCodeInfo': 'ARP',
    'year': '|'.join(str(y) for y in range(2010,2021)),
    'page': 1,
    'perPage': 10
}

# making get request
accountCompliancePageUrl = "https://api.epa.gov/easey/account-mgmt/allowance-compliance"
accountCompliancePageResponse = requests.get(accountCompliancePageUrl, params=parameters)

# Note: the x-total-count header is the total number of records in the response.
# You can use this to determine if you need to make another request to get all the records.
totalCount = accountCompliancePageResponse.headers['X-Total-Count']
print("Status code: "+str(accountCompliancePageResponse.status_code))
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
accountCompliancePage_df = pd.DataFrame(accountCompliancePageResponse.json())
print(accountCompliancePage_df)
