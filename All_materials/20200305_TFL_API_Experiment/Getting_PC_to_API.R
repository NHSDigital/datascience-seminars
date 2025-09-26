library("httr")
library('jsonlite')
library('tidyverse')
library("XML")
library(knitr, quietly = T)

#For the API
username <- 
password <- 

#This is to get the strings
Postcode_preprocess <- function(post_code){
  #This is to remove space
  searchString <- ' '
  replacementString <- ''
  sentenceString <- sub(searchString,replacementString,post_code)
  #This is to covert the lower string
  sentenceString <- tolower(sentenceString)
  return(sentenceString)
}

#This is to get the API link
API_link_maker <- function(ind_hospital_postcode,IMD_postcode){
  starting_link <- 'https://api.tfl.gov.uk/journey/journeyresults/'
  complete_link <- paste(starting_link,IMD_postcode,'/to/',ind_hospital_postcode,sep='')
  return(complete_link)
}

setwd('')

hosp_postcode <- read.csv('London_hospital.csv',stringsAsFactors = FALSE)
dep_IMD <- read.csv('London_IMD_scores_with_PC.csv')

#Getting two post codes together
IMD_postcode <- Postcode_preprocess(as.character(dep_IMD$pcds[100]))
ind_hospital_postcode <- Postcode_preprocess(as.character(hosp_postcode$X9[34]))

print(IMD_postcode)
print(ind_hospital_postcode)

#This is the link for tfl's api
tfl_link <- API_link_maker(ind_hospital_postcode,IMD_postcode)

#The following is taken from the link https://github.com/alex-drake/R-for-Analysts/blob/master/06%20Data%20Wrangling.md

requestUrl <- paste0(tfl_link , "?app_id=", username, "&app_key=", password)

info_in_list_of_list <- fromJSON(requestUrl)

#Need to get thet miniumn travel distance
info_on_travel_times = min(info_in_list_of_list$journeys$duration)


