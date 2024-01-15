from datetime import datetime

from src.utils.file_paths import get_config
from src.web_scraping_and_data_wrangling import fos_web_scrape

config = get_config("config.toml")

#%%
# Step 1 - getting the link
start_date = datetime.strptime(config["web"]["start_date"], "%Y-%m-%d").date()
end_date = datetime.strptime(config["web"]["end_date"], "%Y-%m-%d").date()
search_term = config["web"]["search_term"]

url_link_from_function = fos_web_scrape.getting_URL_with_date_range(
    start_date, end_date, search_term)

#%%
# Step 2 - getting the data

complete_list = fos_web_scrape.get_complete_decision_list(url_link_from_function)

#%% Step 3 - getting the tweets

_, _, summary_table = fos_web_scrape.list_of_summary(complete_list)

#%%

# Collect a sample
output_table = summary_table.copy()
output_table.rename(columns=config["table"], inplace=True)
output_table = output_table[list(config["table"].values())]
mk_table = output_table.to_markdown(index=False).replace("\uf0b7", "")

# Save the file
with open(config["file"]["name"], "w") as text_file:
    text_file.write(mk_table)
    text_file.close()
