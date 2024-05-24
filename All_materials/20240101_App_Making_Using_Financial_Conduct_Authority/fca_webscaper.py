from src.fca_web_scrape import fca_scrape
import bs4
import re

FIRM_REF_NUMBER = 'firm_ref_number'
FIRM_FCA_LINK = 'fca_ref'

soup = fca_scrape.get_soup_of_fca_search('Beehive')

ref_table = fca_scrape.get_dict_of_ordering_firm_listings(soup)


#%%

list_of_links  = ref_table
