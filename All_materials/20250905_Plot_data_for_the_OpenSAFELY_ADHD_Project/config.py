
# From https://www.england.nhs.uk/nhsidentity/identity-guidelines/colours/
nhs_palette = ["#003087",'#7C2855', "#DA291C", "#ED8B00", "#006747"]

pre_processing = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files',
    'marker':'FAKE_DATA',
}

user_time_plots = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/Table_5_time_from_diagnosis_to_treatment.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_5_time_from_diagnosis_to_treatment.jpeg',
    'watermark':'TEST DATA - NOT REAL',
}

monthly_interval_plot = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/Table_3_percentage_of_people_with_ADHD_then_have_had_meds_in_the_last_6_months.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_3_percentage_of_people_with_ADHD_then_have_had_meds_in_the_last_6_months.jpeg',
    'watermark':'TEST DATA\nNOT REAL',
}

bland_altman_plt = {
    'file_path_emis':'All_materials/20250905_Calculating_ADHD_prevalence_rate_from_EMIS_and_Cegedim_records_using_open_source_data_from_NHS_England/emis_measure.csv',
    'file_path_tpp' : 'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/Table_2_Prevalence_of_ADHD_Diagnosis.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Bland_Altman_plot_between_ADHD_Diagnosis_Prevalence.jpeg',
    'watermark':'TEST DATA - NOT REAL',
    'joining_cols' : ['interval_start','interval_end','sex','age_band'],
    'suffixes' : ('_tpp','_emis'),
}

dia_plots = {
    'file_path':'All_materials/20250905_Calculating_ADHD_prevalence_rate_from_EMIS_and_Cegedim_records_using_open_source_data_from_NHS_England/emis_measure.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_2_Prevalence_of_ADHD_Diagnosis.jpeg',
    'watermark':'EMIS + Cegedim',
    'top_left':{
        'title':'ADHD Diagnosis Prevalence and Counts by Sex',
    },
    'top_right':{
        'title':'ADHD Diagnosis Prevalence and Counts by Age Band (24 and under)',
    },
    'bottom_left':{
        'title':'ADHD Diagnosis Prevalence and Counts by Age Band (25 to 64)',
    },
    'bottom_right':{
        'title':'ADHD Diagnosis Prevalence and Counts by Age Band (65 and over)',
    },
}