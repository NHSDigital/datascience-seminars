from src.fca_web_scrape import fca_scrape
import bs4
import re

soup = fca_scrape.get_soup_of_fca_search('Coventry')

ref_number = fca_scrape.get_reference_number(soup)

#Test