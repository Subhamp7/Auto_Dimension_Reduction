# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:40:07 2020

@author: subham
"""

#importing libraries
import pandas as pd
import numpy as np

def corr_max(dataset,corr_value=0.8):
  #creating the correlation matrix,Pearson by default and abs() to convert negative correlation to positive.
  dataset_corr = dataset.corr().abs()

  #generating a diagonal matrix of boolean with same shape as for the correlated matrix and starting column k=1.
  ones_matrix = np.triu(np.ones(dataset_corr.shape), k=1).astype(np.bool)
                      
  #selecting the values from dataset passing the matrix
  dataset_corr = dataset_corr.where(ones_matrix)

  #selecting those columns with corr value more than 0.85
  column_drop = [index for index in dataset_corr.columns if any(dataset_corr[index] > corr_value)]

  #dropping columns from dataset
  dataset=dataset.drop(column_drop, axis=1)

  return dataset

#testing the corr_max function
dataset_1= pd.read_csv('https://query.data.world/s/ozjojlneoblmv5pfwevrjhx67dbscl')
print("Shape before the function {} \nShape after  the function {}".format(dataset_1.shape,corr_max(dataset_1,corr_value=0.7).shape))
