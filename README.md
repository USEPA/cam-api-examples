# EPA's Clean Air Markets (CAM) API Examples
The purpose of this repo is to provide users examples on how to use the Clean Air Market's (CAM) APIs using R and Python. Users can find documentation of the APIs in the [CAM API Portal](https://www.epa.gov/airmarkets/cam-api-portal).

## Background
### About EPA's Clean Air Markets
To learn more about the programs associated with the data through these APIs, as well as other information, visit the [CAMD webpage](https://www.epa.gov/airmarkets).

### Data.gov API key
Visit [https://api.data.gov/](https://api.data.gov/) to find API documentation across the federal government. Be sure to [sign up for an API key](https://www.epa.gov/airmarkets/cam-api-portal#/api-key-signup) which can be used not only for the CAM APIs, but also for the other APIs you can find from api.data.gov.

## Description of python scripts
Recommended versions of Python to have installed to use these scripts is 3.8, 3.9 or 3.10.

Before executing the scripts, install the following packages.

`pip install requests`

`pip install pandas`

### Python/bulk_data_api_demo.py
Insert your API key at

`API_KEY = 'YOUR_API_KEY'`

The script retrieves daily emissions files by the quarter of 2021 using the camd-services API. The script then concatenates the files to make a single data frame. Additionally, the script will also download XML files to a local directory.

To execute the script run in your terminal:

`cd Python/`
`python bulk_data_api_demo.py`

### Python/emissions_data_demo.R

Insert your API key at

`API_KEY = 'YOUR_API_KEY'`

The script retrieves annual emissions attribute data by using the streaming-services and emission-mgmt APIs. The script also prints out useful data from the response headers too.

Use RStudio to run the script.

### Python/facility_data_demo.py
Insert your API key at

`API_KEY = 'YOUR_API_KEY'`

The script retrieves facility attribute data by using the streaming-services and facilities-mgmt APIs. The script also prints out useful data from the response headers too.

To execute the script run in your terminal:

`cd Python/`
`python facilities_api_demo.py`

## Description of R scripts
Recommended versions of R to have installed to use these scripts is R (>= 3.2).

Before executing the scripts, install the following packages.

`install.packages("httr")`

`install.packages("htmltools")`

`install.packages("jsonlite")`

### R/bulk_data_api_demo.R

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves CSAPR compliance data and daily emissions data using the camd-services API. Additionally, the script will also download XML files to a local directory.

Use RStudio to run the script.

### R/emissions_data_demo.R

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves annual emissions attribute data by using the streaming-services and emission-mgmt APIs. The script also prints out useful data from the response headers too.

Use RStudio to run the script.

### R/facility_data_demo.py

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves annual emissions attribute data by using the streaming-services and facilities-mgmt APIs. The script also prints out useful data from the response headers too.

Use RStudio to run the script.

## Disclaimer  

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity , confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
