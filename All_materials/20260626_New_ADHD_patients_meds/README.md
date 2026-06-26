> [!WARNING]  
> The following holds code to plot graphs
>
> I’m testing the Microsoft copilot AI to document functions – thus treat the docstring with caution

# New ADHD patients with medication counts

This folder contains a small analysis script that reads an existing OpenSAFELY ADHD data file, summarises the number of new medication records by year and sex, and saves a plot as an SVG image.

## What the code does

The script in [main.py](main.py) performs the following steps:

1. Reads the source CSV from the OpenSAFELY ADHD project data folder.
2. Groups the data by year of medication and sex.
3. Sums the counts for each group.
4. Creates a line chart for female and male records.
5. Saves the resulting figure to [counts_of_new_medication_by_sex.svg](counts_of_new_medication_by_sex.svg).

## Files in this folder

- [main.py](main.py): Python script that generates the plot.
- [counts_of_new_medication_by_sex.svg](counts_of_new_medication_by_sex.svg): Output chart showing the counts by year and sex.

## How to run

From the repository root, run:

```bash
python All_materials/20260626_New_ADHD_patients_meds/main.py
```

## Result

Running the script produces a chart with:

- x-axis: year of medication
- y-axis: count
- series: female and male