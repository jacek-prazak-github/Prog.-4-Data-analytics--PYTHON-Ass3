#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on a sunny and rainy day

@author: Jacek Prazak
@id: R00193791
@Cohort: SD3B
"""
import pandas as pd


df = pd.read_csv("humanDetails.csv", encoding="ISO-8859-1")

"""
1. Task1: For each known county use Work-class and Age to predict Income with the following
setting:
(a) Any record associated with an unknown cell in work-class should be removed from the
dataset.
(b) Some values in Age columns are represented as decade, e.g., 20s or 30s. You are required
to clean these values by removing the s and convert it into an integer value.
(c) Income is either less or equal than 50k or greater than 50k.
(d) Cross validation using 5 folds and 20% test size.
1
For each country run decision tree classifier and try different values for the depth of the tree.
Pick the depth that produces highest accuracy for test set. And finally pick those countries
that their process of learning still suggest overfitting and visualize them using appropriate
visualization technique to display the gap between training and test. In this task overfitting
occurs if the gap between training and test is more than 20%.
Interpret the results.
"""

def Task1():
    # PRINT ALL COLUMNS NAMES
    #print(df.columns.tolist())
    # Rename ' workclass' column to 'workclass'
    #df.rename(columns={' workclass': "workclass"}, inplace=True)
    # Print unique values in data series (column workclass) to check for potential typos
    #print(df['workclass'].unique())
    # Delete rows with ' ?' unknown cell
    #df.drop(df[df['workclass'] == ' ?'].index, inplace = True)
    #print(df['native-country'].unique())

    # Print unique values in data series (column ages) to check for potential typos
    #print(df['age'].unique())
    # Rename values in age column which ends with s
    #df.loc[df['age'].str.endswith('s'), 'age'] = df['age'].str[:-1]
    # Print unique values in data series (column ages) to view changes
    #print(df['age'].unique())
    #print(df['age'].values)
    #df['age'].replace({'20s' : 20, '40s' : 40, '90s' : 90, })


    #Veryfing data in the Income column for potential typos, invalid values
    print(df['Income'].unique())




    #print(df)
    #print(df['workclass'].keys)







Task1()















def Task2():
    print('task2')


def Task3():
    print('task3')
