# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Khera
"""
import FeedForwardNetwork as net
import numpy as np

class GeneticNetwork():
    
    Population = []
    PopulationSize = 0
    NetworkSize = []
    Fitnesses = []
    
    def __init__(self, _PopulationSize, _NetworkSize):
        
        self.Population = []
        self.Fitnesses = []
        self.PopulationSize = _PopulationSize
        self.NetworkSize = _NetworkSize
        
        #initialise the starting population
        for i in range(self.PopulationSize):
            
            self.Population.append(net.FeedForwardNetwork(self.NetworkSize))
            self.Fitnesses.append(0)
    
    
    #assess the fitness of a single network
    def AssessNetworkAccuracy(self, NetworkNumber, X, Y):
        
        Network = self.Population[NetworkNumber]
        
        TotalValues = len(Y)
        Accuracy = 0
        
        for i in range(len(Y)):
            #print(i)
            prediction = Network.predict(X[i])
            
            if np.argmax(prediction) == Y[i]:
                #print(np.argmax(prediction))
                Accuracy += 1
        
        Fitness = Accuracy/TotalValues
        
        return Fitness
    
    #Assess the entire population
    def AssessPopulation(self, X, Y):
        
        for i in range(len(self.Population)):
            
            fitness = self.AssessNetworkAccuracy(i, X, Y)
            self.Fitnesses[i] = fitness
    
        bestFitness = 0
        
        for i in self.Fitnesses:
            print(i)

        
data = [[0,0],[0,1],[1,0],[1,1]]
targets = [1,0,0,1]        
        
GA = GeneticNetwork(10, [2,2,2])
GA.AssessPopulation(data, targets)











