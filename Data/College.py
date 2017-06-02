# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:46:15 2016

@author: v-haharv
"""

import numpy as np
import os
import pandas as pd


all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")

#create list of columns for both dataframes
all_ages_columns = all_ages.columns.tolist()
recent_grads_columns = recent_grads.columns.tolist()

all_majors = recent_grads["Major"].value_counts().index

unique_major_cats = all_ages['Major_category'].value_counts().index

all_ages_major_categories = {}
recent_grads_major_categories ={}

major_categories = list(set(all_ages["Major_category"]))


'''(dataFrame, str-"col_name") --> dict {str: sum of type}'''
def count_totals(data_frame, for_column):
    unique_major_categories=data_frame[for_column].value_counts().index
    counts_dictionary = dict()    
    for i in unique_major_categories:
        major = data_frame[data_frame[for_column]== i]
        total = major["Total"].sum(axis=0)
        counts_dictionary[i] = total
    return counts_dictionary

all_ages_lower_unemp_count = 0
recent_grads_lower_unemp_count = 0 

def compare_counts(dataFrame1, dataFrame2):
    global all_ages_lower_unemp_count
    global recent_grads_lower_unemp_count    
    for i in all_majors:
        major_df1 = dataFrame1[dataFrame1["Major"] == i ]
        major_df2 = dataFrame2[dataFrame2["Major"] == i ]
        df1_unemp_rate = major_df1["Unemployment_rate"].values[0]
        df2_unemp_rate = major_df2["Unemployment_rate"].values[0]
        if df1_unemp_rate > df2_unemp_rate:
            recent_grads_lower_unemp_count += 1
        elif df2_unemp_rate > df1_unemp_rate:
            all_ages_lower_unemp_count += 1

            
        
    

        
        
    