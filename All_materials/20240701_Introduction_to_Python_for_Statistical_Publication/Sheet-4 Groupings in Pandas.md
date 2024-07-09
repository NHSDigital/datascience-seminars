# Groupings in Pandas (15mins)

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

### Exercise

In python, you can plot a scatter graph using:

```python
tips = sns.load_dataset("tips") #Loads sample data
sns.scatterplot(data=tips, x="total_bill", y="tip")
```

**Exercise** For each vaule in ``PSEUDO_HESID`` compute the aggregation of the mean ``STARTAGE`` and maximum ``PROVDIST``. Then plot a scatter graph between mean ``STARTAGE`` on the x axis and maximum ``PROVDIST``

**Exercise** Consider the column:
```python
'ETHNOS'.
```
Create a [series from the Pandas Dataframe]( https://www.geeksforgeeks.org/select-a-single-column-of-data-as-a-series-in-pandas/) and [find the frequency counts using the function]( https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html):
```python
value_counts()
```
Then plot a bar chart using functions in [seaborn](https://seaborn.pydata.org/generated/seaborn.barplot.html)

