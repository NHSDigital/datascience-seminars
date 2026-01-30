
# From https://www.england.nhs.uk/nhsidentity/identity-guidelines/colours/
nhs_palette = ["#12436D",'#28A197', "#801650", "#F46A25", "#3D3D3D","#A285D1"]

pre_processing = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files',
    'marker':'FAKE_DATA',
    'open_data_link':r'https://files.digital.nhs.uk/02/F0E82B/OpenSAFELY%20-%20Additional%20data%20tables.zip',
    'open_data_check_folder':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/open_data',
    'zip_file_name':'open_data.zip',
}

save_plots_config = {
    'file_type':'svg',
    'dpi': 500
}

user_time_plots = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/Table_5_time_from_diagnosis_to_treatment.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_5_time_from_diagnosis_to_treatment.svg',
    'watermark':'TEST DATA - NOT REAL',
    'cut_file_name': 'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Cut_Time_average.svg',
}

monthly_interval_plot = {
    'file_path':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/Table_3_percentage_of_people_with_ADHD_then_have_had_meds_in_the_last_6_months.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_3_percentage_of_people_with_ADHD_then_have_had_meds_in_the_last_6_months.svg',
    'watermark':'TEST DATA\nNOT REAL',
}

bland_altman_plt = {
    'file_path_emis':'All_materials/20250905_ADHD_Prevalence_EMIS_and_Cegedim/emis_measure.csv',
    'file_path_tpp' : '/workspaces/datascience-seminars/All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/source_files/open_data/Table 1 - ADHD prevalence.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Bland_Altman_plot_between_ADHD_Diagnosis_Prevalence.svg',
    'watermark':'TEST DATA - NOT REAL',
    'joining_cols' : ['interval_start','interval_end','sex','age_band'],
    'suffixes' : ('_tpp','_emis'),
}

dia_plots = {
    'file_path':'All_materials/20250905_ADHD_Prevalence_EMIS_and_Cegedim/emis_measure.csv',
    'file_name':'All_materials/20250905_Plot_data_for_the_OpenSAFELY_ADHD_Project/Table_2_Prevalence_of_ADHD_Diagnosis.svg',
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