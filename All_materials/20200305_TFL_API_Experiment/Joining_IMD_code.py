#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is to join the IMD scores with post code or long and latt
"""
#%% Getting the packages

import pandas as pd

#%% Getting the data

IMD_data_london = pd.read_csv('London_IMD_scores.csv')
Postcode_finder = pd.read_csv('Postcode_to_Output_Area_to_Lower_Layer_Super_Output_Area_to_Middle_Layer_Super_Output_Area_to_Local_Authority_District_February_2018_Lookup_in_the_UK.csv')
Postcode_finder = Postcode_finder.drop_duplicates(subset = 'lsoa11cd')

#%% Joing the data

IMD_data_london = IMD_data_london.set_index('LSOA code (2011)').join(Postcode_finder.set_index('lsoa11cd'))

#This is to save the post codes
IMD_data_london.to_csv('London_IMD_scores_with_PC.csv')
