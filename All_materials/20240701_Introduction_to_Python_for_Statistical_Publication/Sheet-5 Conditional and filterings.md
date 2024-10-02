# Conditional and filterings (15 mins)

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

#Create a date
selected_date = datetime.datetime(2020, 6, 7)

#Coverting column to a date
hes_data['ADMIDATE'] = pd.to_datetime(hes_data['ADMIDATE'], format="%Y/%m/%d")

filter_dates_indicator = hes_data['ADMIDATE'] > selected_date

filtered_dates = hes_data[filter_dates_indicator]

print(filtered_dates)
```

```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

#Coverting column to a date
hes_data['ADMIDATE'] = pd.to_datetime(hes_data['ADMIDATE'], format="%Y/%m/%d")

filter_month_indicator = hes_data['ADMIDATE'].dt.month == 6

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

### Exercise

**Exercise** Add a new column on the dataframe called ``PERSON_STATE`` where each value is either ``Adult``if ``STARTAGE`` is equal or above 18 and ``Child`` is below 18.

**Exercise** Plot a bar chart which list the number of records that in for each month between October to February (inclusive) in ``ADMIDATE``

**Exercise** Find the ``PSEUDO_HESID`` with the most labels with a ``D`` in ``DIAG_4_01``


## Stoptake + Take away
[Having a retro](https://www.atlassian.com/team-playbook/plays/retrospective)

