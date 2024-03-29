# Web Scraping Complaints from the Financial Ombudsman Service

**Kenneth Quan**

TODO: Add downgit link

> [!WARNING]  
> This repository will contain detailed discussions of victims of bank fraud.
>
> There may be references to mental health problems, self-harm, abuse and suicide.
>
> Samaritans suicide helpline: [116-123](tel:116123)
>
> Financial Help: [https://www.citizensadvice.org.uk/](https://www.citizensadvice.org.uk/) <br>
> Debt Advice: [https://www.stepchange.org/](https://www.stepchange.org/) <br>
> Do not use search engines. Go directly via the links.

## Introduction

This repo is designed as training material on the web scraping, data wrangling (also known as [munging](https://en.wikipedia.org/wiki/Data_wrangling)) and text analysis of open score complaints data from the [Financial Ombudsman Service]( https://www.financial-ombudsman.org.uk/).
The work is NOT endorsed by the Financial Ombudsman Service.

## How to use the code

The main code is found in `create_output.py`. The script contains the following steps.

### Constructing the URL link

The construction of the URL link is made using the function:

```python
url_link_from_function = fos_web_scrape.getting_URL_with_date_range(start_date, end_date, search_term)
```

The inputs of the function are the date range when the complaints were made and the search term use to find the relevant complaints. The parameters can be found in the `config.toml` file.

### Web scraping

The web scraping is performed using the function:

```python
complete_list = fos_web_scrape.get_complete_decision_list(url_link_from_function)
```

There are hardcoded parameters to extract the relevant html data from the webpage.

### Wrangling and Analysis

The wrangling and analysis are performed using:

```python
_ , _, summary_table = fos_web_scrape.list_of_summary(complete_list)
```

The function takes all relevant data from metadata in the html and text from the PDF to a Pandas table.

### Output

The resulting output can be found in `table_of_complaints.md`.

For brevity, the main PDF text has been removed before publishing.

## Example Output

The following is example of a table outputted in by the `create_output.py` script. The columns mean the following:

- Ref – Unique compliant reference
- Date – Date of complaint
- Bank – Financial institutions against which the complaint was made
- Scale of Lost – The order of magnitude of the largest of sum of money mentioned in the complaint. For example, if a complaint mentions transactions of £19, £123, £1999 the output shows the order of magnitude of the highest transaction – in this case it will be 10^3.
- Outcome – If the complaint was upheld
- CRM – Did the complaint mention CRM ([Contingent Reimbursement Model Code]( https://www.lendingstandardsboard.org.uk/crm-code/))
- Sample – A sample of the complaint from the main body of text

| Ref         | Date                | Bank                                        | Scale of Lost   | Outcome   | CRM   | Sample                                                                                                                                                                                                                                                                                                                                                                                                           |
|:------------|:--------------------|:--------------------------------------------|:----------------|:----------|:------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DRN-4009518 | 2023-06-01 00:00:00 | Lloyds Bank PLC                             | 10^5            | Notupheld | False | omplaint . I know disappointing , I  explain . Was Mr D victim scam ? It dispute Mr D victim scam  initially persuaded invest dating app , introduced third parties applied pressure Mr D part money order access supposed profits . The scammers cut contact Mr D would part money . Did Mr D authorise payments ? In line Payment Services Regulations 2017 ( PSRs ) , Mr D  liable payments  authorise ,  |
| DRN-4076920 | 2023-06-02 00:00:00 | Monzo Bank Ltd                              | 10^4            | Notupheld | False | 0 , Ms R contact Monzo increase payment limit . When Monzo asked needed , said pay money account paid . While Ms R paying funds directly cryptocurrency accounts , transferred scammer  trading platform . And ultimate reason behind needing increase payment limit . But  mention payments investing go detail . I  mindful Monzo  probe Ms R explanation . But reviewing responses ,  persuade , quest |
| DRN-4161466 | 2023-06-02 00:00:00 | Lloyds Bank PLC                             | 10^6            | Upheld    | False | . Although payment made new payee , considering relatively low value payment I  think  unreasonable Lloyds concerns . It would reasonable say Lloyds step prevent customers making relatively low payments every time tried pay new business . Mr E made second payment 20 July 2020 branch £12,000 . Lloyds provided notes system show second payment £12,000 required manager  approval . The £12,000 payme |
| DRN-4158966 | 2023-06-01 00:00:00 | Monzo Bank Ltd                              | 10^4            | Notupheld | False | crime , might liable losses incurred customer result . However , duty  extend protecting customers poor investment choices . Mr C says scammed GF Markets . And events Mr C describes could attributed scam . But I  mindful Mr C met Mr S legitimate investment business . It would appear must moved  typical career paths move legitimate investment business scamming customers . I also  able find ind  |
| DRN-4165462 | 2023-06-01 00:00:00 | ClearBank Limited                           | 10^2            | Notupheld | True  | Our investigation far J brought complaint us . Our investigator said ClearBank refund payments fifth one onwards . This investigator thought pattern payments made day question unusual way J operated account months . He said ClearBank  contacted J discuss payment five . If , scam would likely uncovered payments would  stopped . The investigator also felt ClearBank done could recover J  funds de  |
| DRN-4164863 | 2023-06-01 00:00:00 | Monzo Bank Ltd                              | 10^3            | Upheld    | True  | mer made payment consequence actions fraudster , may sometimes fair reasonable bank reimburse customer even though authorised payment . Monzo  signatory Lending Standards Boards Contingent Reimbursement Model ( CRM code ) said committed applying principles set . This code requires firms reimburse customers victim authorised push payment scams , like one Ms C fell victim , limited number circumsta |
| DRN-4162779 | 2023-06-02 00:00:00 | Barclays Bank UK PLC                        | 10^4            | Notupheld | False | cantly lower value I would expected trigger Barclays  fraud prevention systems . On 29 June 2021 Barclays conversation Mr J payment making . I listened call . The Barclays representative explained calling £22,500 payment Mr J attempting make . He checked Mr J making payment made type investment . Mr J confirmed making payment account Kraken made type investment . Mr J also confirmed may making si |
