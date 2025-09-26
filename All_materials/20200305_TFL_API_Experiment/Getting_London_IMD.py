#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is to get the indices of d for london only
"""

import pandas as pd
import numpy as np

#Getting London IMD scores 

london_imd_dataset = pd.read_excel('ID_2019_for_London.xlsx',sheet_name='IMD 2019')
#%% Saving the files

london_imd_dataset.to_csv('London_IMD_scores.csv')
