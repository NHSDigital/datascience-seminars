
library("httr")
library('jsonlite')
library("XML")

username <- 
password <- 

base <- "https://api.tfl.gov.uk/journey/journeyresults/1000266/to/1000013"


call1 <- paste(base)

get_prices <- GET(call1, authenticate(username,password, type = "basic"))

tfl_info <- class(get_prices)

get_prices_text <- content(get_prices, "text")

get_prices_json <- fromJSON(get_prices_text, flatten = TRUE)

df<-data.frame(get_prices_json=unlist(get_prices_json))

get_prices_df <- as.data.frame(get_prices_json,stringsAsFactors = FALSE, is.na = "N")

names(get_prices_json)

get_prices_json$journeyVector

a <- as.data.frame(get_prices_json$fromLocationDisambiguation)
b <- as.data.frame(get_prices_json$toLocationDisambiguation)
c <- as.data.frame((get_prices_json$journeyVector))
d <- as.data.frame((get_prices_json$searchCriteria))
e <- as.data.frame((get_prices_json$recommendedMaxAgeMinutes))
f <- as.data.frame(get_prices_json$viaLocationDisambiguation)
g <- as.data.frame(get_prices_json$`$type`)

tfl1 <- tibble(user = get_prices_json)
names(tfl1$user)
get_prices_json1 <- as.character(get_prices_json)
tfl1 %>% unnest_wider(get_prices_json1)