from src.fca_web_scrape import fca_scrape
import bs4
import re

FIRM_REF_NUMBER = 'firm_ref_number'
FIRM_FCA_LINK = 'fca_ref'

soup = fca_scrape.get_soup_of_fca_search('Leeds Building society')

ref_table = fca_scrape.get_dict_of_ordering_firm_listings(soup)

selected_link = ref_table.iloc[0][FIRM_FCA_LINK]

#%%

soup_data_for_firm = fca_scrape.get_soup_without_cookie_notice(selected_link)

#%% 

text_analysis = soup_data_for_firm.prettify()

element_list = soup.find_all({'aria-hidden':'ture'})

print([x.get_text() for x in element_list])