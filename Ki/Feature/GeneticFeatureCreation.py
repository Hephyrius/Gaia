# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 09:40:23 2018

@author: Khera

genetic feature creation uses GA to create features using strings of mathematical operations
"""

import pandas as pd
import numpy as np
import random as r

#remove warnings given by np
import warnings
warnings.filterwarnings("ignore")

#sk learn is being used as a quick and dirty way of getting feature importances
#as this is at the core of the GA

import sklearn as sk

class GeneticFeatureCreation():
    
    Data = []
    ColumNames = []
    Population = []
    PopulationSize = 0
    NumOperations = 0
    FeaturesToAvoid = []
    BestFeatures = []
    
    def __init__(self, _Data, _PopulationSize=100, _NumOperations=10, _FeaturesAvoid=[]):
        
        self.Data = _Data.copy()
        self.PopulationSize = _PopulationSize
        self.NumOperations = _NumOperations
        self.Population = []
        self.ColumNames = []
        self.BestFeature = []
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
                operations.append(r.randint(0,6))
                math.append(r.randint(0,3))
                features.append(r.randint(0, len(self.ColumNames)-1))
            
            IndividualData = {"Operations":operations, "FeaturesUsed":features, "Math":math, "Output":[], "Fitness":0}
            self.Population.append(IndividualData)
   
    #iterate over all rows and execute the calculation function. adding the results to a table for later use.
    def CalculateResults(self):
        features = pd.DataFrame()
        for i in range(len(self.Population)):
            
            features["NewFeature"+str(i)] = self.CalculateFeature(self.Population[i])
            #print(self.Population[i])
            
        return features
    
    #use the individuals 'genes' to generate a feature for testing
    def CalculateFeature(self, row):
        row['output'] = 0
        out = 0
        for i in range(self.NumOperations):
            
            #pull the rows data.
            Res = self.Data[self.ColumNames[row['FeaturesUsed'][i]]].copy()
            Res = np.asarray(Res)
            
            #sqrt the feature column
            if row['Operations'][i] == 0:
                Res = np.sqrt(Res)
            
            #exponential
            elif row['Operations'][i] == 1:
                Res = np.exp(Res)
        
            #cosine
            elif row['Operations'][i] == 2:
                Res = np.cos(Res)
                
            #sine
            elif row['Operations'][i] == 3:
                Res = np.sin(Res)
                
            #log
            elif row['Operations'][i] == 4:
                Res = np.log(Res)
            
            #apply the result to the outputs
            
            #add
            if row['Math'][i] == 0:
                out += Res
            
            #sub
            elif row['Math'][i] == 1:
                out -= Res
        
            #div
            elif row['Math'][i] == 2:
                out /= Res
                
            #mul
            elif row['Math'][i] == 3:
                out *= Res
                
        #out = out/np.max(out)
        row['output'] = out
        return out
    
    def EvaluateFeatureSet(self, features, targets):
        
        #add in the original data for future reference
        for i in self.ColumNames:
            features['orig_'+i] = self.Data[i]
        
        #get the names as this helps for debugging later on
        names = features.columns
        
        #fill potential nan values
        features= features.replace([np.inf, -np.inf], np.nan)
        features = features.fillna(0)
        
        #use random forest as a way of assessing how useful a new feature is
        from sklearn.ensemble import RandomForestClassifier
        clf = RandomForestClassifier(n_jobs=256, random_state=0)
        clf.fit(features, targets)
        
        #now get the importance of the features
        importance = clf.feature_importances_  
        
        #generate a table for the results, and return the table
        res = pd.DataFrame()
        res['names'] = names
        res['importance'] = importance
        
        mean = 0
        
        #use the importance as fitness values for individuals
        for i, row in res.iterrows():
            if "NewFeature" in row['names']:
                if row['importance'] > 0.1:
                    if self.Population[i] not in self.BestFeatures:
                        print("Found strong feature, adding to bests")
                        self.BestFeatures.append(self.Population[i])
                    
                self.Population[i]['Fitness'] = row['importance']
                mean += row['importance']
        #print("best fitness is: " + str(np.max(importance)))
        print("Pop fitness is: " + str(mean))
        return res
    
    #evolve new features 
    def EvolveFeatures(self, targets, generations=100):
        
        for i in range(generations):
            f = self.CalculateResults()
            r = gen.EvaluateFeatureSet(f, targets)
            self.SortByFitness()
            
    #create a new population
    def ConstructNewPopulation(self):
        
        NewPopulation = []
        for i in range(len(self.Population)):
            
            #preserve some solutions -- elitism 
            if i <= 3:
                NewPopulation.append(self.Population[i])
            
            #else do some crossover/mutations
            else:
                ran = r.random()
                
                #mutate only
                if ran < 0.3:
                    index = r.randint(0,len(self.Population)/5)
                    Newindiv = self.Mutate(self.Population[index])
                    NewPopulation.append(Newindiv)
                
                #crossover only
                elif ran < 0.85:
                    index = r.randint(0,len(self.Population)/5)
                    index2 = r.randint(0,len(self.Population)/5)
                    Newindiv = self.CrossOver(self.Population[index], self.Population[index2])
                    NewPopulation.append(Newindiv)
                    
                #mutate and cross over
                else:
                    index = r.randint(0,len(self.Population)/5)
                    index2 = r.randint(0,len(self.Population)/5)
                    Newindiv = self.CrossOver(self.Population[index], self.Population[index2])
                    Newindiv = self.Mutate(Newindiv)
                    NewPopulation.append(Newindiv)
                    
        self.Population = NewPopulation
    
    #mutate a given individual in order to generate a new one
    def Mutate(self, indiv):
        
        operations = indiv['Operations']
        features = indiv['FeaturesUsed']
        math = indiv['Math']
        
        for i in range(self.NumOperations):
            
            r1 = r.random()
            r2 = r.random()
            r3 = r.random()
            
            if r1 <= 0.05:
                operations[i] = (r.randint(0,6))
                
            if r2 <= 0.05:
                math[i] = (r.randint(0,3))
                
            if r3 <= 0.05:
                features[i] = (r.randint(0, len(self.ColumNames)-1))
        
        IndividualData = {"Operations":operations, "FeaturesUsed":features, "Math":math, "Output":[], "Fitness":0}
        return IndividualData
    
    #produce an offspring from parents
    def CrossOver(self, indiv, indiv1):
        
        operations = []
        features = []
        math = []
        
        for i in range((self.NumOperations)):
            
            r1 = r.random()
            r2 = r.random()
            r3 = r.random()
            
            if r1 <= 0.7:
                operations.append(indiv['Operations'][i])
            else:
                operations.append(indiv1['Operations'][i])
                
            if r2 <= 0.7:
                features.append(indiv['FeaturesUsed'][i])
            else:
                features.append(indiv1['FeaturesUsed'][i])
                
            if r3 <= 0.7:
                math.append(indiv['Math'][i])
            else:
                math.append(indiv1['Math'][i])
        
        IndividualData = {"Operations":operations, "FeaturesUsed":features, "Math":math, "Output":[], "Fitness":0}
        return IndividualData
    #sort results based on fitness
    def SortByFitness(self):
        
        #sort the population in fitness order USING BUBBLE SORT
        for i in range(len(self.Population)):
            
            for j in range(i+1, len(self.Population)):
                
                if self.Population[i]['Fitness'] < self.Population[j]['Fitness']:
                    individual = self.Population[i]
                    self.Population[i] = self.Population[j]
                    self.Population[j] = individual
                    self.ConstructNewPopulation()
        
#testing - data prep
datas = pd.read_csv('../Examples/TestData/iris.csv')
label = datas['label']
datas = datas.drop(['label'], axis=1)

#prepare the model
gen = GeneticFeatureCreation(datas)
print(gen.Population[0]['FeaturesUsed'])
gen.EvolveFeatures(label)


