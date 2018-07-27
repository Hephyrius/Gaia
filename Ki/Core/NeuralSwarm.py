# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 07:34:01 2018

@author: Harnick Khera
"""
import random as r
from .FeedForwardNetwork import FeedForwardNetwork as FFN
import numpy as np
import copy

class NeuralSwarm():
    
    #Hyper Parameters
    SwarmSize = 0
    
    #store population networks and swarm sizes
    SwarmPopulations = []
    NetworkSize = []
    SwarmParticleVelocities = []
    
    #constructor for initing the "hive mind network"
    def __init__(self, _NetworkSize, _SwarmSize):
        
        self.NetworkSize = _NetworkSize
        self.SwarmSize = _SwarmSize
        self.SwarmPopulations = []
        
        #initialise the networks in the swarms
        self.initSwarms()
    
    #create random networks and add them to a population
    def initSwarms(self):
        
        #add networks to totalpops
        for j in range(self.SwarmSize):
            
            partical = FFN(self.NetworkSize)
            self.SwarmPopulations.append(partical)


    #assess the fitness of a single network
    def AssessNetworkAccuracy(self, NetworkNumber, X, Y):
        
        Network = self.SwarmPopulations[NetworkNumber]
        
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

    #assess the fitness of a single network
    def AssessAccuracy(self, Network, X, Y):

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
        
        for i in range(len(self.SwarmPopulations)):
            
            self.AssessNetworkAccuracy(i, X, Y)
        
        bestFitness = 0
        popfitness = 0
        
        for i in range(len(self.SwarmPopulations)):
            popfitness += self.SwarmPopulations[i].Fitness
            if self.SwarmPopulations[i].Fitness > bestFitness:
                bestFitness = self.SwarmPopulations[i].Fitness
                bestIndividual = i
        
        popfitness = popfitness / self.SwarmSize
        print("Best Fitness = " + str(bestFitness) + " for swarm " )
        print("Population Fitness = " + str(popfitness)+ " for swarm " )
        
        return bestFitness, bestIndividual
    
    def ArrangeByFitness(self):
        
        #sort the population in fitness order
        for j in range(len(self.SwarmPopulations)):
            
            for k in range(j+1, len(self.SwarmPopulations)):
                
                if self.SwarmPopulations.Fitness < self.SwarmPopulations[k].Fitness:
                    
                    net = self.SwarmPopulations[j]
                    self.SwarmPopulations[j] = self.SwarmPopulations[k]
                    self.SwarmPopulations[k] = net
        
    #uodate velocities
    def UpdateVelocities(self, Network, BestNetwork, GlobalNetwork, X, Y):
        
        WeightG = 0.5
        WeightP = 0.5
        W = 0.9
        Orig = copy.deepcopy(Network)
        
        for i in range(len(Network.Layers)):
            
            if i != len(Network.Layers) -1:
                
                for j in range(len(Network.Layers[i])):
                    
                    for k in range(len(Network.Layers[i][j].ConnectionsIn)):
                        Rp = r.uniform(-1,1)
                        Rg = r.uniform(-1,1)

                        
                        Pi = (BestNetwork.Layers[i][j].ConnectionsIn[k].Weight - Network.Layers[i][j].ConnectionsIn[k].Weight) * Rp * WeightP
                        Pg = (GlobalNetwork.Layers[i][j].ConnectionsIn[k].Weight - Network.Layers[i][j].ConnectionsIn[k].Weight) * Rg * WeightG
                        V =  (W*Network.Layers[i][j].ConnectionsIn[k].Velocity) + Pi + Pg
                        
                        Network.Layers[i][j].ConnectionsIn[k].Velocity = V
                        Network.Layers[i][j].ConnectionsIn[k].Weight += V
                        
                        Orig.Layers[i][j].ConnectionsIn[k].Velocity = V
                        
        self.AssessAccuracy(Network, X, Y)
        self.AssessAccuracy(Orig, X, Y)
        self.AssessAccuracy(GlobalNetwork, X, Y)
        
        UpdateGlobal = False
        NetworkToReturn = Orig
        
        if Network.Fitness> Orig.Fitness:

            NetworkToReturn = Network
            if Network.Fitness> GlobalNetwork.Fitness:
                
                UpdateGlobal = True
                
        
        return NetworkToReturn, UpdateGlobal
                              
    
    #find the avarage/middle values of the swarm            
    def GlobalPosition(self):
        
        #create a placeholder network to deal with the position of the swarm
        GlobalNet = FFN(self.NetworkSize)
        
        for i in range(len(self.SwarmPopulations[0].Layers)):
                if i != len(self.SwarmPopulations[0].Layers) - 1:
                    
                    for j in range(len(self.SwarmPopulations[0].Layers[i])):
                        
                        for k in range(len(self.SwarmPopulations[0].Layers[i][j].ConnectionsIn)):
                            
                            for l in range(self.SwarmSize):
                                GlobalNet.Layers[i][j].ConnectionsIn[k].Weight += self.SwarmPopulations[l].Layers[i][j].ConnectionsIn[k].Weight
                            
                            GlobalNet.Layers[i][j].ConnectionsIn[k].Weight /= self.SwarmSize
        return GlobalNet
            
        
    
    #optimize the swarms for x iterations
    def Fit(self, X, Y, iterations):

        for j in range(iterations):
        
            bf, bi = self.AssessPopulation(X, Y)
            BestIndiv = self.SwarmPopulations[bi]
            GlobalNet = self.GlobalPosition()
            
            for k in range(self.SwarmSize):
                IndivNet = self.SwarmPopulations[k]
                NewNet, UpdateGlobal = self.UpdateVelocities(IndivNet, BestIndiv, GlobalNet, X, Y)
                self.SwarmPopulations[k] = NewNet
                
                if UpdateGlobal == True:
                    
                    GlobalNet = self.GlobalPosition()
                    

        
          