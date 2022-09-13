library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api.epa.gov/easey"
apiKEY <- "YOUR_API_KEY"

####### Emissions mgmt API #######

# facility attributes endpoint url
facilitiesPageUrl <- paste0(apiUrlBase,"/facilities-mgmt/facilities/attributes?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              unitFuelType=paste0(c("Coal","Natural Gas"), collapse = '|'),
              page=1,
              perPage=10)

# API GET request
res = GET(facilitiesPageUrl, query = query)

# There's useful information in the response headers - here's a few
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
facilityDataPage <- fromJSON(rawToChar(res$content))
print(facilityDataPage)

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

# streaming facility attributes endpoint url
facilitiesUrl <- paste0(apiUrlBase,"/streaming-services/facilities/attributes?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              unitFuelType=paste0(c("Coal","Natural Gas"), collapse = '|'))

# API GET request
res = GET(facilitiesUrl, query = query)

# convert response to a data frame
facilitiesData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(facilitiesData))
