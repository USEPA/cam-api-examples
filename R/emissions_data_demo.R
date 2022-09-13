library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api.epa.gov/easey"
apiKEY <- "YOUR_API_KEY"

####### Emissions mgmt API #######

# annual emissions endpoint url
annualEmissionsPageUrl <- paste0(apiUrlBase,"/emissions-mgmt/emissions/apportioned/annual?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              programCodeInfo="CSNOX",
              stateCode=paste0(c("IN","MI"), collapse = '|'),
              page=1,
              perPage=10)

# API GET request
res = GET(annualEmissionsPageUrl, query = query)

# There's useful information in the response headers - here's a few
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
annualEmissDataPage <- fromJSON(rawToChar(res$content))
print(annualEmissDataPage)

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

# streaming annual emissions endpoint url
annualEmissionsUrl <- paste0(apiUrlBase,"/streaming-services/emissions/apportioned/annual?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              programCodeInfo="CSNOX",
              stateCode=paste0(c("IN","MI"), collapse = '|'))

# API GET request
res = GET(annualEmissionsUrl, query = query)

# convert response to a data frame
annualEmissData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(annualEmissData))
