from src.web_scraping_and_data_wrangling import fos_web_scrap
from src.utils.file_paths import get_config
from datetime import datetime

config = get_config("config.toml") 

#%%
#Step 1 - getting the link
start_date = datetime.strptime(config['web']['start_date'], 
                               '%Y-%m-%d').date()
end_date = datetime.strptime(config['web']['end_date'], 
                               '%Y-%m-%d').date()

url_link_from_function = fos_web_scrap.getting_URL_with_date_range(start_date, end_date)

#%% 
#Step 2 - getting the data

example_of_soup = fos_web_scrap.get_info_as_soup(url_link_from_function)
example_of_soup = example_of_soup.prettify()

complete_list = get_complete_desision_list(url_link_from_function)

#%% Step 3 - getting the tweets

#file_name = saving_the_tweets(complete_list, url_link_from_function)
