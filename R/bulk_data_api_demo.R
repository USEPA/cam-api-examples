library(httr)
library(htmltools)
library(jsonlite)

# API info
apiUrlBase <- "https://api.epa.gov/easey/dev"
apiKEY <- "B9jNE2eT6xiWOANh0jjeHcBKbZvyD7P3gIgARghb"

# base to S3 bucket
bucketUrlBase <- 'https://api.epa.gov/easey/dev/bulk-files/'

# bulk data files url
servicesUrl <- paste0(apiUrlBase,"/camd-services/bulk-files?API_KEY=",apiKEY)

# API GET request
res = GET(servicesUrl)

# convert response to a data frame
bulkFiles <- fromJSON(rawToChar(res$content))

# filter by compliance data type
complianceFiles <- bulkFiles[bulkFiles$metadata$dataType=="Compliance",]

# filter to the ARP compliance file (only one exists)
ARPComplianceFile <- complianceFiles[complianceFiles$filename == 'compliance-arp.csv',]

# Read the csv from source
ARPCompliaceDF <- read.csv(paste0(bucketUrlBase,ARPComplianceFile$s3Path))
