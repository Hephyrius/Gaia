# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Khera
"""
import GeneticNetwork as Gen
import numpy as np
import pandas as pd
import copy
import random as r
      

iris = pd.read_csv("testdata/iris.csv")
cols = iris.columns
X = []
Y = []
iris['label'] = iris['label'].astype('category')
iris['label'] = iris['label'].cat.codes

for c, i in iris.iterrows():
    
    row = []
    row.append(i['1'])
    row.append(i['2'])
    row.append(i['3'])
    row.append(i['4'])
    X.append(row)
    
    Y.append(i['label'])



titanicData = pd.read_csv("testdata/titanictrain.csv")
titanicTest = pd.read_csv("testdata/titanictest.csv")
#%%
#if its 1 first then its Xor else its And
data = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
targets = [1,0,0,1,0,1,1,0]        
        
GA = Gen.GeneticNetwork(20, [4,16,3])

GA.Neat(X, Y, 1)

#%%
print(GA.Population[0].predict(X[148]))























