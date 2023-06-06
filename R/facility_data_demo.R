library(httr)
library(htmltools)
library(jsonlite)
library(stringr)

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all facility data for more than one year.
#######

# Below are examples of querying facility attribute data.

# Set your API key here
apiKEY <- "YOUR_API_KEY"


# API info
apiUrlBase <- "https://api.epa.gov/easey"

####### Streaming services API #######
# This is an example of how to use the streaming services API to get facility attribute data.

# Use this API for continuous data streams and avoiding paging through results.

# streaming facility attributes endpoint url
facilitiesUrl <- paste0(apiUrlBase,"/streaming-services/facilities/attributes?API_KEY=",apiKEY)

# api parameters for the streaming facility/attributes endpoint
query <- list(year="2020",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              unitFuelType=paste0(c("Coal","Natural Gas"), collapse = '|'))

if (length(unlist(str_split(query$year,'\\|'))) > 1){
  warning("The request you're making could be too large for the streaming services API and may result in a bad request. Please consider using the bulk data api endpoint instead. An example can be found in the bulk_data_demo.py file.")
}

# making get request using the facilities/attributes endpoint
res = GET(facilitiesUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

fieldMappings <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMappings)

# convert response to a data frame
facilitiesData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(facilitiesData))

####### Facilities mgmt API #######
# This is an example of how to use the facilities mgmt API to get facility attribute data.

# Use this API for getting data in pages.

# facility attributes endpoint url
facilitiesPageUrl <- paste0(apiUrlBase,"/facilities-mgmt/facilities/attributes?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              unitFuelType=paste0(c("Coal","Natural Gas"), collapse = '|'),
              page=1,
              perPage=10)

# making get request using the facilities/attributes endpoint
res = GET(facilitiesPageUrl, query = query)

# Note: the x-total-count header is the total number of records in the query (not influenced by paging).
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
facilityDataPage <- fromJSON(rawToChar(res$content))
print(facilityDataPage)
