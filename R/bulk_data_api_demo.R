library(httr)
library(htmltools)
library(jsonlite)
library(data.table)

# API info
apiUrlBase <- "https://api.epa.gov/easey"
apiKEY <- "YOUR_API_KEY"

# base url to S3 bucket
bucketUrlBase <- 'https://api.epa.gov/easey/bulk-files/'

# CAMD Administrative Services API url to bulk data files endpoint
servicesUrl <- paste0(apiUrlBase,"/camd-services/bulk-files?API_KEY=",apiKEY)

# API GET request
res = GET(servicesUrl)

# convert response to a data frame
bulkFiles <- fromJSON(rawToChar(res$content))
# if you would like all file names and meta information in a csv, uncomment
# the write function below.
#write.csv(bulkFiles, paste0(getwd(),"/available-bulk-files.csv"), row.names = FALSE)

####### Compliance Files #######

# filter by compliance data type and CSAPR programs
complianceFiles <- bulkFiles[bulkFiles$metadata$dataType=="Compliance",]
csaprComplianceFiles <- complianceFiles[complianceFiles$metadata$programCode %like% 'CS',]
print(csaprComplianceFiles)

# Read the csvs from source and concatenate them together
complianceData <- data.frame()
for (s3Path in csaprComplianceFiles$s3Path){
  print(paste0('Full path to file on S3: ',bucketUrlBase,s3Path))
  complianceData <- rbind(complianceData,read.csv(paste0(bucketUrlBase,s3Path)))
}

####### Emission Files #######

# reduce down to get the first two quarter files of daily emissions for 2020
emissionFiles <- bulkFiles[bulkFiles$metadata$dataType=="Emissions",]
dailyEmissionFiles <- emissionFiles[emissionFiles$metadata$dataSubType=="Daily",]
dailyttEmissionFiles <- dailyEmissionFiles[dailyEmissionFiles$metadata$year=="2020",]
dailyttQEmissionFiles <- dailyttEmissionFiles[dailyttEmissionFiles$metadata$quarter %in% c(1,2),]
print(dailyttQEmissionFiles)

# Read the csvs from source and concatenate them together
emissionData <- data.frame()
for (s3Path in dailyttQEmissionFiles$s3Path){
  print(paste0('Full path to file on S3: ',bucketUrlBase,s3Path))
  emissionData <- rbind(emissionData,read.csv(paste0(bucketUrlBase,s3Path)))
}

####### XML Files #######

library(utils)

# reduce down to get the XML files for Alabama
xmlFiles <- bulkFiles[bulkFiles$metadata$dataType=="XML",]
mpXmlEdrFiles <- xmlFiles[xmlFiles$metadata$dataSubType=="Monitoring Plan",]
print(mpXmlEdrFiles)

# get Alabama XML files
alabamaXmlFiles <- mpXmlEdrFiles[mpXmlEdrFiles$metadata$stateCode =="AL",]

# make directory for XML files
currentDirectory <- getwd()
alabamaDirPath <- paste0(currentDirectory,'/AlabamaXML')
dir.create(alabamaDirPath)

# Download XML files and place them in alabamaDirPath directory
for (i in 1:nrow(alabamaXmlFiles)){
  s3Path <- alabamaXmlFiles$s3Path[i]
  filename <- alabamaXmlFiles$filename[i]
  print(paste0('Full path to file on S3: ',bucketUrlBase,s3Path))
  zipFile <- file.path(alabamaDirPath,filename)
  download.file(paste0(bucketUrlBase,s3Path),zipFile)
  unzip(zipFile, exdir=alabamaDirPath)
}





