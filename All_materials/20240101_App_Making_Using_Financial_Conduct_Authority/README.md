# Streamlit to Signpost Genuine Financial Institutions via Financial Conduct Authority 

> [!IMPORTANT]  
> If FCA block the web scaping - this becomes pointless
>
> The project is incomplete

> [!WARNING]  
> I’m testing the Microsoft copilot AI to document functions – thus treat the docstring and README with caution


This project provides tools to scrape and extract information from the [Financial Conduct Authority (FCA) Register](https://register.fca.org.uk). It includes Python scripts for automated data collection and a simple Streamlit app for user interaction.

---

## **Project Structure**

- **`fca_scrape.py`**  
  Core scraping logic using **Selenium** and **BeautifulSoup**. Functions include:
  - `get_soup_of_fca_search(search_term)`: Fetch FCA search results page for a given institution.
  - `get_soup_without_cookie_notice(url_link)`: Load FCA profile page without cookie notice.
  - `get_ref_links_from_soup(soup)`: Extract firm reference links.
  - `get_reference_number(soup)`: Extract firm reference numbers.
  - `get_dict_of_ordering_firm_listings(soup)`: Return a DataFrame of firm reference numbers and links.
  - `get_name_from_fca_profile(soup)`, `get_phone_number_from_fca_profile(soup)`, `get_website_from_fca_profile(soup)`: Extract firm details.
  - `get_general_info_for_a_profile(url_link)`: Get name, phone, and website from a firm profile.
  - `get_general_info_for_a_profile_via_soup(soup)`: Same as above but from an existing soup object.

- **`fca_webscaper.py`**  
  Example usage of the scraper functions:
  - Searches for a firm (e.g., *Leeds Building Society*).
  - Retrieves the first firm link and extracts general info.
  - Demonstrates scraping via URL and via soup.

- **`app_maker.py`**  
  A **Streamlit** app for interactive scraping:
  - User inputs an institution name.
  - Displays the first firm's name, website, and phone number.

---

## **Requirements**

- Python 3.8+
- **Libraries**:
  - `selenium`
  - `beautifulsoup4`
  - `pandas`
  - `streamlit`
  - `re`
  - `urllib`

- **Browser Driver**:
  - Firefox with **GeckoDriver** (ensure it’s installed and in PATH).

---

## **Usage**

### **Run Streamlit App**
```bash
streamlit run app_maker.py
```

### **Run Example Script**
```bash
python fca_webscaper.py
```

---

## **Features**
✔ Scrapes FCA register for firm details  
✔ Handles cookie notices automatically  
✔ Outputs firm name, phone number, and website  
✔ Interactive UI via Streamlit  

---

## **Notes**
- FCA pages may change; selectors might need updates.
- Ensure Firefox and GeckoDriver are properly configured.
