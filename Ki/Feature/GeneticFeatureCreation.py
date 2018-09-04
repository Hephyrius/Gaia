# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:40:23 2018

@author: Khera

genetic feature creation uses GA to create features using strings of mathematical operations
"""

import pandas as pd
import numpy as np
import random as r

class GeneticFeatureCreation():
    
    Data = []
    ColumNames = []
    Population = []
    PopulationSize = 0
    NumOperations = 0
    FeaturesToAvoid = []
    
    def __init__(self, _Data, _PopulationSize=100, _NumOperations=6, _FeaturesAvoid=[]):
        
        self.Data = _Data
        self.PopulationSize = _PopulationSize
        self.NumOperations = _NumOperations
        self.Population = []
        self.ColumNames = []
        self.FeaturesToAvoid = _FeaturesAvoid
        
        #generate column names by removing any avoided columns from the range of features
        self.GetColumnNames()
        
        #initialise the first generation
        self.InitPopulation()
        
    def GetColumnNames(self):
        
        for i in self.Data.columns:
            if i not in self.FeaturesToAvoid:
                self.ColumNames.append(i)
    
    #generate sequences of operations
    def InitPopulation(self):
        for i in range(self.PopulationSize):
            operations = []
            features = []
            math = []
            for j in range(self.NumOperations):
                operations.append(r.randint(0,5))
                math.append(r.randint(0,3))
                features.append(r.randint(0, len(self.ColumNames)-1))
            
            IndividualData = {"Operations":operations, "FeaturesUsed":features, "Math":math, "Output":[], "Fitness":0}
            self.Population.append(IndividualData)
                
    #
#testing 
datas = pd.read_csv('../Examples/TestData/iris.csv')

gen = GeneticFeatureCreation(datas)

print(gen.Population[0]['FeaturesUsed'])



