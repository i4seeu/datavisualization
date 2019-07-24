# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import data from the csv file using pandas
import pandas as pd
data = pd.read_csv('iris.data',names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])