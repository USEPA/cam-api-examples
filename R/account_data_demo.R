library(httr)
library(htmltools)
library(jsonlite)
library(dplyr)

#######
# NOTE: If you are looking to download data in bulk, please see the bulk_data_demo.py file.
# An example of a bulk requests is downloading all holdings or transactions data for a whole program.
#######


# Below are examples of querying hourly and annual emissions data.

# Set your API key here
apiKEY <- "YOUR_API_KEY"

# API info
apiUrlBase <- "https://api.epa.gov/easey"

####### Streaming services API #######
# This is an example of how to use the streaming services API to get account holdings and allowance compliance data.

# Use this API for continuous data streams and avoiding paging through results.

### Account Holdings ###

# streaming account holdings endpoint url
accountHoldingsUrl <- paste0(apiUrlBase,"/streaming-services/allowance-holdings?API_KEY=",apiKEY)

# api parameters for the streaming account holdings endpoint
query <- list(accountType=paste0(c("Facility Account","General Account"), collapse = '|'),
              programCodeInfo="CSOSG3",
              exclude="epaRegion")

# making get request using the account holdings endpoint
res = GET(accountHoldingsUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

fieldMappings <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMappings)

# collecting data as a data frame
accountHoldingsData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(accountHoldingsData))

# to get allowances held by the owner/operator
ownerHoldingsData <- accountHoldingsData %>%
  group_by(ownerOperator) %>%
  summarise(totalBlock = sum(totalBlock))

### Allowance Compliance ###

# streaming allowance compliance endpoint url
allowanceComplianceUrl <- paste0(apiUrlBase,"/streaming-services/allowance-compliance?API_KEY=",apiKEY)

# api parameters for the streaming allowance compliance endpoint
query <- list(programCodeInfo="ARP",
              year=paste0(seq(2010,2021), collapse = '|'))

# making get request using the allowance compliance endpoint
res = GET(allowanceComplianceUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

# collecting data as a data frame
allowanceComplianceData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(allowanceComplianceData))

# print out of compliance facilities for ARP in the last 11 years
print(allowanceComplianceData[!is.na(allowanceComplianceData$excessEmissions),])

####### Account mgmt API #######
# This is an example of how to use the account mgmt API to get account holdings and allowance compliance data.

### Account Holdings ###

# allowance holdings endpoint url
accountHoldingsPageUrl <- paste0(apiUrlBase,"/account-mgmt/allowance-holdings?API_KEY=",apiKEY)

# api parameters for the account holdings endpoint
query <- list(accountType=paste0(c("Facility Account","General Account"), collapse = '|'),
              programCodeInfo="CSOSG3",
              stateCode="OH",
              page=1,
              perPage=10)

# making get request
res = GET(accountHoldingsPageUrl, query = query)
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
accountHoldingsPageData <- fromJSON(rawToChar(res$content))
print(head(accountHoldingsPageData))

### Allowance Compliance ###

# allowance compliance endpoint url
allowanceCompliancePageUrl <- paste0(apiUrlBase,"/account-mgmt/allowance-compliance?API_KEY=",apiKEY)

# api parameters for the allowance compliance endpoint
query <- list(programCodeInfo="ARP",
              year=paste0(seq(2010,2021), collapse = '|'),
              page=1,
              perPage=10)

# making get request
res = GET(allowanceCompliancePageUrl, query = query)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

# Note: the x-total-count header is the total number of records in the query (not infuenced by paging).
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
allowanceCompliancePageData <- fromJSON(rawToChar(res$content))
print(head(allowanceCompliancePageData))
