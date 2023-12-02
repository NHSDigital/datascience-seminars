from src.web_scraping_and_data_wrangling import fos_web_scrap
from src.utils.file_paths import get_config
from datetime import datetime
import re

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

complete_list = fos_web_scrap.get_complete_desision_list(url_link_from_function)

#%% Step 3 - getting the tweets

_ , _, summary_table = fos_web_scrap.list_of_summary(complete_list)

#%% 

output_table = summary_table.copy()
output_table.rename(columns=config['table'],inplace=True)
output_table = output_table[list(config['table'].values())]

#Collect a sample
output_table = output_table.iloc[:9]
mk_table = output_table.to_markdown().replace('\uf0b7', '')
mk_table = re.sub(' +', ' ', mk_table)

#Save the file
with open(config['file']['name'], "w") as text_file:
    text_file.write(mk_table)
    text_file.close()