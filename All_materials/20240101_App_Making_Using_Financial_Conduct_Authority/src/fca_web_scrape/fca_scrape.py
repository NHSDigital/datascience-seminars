from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import bs4
import time
import urllib.parse

def get_soup_of_fca_search(search_term):
    
    #Need to convert to URL
    search_term_url_percentage = urllib.parse.quote(search_term, safe='')
    
    driver = webdriver.Firefox()
    
    driver.get('https://register.fca.org.uk/s/search?q=' + 
               search_term_url_percentage +
               '&type=Companies')
    
    time.sleep(10)
    
    element = driver.find_element(By.XPATH, '//button[@value="no"]')
    driver.execute_script("arguments[0].click();", element)
    
    html_data = driver.page_source
    
    driver.close()
    
    soup = bs4.BeautifulSoup(html_data,'html.parser')
    
    return soup