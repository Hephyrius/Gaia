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

#Xor and And Tests:
##if its 1 first then its Xor else its And
data = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
targets = [1,0,0,1,0,1,1,0]        

#Iris Data:
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


#Titanic Tests
titanicData = pd.read_csv("testdata/titanictrain.csv")
titanicTest = pd.read_csv("testdata/titanictest.csv")

labs = titanicData['Survived']
titanicData = titanicData.drop(['Survived'], axis=1)
fulldata = pd.concat([titanicData, titanicTest])
ind = len(titanicData)

Cols = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
    
for i in fulldata.columns:
    if i in Cols:
        fulldata[i] = fulldata[i].astype('category')
        fulldata[i] = fulldata[i].cat.codes

titanicData = fulldata[:ind]
titanicTest = fulldata[ind:]

TitanicY = []
for i in labs:
    TitanicY.append(i)

TitanicX = []
for c, i in titanicData.iterrows():
    
    row = []
    for j in titanicData.columns:
        row.append(i[j])
    TitanicX.append(row)

TitanicTestX = []
for c, i in titanicTest.iterrows():
    
    row = []
    for j in titanicData.columns:
        row.append(i[j])
    TitanicTestX.append(row)

#%%
        
GA = Gen.GeneticNetwork(20, [11,44,2])
GA.Neat(TitanicX, TitanicY, 100)

























