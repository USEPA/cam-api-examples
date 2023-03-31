library(httr)
library(htmltools)
library(jsonlite)
library(data.table)

# The bulk data api allows you to download prepackaged data sets. There are two endpoints for obtaining bulk data.
# The first is the /bulk-files endpoint which returns metadata about files. This metadata includes the path to the
# file.  The second is the /easey/bulk-files endpoint which along with the path, returns the actual file.

# Set your API key here
apiKEY <- "YOUR_API_KEY"

# change this to the date you want to start downloading files from
# all files after this date and time will be downloaded
timeOfLastRun <- strftime("2023-03-01T00:00:00", "%Y-%m-%dT%H:%M:%S")


# API base url
apiUrlBase <- "https://api.epa.gov/easey"

# S3 bucket url base + s3Path (in get request) = the full path to the files
bucketUrlBase <- 'https://api.epa.gov/easey/bulk-files/'

# CAMD Administrative Services API url to bulk data files endpoint
servicesUrl <- paste0(apiUrlBase,"/camd-services/bulk-files?API_KEY=",apiKEY)

# executing get request
res = GET(servicesUrl)
# printing the response error message if the response is not successful
if (res$status_code > 399){
  errorFrame <- fromJSON(rawToChar(res$content))
  stop(paste("Error Code:",errorFrame$error$code,errorFrame$error$message))
}

# converting the content from json format to a data frame
bulkFiles <- fromJSON(rawToChar(res$content))

# cast lastUpdated to strftime
bulkFiles$lastUpdated <- strftime(bulkFiles$lastUpdated , "%Y-%m-%dT%H:%M:%S")

# reduce to files that are older than the timeOfLastRun value
newBulkFiles <- bulkFiles[bulkFiles$lastUpdated > timeOfLastRun,]

####### Hourly State Emissions Files #######

# filter by state hourly emissions files
emissionsFiles <- newBulkFiles[newBulkFiles$metadata$dataType=="Emissions",]
hourlyEmissionsFiles <- emissionsFiles[emissionsFiles$metadata$dataSubType=="Hourly",]
stateHourlyEmissionsFiles <- hourlyEmissionsFiles[!is.na(hourlyEmissionsFiles$metadata$stateCode),]

print(stateHourlyEmissionsFiles)

currentDirectory <- getwd()
dir.create(paste0(currentDirectory,'/data'))

# Read the csvs from source and concatenate them together
stateHourlyEmissionsData <- data.frame()
for (i in 1:nrow(stateHourlyEmissionsFiles)){
  s3Path <- stateHourlyEmissionsFiles[i,c('s3Path')]
  filename <- stateHourlyEmissionsFiles[i,c('filename')]
  print(paste0('Full path to file on S3: ',bucketUrlBase,s3Path))
  GET(paste0(bucketUrlBase,s3Path), write_disk(paste0(currentDirectory,'/data/',filename)))
  #stateHourlyEmissionsData <- rbind(stateHourlyEmissionsData,read.csv(paste0(bucketUrlBase,s3Path)))
}

# print out unique data sub types in the bulk data files
print(unique(bulkFiles$metadata$dataType))

# select Mercury and Air Toxics Emissions (MATS) files
matsFiles = bulkFiles[bulkFiles$metadata$dataType == "Mercury and Air Toxics Emissions (MATS)",]

# print out unique data sub types in the bulk data
print(unique(matsFiles$metadata$dataSubType))

# check if state groupings exist in any of the files
print(na.omit(unique(matsFiles$metadata$stateCode)))

# check if quarterly groupings exist in any of the files
print(na.omit(unique(matsFiles$metadata$quarter)))

