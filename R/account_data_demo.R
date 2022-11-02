library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api.epa.gov/easey"
apiKEY <- "YOUR_API_KEY"

####### Streaming services API #######

# If you have a lot of data to request, use the streaming services API to avoid
# pagination and much quicker collection of the data you need.

## Example 1

# streaming account holdings endpoint url
accountHoldingsUrl <- paste0(apiUrlBase,"/streaming-services/allowance-holdings?API_KEY=",apiKEY)

# define query parameters
query <- list(accountType=paste0(c("Facility Account","General Account"), collapse = '|'),
              programCodeInfo="CSOSG3",
              exclude="epaRegion")

# API GET request
res = GET(accountHoldingsUrl, query = query)

# convert response to a data frame
accountHoldingsData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(accountHoldingsData))

# to get allowances held by the owner/operator
ownerHoldingsData <- accountHoldingsData %>%
  group_by(ownerOperator) %>%
  summarise(totalBlock = sum(totalBlock))

## Example 2

# streaming allowance compliance endpoint url
allowanceComplianceUrl <- paste0(apiUrlBase,"/streaming-services/allowance-compliance?API_KEY=",apiKEY)

# define query parameters
query <- list(programCodeInfo="ARP",
              year=paste0(seq(2010,2021), collapse = '|'))

# API GET request
res = GET(allowanceComplianceUrl, query = query)

# convert response to a data frame
allowanceComplianceData <- fromJSON(rawToChar(res$content))

# print head of dataframe
print(head(allowanceComplianceData))

# print out of compliance facilities for ARP in the last 11 years
print(allowanceComplianceData[!is.na(allowanceComplianceData$excessEmissions),])

####### Account mgmt API #######

## Example 1

# allowance holdings endpoint url
accountHoldingsPageUrl <- paste0(apiUrlBase,"/account-mgmt/allowance-holdings?API_KEY=",apiKEY)

# define query parameters
query <- list(accountType=paste0(c("Facility Account","General Account"), collapse = '|'),
              programCodeInfo="CSOSG3",
              stateCode="OH",
              page=1,
              perPage=10)

# API GET request
res = GET(accountHoldingsPageUrl, query = query)

# There's useful information in the response headers - here's a few
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
accountHoldingsPageData <- fromJSON(rawToChar(res$content))
print(head(accountHoldingsPageData))

## Example 2

# allowance compliance endpoint url
allowanceCompliancePageUrl <- paste0(apiUrlBase,"/account-mgmt/allowance-compliance?API_KEY=",apiKEY)

# define query parameters
query <- list(programCodeInfo="ARP",
              year=paste0(seq(2010,2021), collapse = '|'),
              page=1,
              perPage=10)

# API GET request
res = GET(allowanceCompliancePageUrl, query = query)

# There's useful information in the response headers - here's a few
totalRowsAvailableForQuery <- res$headers$`x-total-count`
print(totalRowsAvailableForQuery)

fieldMapping <- fromJSON(res$headers$`x-field-mappings`)
print(fieldMapping)

# convert response to a data frame
allowanceCompliancePageData <- fromJSON(rawToChar(res$content))
print(head(allowanceCompliancePageData))
