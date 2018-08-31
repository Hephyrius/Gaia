# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 22:35:58 2018

@author: Khera

The Markov model builds up a raw frequency based 
picture of relationships between members of a sequence
and then uses this as a powerful method of predicting future elements of a sequence
"""
import numpy as np
import pandas as pd

class MarkovModel():
    
    #class variables
    FrequencyTable = pd.DataFrame()
    CountTable = pd.DataFrame()
    
    #
    def __init__(self):
        
        self.CountTable = pd.DataFrame()
        self.FrequencyTable = pd.DataFrame()
    
    #the fit function takes a 1d array as a sequence and uses it to create the markov models relationships
    def fit(self, sequence):
    
        print("fitting")
        lower = self.toLower(sequence)
        uniques = self.uniques(lower)
        self.generateSequenceStats(lower, uniques)
        self.generateProbailities(lower, uniques)
    
    #predict the next value given a current value
    def Predict(self, x):
        for index , row in self.FrequencyTable.iterrows():
            #print(row['Probabilities Followed On'])
            if row['Value'] == x:
                n = np.asarray(row['Probabilities Followed On'])
                v = np.asarray(row['FollowingValue'])
                return n, v
    
    #find the unique values in a sequence
    def uniques(self, sequence):
        
        uniqueValues = []
        for i in seq:
            if i not in uniqueValues:
                uniqueValues.append(i)
        return uniqueValues
        
        
    def toLower(self, sequence):
        return sequence.lower()
    
    #calculate frequency table counts
    def generateSequenceStats(self, sequence, uniques):
        
        Columns = {'Input','Raw Value', 'Related Value', 'Frequency', 'Count'}
        CountTab = pd.DataFrame(columns=Columns)
            
        for value in range(len(uniques)):
            count = 0
            following = []
            values = []
            
            for nextvalue in range(len(uniques)):
                following.append(0)
                values.append(uniques[nextvalue])
            
            for i in range(0, len(sequence)-1):
                
                if sequence[i] == uniques[value]:
                    count = count+1
                    
                for nextvalue in range(len(uniques)-1):
                    
                    if uniques[nextvalue] == sequence[i+1]:
                        following[nextvalue] = following[nextvalue]+1
        
            result=pd.Series([uniques[value], uniques, values, following, count], index=['Input','Raw Value', 'Related Value', 'Frequency', 'Count'])
            CountTab = CountTab.append(result, ignore_index=True)
        
        self.CountTable = CountTab
    
    #create probability table
    def generateProbailities(self, sequence, uniques):
        
        Columns = {'Value', 'FollowingValue', 'Probabilities Followed On'}
        Probability = pd.DataFrame(columns=Columns)
        
        for index , row in self.CountTable.iterrows():
            Value = self.CountTable['Input'].iloc[index]
            Count = self.CountTable['Count'].iloc[index]
            
            FollowingValue = self.CountTable['Frequency'].iloc[index]
            following = []
            
            for k in range(len(uniques)):
                    following.append(0)
            
            if Count>0:
                for i in range(len(FollowingValue)):
                    following[i] = FollowingValue[i]/Count
                    #print(following[i])
                    
            
            result=pd.Series([Value, uniques, following], index=['Value', 'FollowingValue', 'Probabilities Followed On'])
            Probability = Probability.append(result, ignore_index=True)
        
        self.FrequencyTable = Probability
        
#basic testing
mk = MarkovModel()
seq = "hello world world hello   ldkopsfpskdfpskfpskdfpsmfpskdfpmsdf sdfkms[dfs[dfk[sdfm sdf[sdmf[skdf "
mk.fit(seq)
prediction, val = mk.Predict(seq[len(seq)-1:])
value = np.argmax(prediction)
predictedval = val[value]