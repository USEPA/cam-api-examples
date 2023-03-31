import requests
import sys
from datetime import datetime
import pandas as pd

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all holdings or transactions data for a whole program.
#######

# Below are examples of querying hourly and annual emissions data.

# Set your API key here
API_KEY = 'YOUR_API_KEY'

####### Streaming services API #######
# This is an example of how to use the streaming services API to get account holdings and allowance compliance data.

# Use this API for continuous data streams and avoiding paging through results.

### Account Holdings ###
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
if (int(accountHoldingsResponse.status_code) > 399):
    sys.exit("Error message: "+accountHoldingsResponse.json()['error']['message'])

print("Field Mappings: "+str(accountHoldingsResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
accountHoldingsResponse_df = pd.DataFrame(accountHoldingsResponse.json())
print(accountHoldingsResponse_df)

### Allowance Compliance ###
# api parameters for the streaming allowance compliance endpoint
parameters = {
    'api_key': API_KEY,
    'programCodeInfo': 'ARP',
    'year': '|'.join(str(y) for y in range(2010,2021))
}

# making get request using the allowance compliance endpoint
allowanceComplianceUrl = "https://api.epa.gov/easey/streaming-services/allowance-compliance"
allowanceComplianceResponse = requests.get(allowanceComplianceUrl, params=parameters)

# printing useful info from the response
print("Status code: "+str(allowanceComplianceResponse.status_code))
if (int(allowanceComplianceResponse.status_code) > 399):
    sys.exit("Error message: "+allowanceComplianceResponse.json()['error']['message'])

print("Field Mappings: "+str(allowanceComplianceResponse.headers['X-Field-Mappings']))
# collecting data as a data frame
allowanceComplianceResponse_df = pd.DataFrame(allowanceComplianceResponse.json())
print(allowanceComplianceResponse_df)


####### Account mgmt API #######
# This is an example of how to use the account mgmt API to get account holdings and allowance compliance data.

### Account Holdings ###
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

print("Status code: "+str(accountHoldingsPageResponse.status_code))
if (int(accountHoldingsPageResponse.status_code) > 399):
    sys.exit("Error message: "+accountHoldingsPageResponse.json()['error']['message'])

# Note: the x-total-count header is the total number of records in the query (not influenced by paging).
totalCount = accountHoldingsPageResponse.headers['X-Total-Count']
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
accountHoldingsPage_df = pd.DataFrame(accountHoldingsPageResponse.json())
print(accountHoldingsPage_df)


### Allowance Compliance ###
# api parameters for the allowance compliance endpoint
parameters = {
    'api_key': API_KEY,
    'programCodeInfo': 'ARP',
    'year': '|'.join(str(y) for y in range(2010,2021)),
    'page': 1,
    'perPage': 10
}

# making get request
allowanceCompliancePageUrl = "https://api.epa.gov/easey/account-mgmt/allowance-compliance"
allowanceCompliancePageResponse = requests.get(allowanceCompliancePageUrl, params=parameters)

print("Status code: "+str(allowanceCompliancePageResponse.status_code))
if (int(allowanceCompliancePageResponse.status_code) > 399):
    sys.exit("Error message: "+allowanceCompliancePageResponse.json()['error']['message'])

# Note: the x-total-count header is the total number of records in the query (not infuenced by paging).
totalCount = allowanceCompliancePageResponse.headers['X-Total-Count']
print("Status code: "+str(allowanceCompliancePageResponse.status_code))
#print("Field Mappings: "+str(response.headers['X-Field-Mappings']))
print("Total Count: "+str(totalCount))

# print the first page of the data
allowanceCompliancePage_df = pd.DataFrame(allowanceCompliancePageResponse.json())
print(allowanceCompliancePage_df)
