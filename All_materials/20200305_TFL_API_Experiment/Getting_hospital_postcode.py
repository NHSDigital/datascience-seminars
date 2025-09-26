# -*- coding: utf-8 -*-
"""
This just get thet data
"""
import pandas as pd
import numpy as np


#%% Getting the files

tursts_data = pd.read_csv('etrust.csv',header=None)

sites_in_london = tursts_data[tursts_data[7]=='LONDON'].copy()

#Need to get each of the hospital
hospital_entires = pd.DataFrame([])


for index_entry in range(sites_in_london.shape[0]):
    
    each_entry = sites_in_london.iloc[index_entry]
    
    if 'HOSPITAL' in each_entry[1]:
        
        #Adding to the data
        hospital_entires = hospital_entires.append(each_entry,ignore_index=True)
        
#%% Need to get it into 

list_of_finalised_data = hospital_entires.drop_duplicates(
        subset = 9,keep = 'first')

#Finally need to reset index
list_of_finalised_data = list_of_finalised_data.reset_index(drop=True)

#%% Need to have unique types

list_of_finalised_data.to_csv('London_hospital.csv')
