library(httr)
library(htmltools)
library(jsonlite)

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all hourly emissions data for more than one month
#######

# Below are examples of querying hourly and annual emissions data.

# Set your API key here
apiKEY <- "YOUR_API_KEY"


# API info
apiUrlBase <- "https://api.epa.gov/easey"

####### Streaming services API #######
# This is an example of how to use the streaming services API to get hourly emissions data.

# Use this API for continuous data streams and avoiding paging through results.

# streaming hourly emissions endpoint url
hourlyEmissionsUrl <- paste0(apiUrlBase,"/streaming-services/emissions/apportioned/hourly?API_KEY=",apiKEY)

# api parameters for the streaming emissions/apportioned/hourly endpoint
query <- list(beginDate="2021-01-01",
              endDate="2021-01-02",
              programCodeInfo="CSNOX",
              stateCode=paste0(c("IN","MI"), collapse = '|'))

if (as.Date(query$endDate) - as.Date(query$beginDate) > 31){
  warning("The request you're making could be too large for the streaming services API and may result in a bad request. Please consider using the bulk data api endpoint instead. An example can be found in the bulk_data_demo.py file.")
}

# making get request using the emissions/apportioned/hourly endpoint
res = GET(hourlyEmissionsUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

fieldMappings <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMappings)

# convert response to a data frame
hourlyEmissData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(hourlyEmissData))

####### Emissions mgmt API #######
# This is an example of how to use the emissions mgmt API to get annual emissions data.

# Use this API for getting data in pages.

# annual emissions endpoint url
annualEmissionsPageUrl <- paste0(apiUrlBase,"/emissions-mgmt/emissions/apportioned/annual?API_KEY=",apiKEY)

# api parameters for the annual emissions
query <- list(year="2020",
              programCodeInfo="CSNOX",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              page=1,
              perPage=10)

# making get request
res = GET(annualEmissionsPageUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

# Note: the x-total-count header is the total number of records in the query (not influenced by paging).
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
annualEmissDataPage <- fromJSON(rawToChar(res$content))
print(annualEmissDataPage)
