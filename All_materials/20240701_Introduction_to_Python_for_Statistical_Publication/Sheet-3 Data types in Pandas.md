# Data Types in Pandas (15 mins)

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
### Dates
```python
hes_data = pd.read_csv('artificial_hes_apc_2021.csv')

date_looking_col = hes_data['ADMIDATE']

date_col = pd.to_datetime(date_looking_col, format="%Y/%m/%d")

print(date_col)
```

### Exercise

In python, you can generate an if statement for example:

```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
```
>[!CAUTION]
>The spaces and colon are important

**Exercise** Generate a loop to print each value in the column:
```python
'DIAG_COUNT'
```
is fewer than 3

**Exercise** Generate a loop to print each value in the column:
```python
'DIAG_4_01'
```
where the [first letter is](https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python) ``A``


**Exercise** Generate a loop to print each value in the column:
```python
'ADMIDATE'
```
where the [date is in on a Friday]( https://pandas.pydata.org/docs/user_guide/timeseries.html)
