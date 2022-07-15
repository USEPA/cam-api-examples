library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api.epa.gov/easey/dev"
apiKEY <- "YOUR_API_KEY"

# S3 bucket url base + s3Path in get request is the full path to the files
bucketUrlBase <- 'https://api.epa.gov/easey/dev/bulk-files/'

# annual emissions url
servicesUrl <- paste0(apiUrlBase,"/camd-services/bulk-files?API_KEY=",apiKEY)

res = GET(servicesUrl)

bulkFiles <- fromJSON(rawToChar(res$content))

complianceFiles <- bulkFiles[bulkFiles$metadata$dataType=="Compliance",]

ARPComplianceFile <- complianceFiles[complianceFiles$filename == 'compliance-arp.csv',]

ARPCompliaceDF <- read.csv(paste0(bucketUrlBase,ARPComplianceFile$s3Path))
