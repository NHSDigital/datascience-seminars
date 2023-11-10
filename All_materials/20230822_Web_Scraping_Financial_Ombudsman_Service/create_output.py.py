import pandas as pd
from nltk.corpus import stopwords
import bs4
import requests
from io import BytesIO
import PyPDF2
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import re
import string
import datetime
import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
all_stopwords = stopwords.words('english')
stemmer = SnowballStemmer("english")
from src.web_scraping_and_data_wrangling import fos_web_scrap

#Step 1 - getting the link
start_date = datetime.date(2023, 3, 1)
end_date = datetime.date(2023, 3, 2)

url_link_from_function = fos_web_scrap.getting_URL_with_date_range(start_date, end_date)

#%% 
#Step 2 - getting the data

example_of_soup = get_info_as_soup(url_link_from_function)
example_of_soup = example_of_soup.prettify()

complete_list = get_complete_desision_list(url_link_from_function)

#%% Step 3 - getting the tweets

#file_name = saving_the_tweets(complete_list, url_link_from_function)
