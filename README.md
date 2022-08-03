# EPA's Clean Air Markets (CAM) API Examples
The purpose of this repo is to provide users examples on how to use the Clean Air Market's (CAM) APIs using R and Python. Users can find documentation of the APIs in the [CAM API Portal](https://www.epa.gov/airmarkets/cam-api-portal).

## About EPA's Clean Air Markets
Link to [CAMD webpage](https://www.epa.gov/airmarkets)

## Data.gov API key
Visit [https://api.data.gov/](https://api.data.gov/) to find API documentation across the federal government. You can also [sign up for an API key](https://api.data.gov/signup/).

## Description of python scripts
Recommended versions of Python to have installed to use these scripts is 3.8, 3.9 or 3.10.

Before executing the scripts, install the following packages.

`pip install requests`

`pip install pandas`

### Python\bulk_data_api_demo.py
Insert your API key at

`6 | API_KEY = 'YOUR_API_KEY'`

The script retrieves daily emissions files by the quarter of 2021 using the camd-services API. The script then concatenates the files to make a single data frame.

### Python\facilities_api_demo.py
Insert your API key at

`5 | API_KEY = 'YOUR_API_KEY'`

The script retrieves facility attribute data using the facilities-mgmt API. Change the parameters on line 14 to request other data.

## Description of R scripts
Recommended versions of R to have installed to use these scripts is R (>= 3.2).

Before executing the scripts, install the following packages.

`install.packages("httr")`

`install.packages("htmltools")`

`install.packages("jsonlite")`
