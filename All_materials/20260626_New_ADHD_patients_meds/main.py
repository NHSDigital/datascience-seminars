from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

repo_root = Path(__file__).resolve().parents[2]
input_path = repo_root / 'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/open_data/Table 5 - Median time from ADHD diagnosis to medication being prescribed.csv'
output_path = repo_root / 'All_materials/20260626_New_ADHD_patients_meds/counts_of_new_medication_by_sex.svg'

tmp = pd.read_csv(input_path)

sex_trend = tmp.groupby(['Year_of_medication', 'Sex'], as_index=False)['size'].sum()
sex_trend = sex_trend[['Year_of_medication', 'Sex', 'size']]
sex_trend = sex_trend[sex_trend['Sex'].isin(['female', 'male'])]

plt.figure(figsize=(8, 4))
for sex, group in sex_trend.groupby('Sex'):
    plt.plot(group['Year_of_medication'], group['size'], marker='o', label=sex)

plt.xlabel('Counts of new patients with ADHD meds')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Count')
plt.title('Size by Year of Medication and Sex')
plt.legend()
plt.tight_layout()
output_path.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(output_path, format='svg', dpi=300)
plt.close()