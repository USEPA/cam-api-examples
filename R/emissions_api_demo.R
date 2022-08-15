library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api-easey.app.cloud.gov"
apiKEY <- "YOUR_API_KEY"

# annual emissions url
annualEmissionsUrl <- paste0(apiUrlBase,"/streaming-services/emissions/apportioned/annual?API_KEY=",apiKEY)

# define query parameters
query <- list(year="2020",
              programCodeInfo="CSNOX",
              stateCode=paste0(c("IN","MI"), collapse = '|'))

# API GET request
res = GET(annualEmissionsUrl, query = query)

# print response if status code is not 200
if (length(res$status_code) != 0){
  if (res$status_code != 200){
    print(paste("API status code:",res$status_code,annualEmissionsUrl,"..",res$message))
  }
}

# convert response to a data frame
annualEmissData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(annualEmissData))
