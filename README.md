# EPA's Clean Air Markets (CAM) API Examples
The purpose of this repo is to provide users examples on how to use the Clean Air Market's (CAM) APIs using Python and R. Users can find documentation of the APIs in the [CAM API Portal](https://www.epa.gov/airmarkets/cam-api-portal).

## Background
### About EPA's Clean Air Markets
To learn more about the programs associated with the data through these APIs, as well as other information, visit the [Clean Air Markets Division (CAMD) homepage](https://www.epa.gov/airmarkets).
<br/><br/>

### Data.gov API key
Visit [https://api.data.gov/](https://api.data.gov/) to find API documentation for various Federal Government Deparment and Agencies. Be sure to [sign up for an API key](https://www.epa.gov/airmarkets/cam-api-portal#/api-key-signup) which can be used not only for the CAM APIs, but also for the other APIs you can find from api.data.gov.
<br/><br/>

## Python Scripts Description
Recommended versions of Python to have installed to use these scripts is 3.8, 3.9 or 3.10.

Before executing the scripts, install the following packages.

`pip install requests`

`pip install pandas`
<br/><br/>

### Python/bulk_data_api_demo.py
The script retrieves daily emissions files by the quarter of 2021 using the camd-services API. The script then concatenates the files to make a single data frame. Additionally, the script will also download XML files to a local directory.

<ol>
<li>In the file, insert your API key at: `API_KEY = 'YOUR_API_KEY'`</li>
<li>To execute the script run in your terminal:<br>

`cd Python/`<br>
`python bulk_data_api_demo.py`
</li>
<li>If successful, you will see a response, `Status code: 200`.</li>
</ol>
<br/><br/>

### Python/emissions_data_demo.py
The script retrieves annual emissions attribute data by using the streaming-services and emission-mgmt APIs. The script also prints out useful data from the response headers too.

<ol>
<li>In the file, insert your API key at: `API_KEY = 'YOUR_API_KEY'`</li>
<li>To execute the script run in your terminal:<br>

`cd Python/`<br>
`python emissions_data_demo.py`
</li>
<li>If successful, you will see a response, `Status code: 200`.</li>
</ol>
<br/><br/>

### Python/facility_data_demo.py
The script retrieves facility attribute data by using the streaming-services and facilities-mgmt APIs. The script also prints out useful data from the response headers too.

<ol>
<li>In the file, insert your API key at: `API_KEY = 'YOUR_API_KEY'`</li>
<li>To execute the script run in your terminal:<br>

`cd Python/`<br>
`python facilities_api_demo.py`</br>
</li>
<li>If successful, you will see a response, `Status code: 200`.</li>
</ol>
<br/><br/>

## R Scripts Description
Recommended versions of R to have installed to use these scripts is R (>= 3.2).

Before executing the scripts, install the following packages.

`install.packages("httr")`

`install.packages("htmltools")`

`install.packages("jsonlite")`
<br/><br/>

### R/bulk_data_api_demo.R

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves CSAPR compliance data and daily emissions data using the camd-services API. Additionally, the script will also download XML files to a local directory.

Use RStudio to run the script.
<br/><br/>

### R/emissions_data_demo.R

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves annual emissions attribute data by using the streaming-services and emission-mgmt APIs. The script also prints out useful data from the response headers too.

Use RStudio to run the script.
<br/><br/>

### R/facility_data_demo.R

Insert your API key at

`apiKEY <- "YOUR_API_KEY"`

The script retrieves annual emissions attribute data by using the streaming-services and facilities-mgmt APIs. The script also prints out useful data from the response headers too.

Use RStudio to run the script.
<br/><br/>

## Disclaimer  

The United States Environmental Protection Agency (EPA) GitHub project code is provided on an "as is" basis and the user assumes responsibility for its use. EPA has relinquished control of the information and no longer has responsibility to protect the integrity , confidentiality, or availability of the information. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by EPA. The EPA seal and logo shall not be used in any manner to imply endorsement of any commercial product or activity by EPA or the United States Government.
