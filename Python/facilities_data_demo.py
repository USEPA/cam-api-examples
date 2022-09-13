import requests
import json
import pandas as pd

# This is an example of querying facility data.  
# This is example also shows how to page through results.

API_KEY = 'YOUR_API_KEY'

# function for printing json neatly
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# api parameters for the facility attributes endpoint
parameters = {
    'api_key': API_KEY,
    'year': 2020,
    'facilityId': '3|7',
    'page': 1,
    'perPage': 10
}

# making get request
# Note: the x-total-count header is the total number of records in the response.  
# You can use this to determine if you need to make another request to get all the records.
# TODO: add pagination to this example
response = requests.get("https://api.epa.gov/easey/facilities-mgmt/facilities/attributes", params=parameters)
print("Status code: "+str(response.status_code))

# printing in json format
jprint(response.json())

# convert to a data frame and print first 5 rows
response_df = pd.DataFrame(response.json())
print(response_df)
