# README

> [!IMPORTANT]  
> FAKE DATA

https://github.com/nhs-pycom/coding-club/tree/main

https://github.com/nhs-pycom/

https://digital.nhs.uk/services/artificial-data 

## Housekeeping (5 mins)

## Introduction to Python (15 mins)

### How to read Python script

### How to run Python

### Library

```python
import pandas as pd
import datetime
```

## How to print and access Pandas info (15 mins)

### Print Function

### To access information from Pandas table

#### Columns



##### All the columns in the table

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

list_of_cols = hes_data.columns

print(list_of_cols)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_col = hes_data[['FYEAR', 'PARTYEAR', 'EPIKEY']]

print(selected_col)
```

##### A single column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_col = hes_data[['AEKEY']]

print(selected_col)
```

##### A single row
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_row = hes_data.iloc[3]

print(selected_row)
```
##### A entry for a given row and column
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_entry = hes_data.iloc[3]['ADMIDATE']

print(selected_entry)
```
## Data types in Pandas (15 mins)

### Numbers
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

number_col = hes_data['DISDEST']

print(number_col)
```

### Strings
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

string_col = hes_data['DIAG_4_01']

print(string_col + 'test')

print(string_col * 2)
```
### Dates?
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

date_looking_col = hes_data['ADMIDATE']

date_col = pd.to_datetime(date_looking_col, format="%Y/%m/%d")

print(date_col)
```
## Break + Stoptake + Retro (15 mins)


## Groupings in Pandas (15mins)

### Aggrating over a single column
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_distances = hes_data[['DISDEST']]

mean_distance = selecting_distances.mean()

print(mean_distance)
```

### Aggrating over a value in a column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_each_patient = hes_data[['PSEUDO_HESID','DISDEST']]

grouping_agg_distance = selecting_each_patient.groupby('PSEUDO_HESID').agg(['min','max','mean'])

print(grouping_agg_distance)
```

### Aggrating over a value in multple column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selecting_diag_codes_and_demogr_data = hes_data[['DIAG_4_01','ETHNOS','ELECDUR_CALC']]

grouping_dia_codes = selecting_diag_codes_and_demogr_data.groupby(['DIAG_4_01','ETHNOS']).agg(['mean'])

print(grouping_dia_codes)
```
## Conditional and filterings (15 mins)

### Filtering the strings

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter = hes_data['DIAG_4_01'] == 'D610'

filtered_icd10 = hes_data[binary_filter_letter]

print(filtered_icd10)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter = hes_data['DIAG_4_01'].str.contains('D')

filtered_icd10 = hes_data[binary_filter_letter]

print(filtered_icd10)
```

### Filtering numbers

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_age = hes_data['STARTAGE_CALC'] < 18

filtered_age = hes_data[binary_filter_age]

print(filtered_age)
```

### Filtering Dates

#### Date range
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

date_looking_col = hes_data['ADMIDATE']

#Create a date
selected_date = datetime.datetime(2020, 6, 7)

#Coverting column to a date
hes_data['ADMIDATE'] = pd.to_datetime(date_looking_col, format="%Y/%m/%d")

filter_dates_indicator = hes_data['ADMIDATE'] > selected_date

filtered_dates = hes_data[filter_dates_indicator]

print(filtered_dates)
```

### Multipe conditions

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

binary_filter_letter_D = hes_data['DIAG_4_01'].str.contains('D')

binary_filter_letter_E = hes_data['DIAG_4_01'].str.contains('E')

indicator_either_D_or_E = binary_filter_letter_D | binary_filter_letter_E

filtered_icd10 = hes_data[indicator_either_D_or_E]

print(filtered_icd10)
```

## Stoptake + Take away

## END

## Licence
The documentation and the artificial data files are © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.

