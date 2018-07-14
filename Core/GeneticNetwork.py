# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Khera
"""
import FeedForwardNetwork as FFN
import numpy as np
import pandas as pd
import copy
import random as r

class GeneticNetwork():
    
    Population = []
    PopulationSize = 0
    NetworkSize = []
    Best = []
    
    def __init__(self, _PopulationSize, _NetworkSize):
        
        self.Population = []
        self.PopulationSize = _PopulationSize
        self.NetworkSize = _NetworkSize
        self.Best = []
        
        #initialise the starting population
        for i in range(self.PopulationSize):
            
            self.Population.append(FFN.FeedForwardNetwork(self.NetworkSize))
    
    
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
        Network.Fitness = Fitness
    
    #Assess the entire population
    def AssessPopulation(self, X, Y):
        
        for i in range(len(self.Population)):
            
            self.AssessNetworkAccuracy(i, X, Y)
        
        bestFitness = 0
        popfitness = 0
        
        for i in range(len(self.Population)):
            popfitness += self.Population[i].Fitness
            if self.Population[i].Fitness > bestFitness:
                bestFitness = self.Population[i].Fitness
        
        popfitness = popfitness / self.PopulationSize
        print("Best Fitness = " + str(bestFitness))
        print("Population Fitness = " + str(popfitness))
        
        return bestFitness
    
    #Copy a network
    def CopyNetworkIndex(self, index):
        
        NewNet = copy.deepcopy(self.Population[index])
        NewNet.Fitness = 0
        return NewNet
    
    #Copy a network
    def CopyNetwork(self, Network):
        NewNet = copy.deepcopy(Network)
        NewNet.Fitness = 0
        return NewNet
    
    #crossover style using a the mean of the weights and biases
    def Crossover(self, Network1, Network2):

        newNet = FFN.FeedForwardNetwork(self.NetworkSize)
        
        for i in range(len(newNet.Layers)):
            
            if i != len(newNet.Layers) -1:
                
                for j in range(len(newNet.Layers[i])):
                    
                    for k in range(len(newNet.Layers[i][j].ConnectionsIn)):
                        
                        newNet.Layers[i][j].ConnectionsIn[k].Weight = (Network1.Layers[i][j].ConnectionsIn[k].Weight + Network2.Layers[i][j].ConnectionsIn[k].Weight)/2
                    
                    newNet.Layers[i][j] = (Network1.Layers[i][j].Bias + Network2.Layers[i][j].Bias)/2
        
        return newNet
                        
    
    #mutate a network
    def Mutate(self, Network):
        
        for i in range(len(Network.Layers)):
            
            if i != len(Network.Layers) -1:
                
                for j in Network.Layers[i]:
                    
                    for k in j.ConnectionsIn:
                        
                        val = r.random()
                        
                        #flip the weight sign
                        if val <= 0:
                            
                            k.Weight *= -1
                        
                        #randomise the weight value
                        elif val <= 0.02:
                            
                            k.Weight = r.random()
                        
                        #increase by a factor
                        elif val <= 0.04:
                            
                            factor = r.random() + 1
                            k.Weight *= factor
                            
                        elif val <=0.08:
                            
                            factor = r.random()
                            k.Weight *= factor
        
                    val = r.random()
                    
                    #flip the weight sign
                    if val <= 0:
                        
                        j.Bias *= -1
                    
                    #randomise the weight value
                    elif val <= 0.02:
                        
                        j.Bias = r.random()
                    
                    #increase by a factor
                    elif val <= 0.04:
                        
                        factor = r.random() + 1
                        j.Bias *= factor
                        
                    elif val <=0.08:
                        
                        factor = r.random()
                        j.Bias *= factor
                            
    #do the entire GA process
    def Neat(self, X, Y, NumIterations):
        
        for i in range(NumIterations):
            
            #assess the networks
            self.AssessPopulation(X, Y)
            
            #sort the population in fitness order
            for j in range(len(self.Population)):
                
                for k in range(j+1, len(self.Population)):
                    
                    if self.Population[j].Fitness < self.Population[k].Fitness:
                        
                        net = self.Population[j]
                        self.Population[j] = self.Population[k]
                        self.Population[k] = net
            
            #store the best two in the bests array
            self.Best = []
            self.Best.append(self.Population[1])
            self.Best.append(self.Population[0])
            
            #Create a new Population
            NewPopulation = []
            NewPopulation.append(self.Population[1])
            NewPopulation.append(self.Population[0])
            
            for i in range(self.PopulationSize - 2):
                
                operation = r.random()
                
                if operation <=0.9:
                    
                    net = r.randrange(0,self.PopulationSize/2)
                    newNet = self.CopyNetworkIndex(net)
                    self.Mutate(newNet)
                    NewPopulation.append(newNet)
                
#                elif operation <= 1:
#                    
#                    net1 = r.randrange(2,self.PopulationSize/2)
#                    net2 = r.randrange(2,self.PopulationSize/2)
#                    
#                    net3 = self.Crossover(self.Population[net1], self.Population[net2])
#                    NewPopulation.append(net3)
#                
                else: 
                    #print(self.NetworkSize)
                    NewPopulation.append(FFN.FeedForwardNetwork(self.NetworkSize))
            
            self.Population = NewPopulation
