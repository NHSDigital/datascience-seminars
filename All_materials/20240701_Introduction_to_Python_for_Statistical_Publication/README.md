# README

https://github.com/nhs-pycom/coding-club/tree/main

https://github.com/nhs-pycom/

https://digital.nhs.uk/services/artificial-data 

## Housekeeping (5 mins)

## Introduction to Python (15 mins)

### How to read Python script

### How to run Python

### Library

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

##### A single column

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

selected_col = hes_data['AEKEY']

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

## Conditional and filterings (15 mins)

## Stoptake + Take away

## END

## Licence
The documentation and the artificial data files are © Crown copyright and available under the terms of the [Open Government 3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) licence.
