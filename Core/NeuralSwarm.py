# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 07:34:01 2018

@author: Harnick Khera
"""
import random as r
import FeedForwardNetwork as FFN
import numpy as np

class NeuralSwarm():
    #Hyper Parameters
    InputSize = 0
    OutputSize = 0
    SwarmSize = 0
    TotalSwarms = 0
    
    #store population networks and swarm sizes
    SwarmPopulations = []
    SwarmNetworkSizes = []
    SwarmParticleVelocities = []
    
    #constructor for initing the "hive mind network"
    def __init__(self, _InputSize, _OutputSize, _SwarmSize, _TotalSwarms):
        
        self.InputSize = _InputSize
        self.OutputSize = _OutputSize
        self.SwarmSize = _SwarmSize
        self.TotalSwarms = _TotalSwarms
        self.SwarmPopulations = []
        self.SwarmNetworkSizes = []
        self.SwarmParticleVelocities = []
        
        #initialise the networks in the swarms
        self.initSwarms()
    
    #create random sized networks and add them to a population, and then add each population to the total list
    def initSwarms(self):
        
        #create random sized hidden layer sizes and counts
        for i in range(self.TotalSwarms):
            NetworkSize = []
            NetworkSize.append(self.InputSize)
            HiddenSize = r.randint(1,2)
            for j in range(HiddenSize):
                NetworkSize.append(r.randint(2,(8*self.InputSize)))
                
            NetworkSize.append(self.OutputSize)
            
            self.SwarmNetworkSizes.append(NetworkSize)
            
            Population = []
            
            #add networks to pop and then add pop to totalpops
            for j in range(self.SwarmSize):
                
                partical = FFN.FeedForwardNetwork(NetworkSize)
                Population.append(partical)
            
            self.SwarmPopulations.append(Population)
            
            #init the velocities for each connection
            for l in range(self.SwarmSize):
                PopulationVelocities = []
                IndivVelocities = []
                for j in NetworkSize:
                    
                    LayerVelocities = []
                    for k in range(j):
                       LayerVelocities.append(r.random())
                      
                    IndivVelocities.append(LayerVelocities)
                
                PopulationVelocities.append(IndivVelocities)
            
            self.SwarmParticleVelocities.append(PopulationVelocities)
                    
                    
            
    #assess the fitness of a single network
    def AssessNetworkAccuracy(self, SwarmNumber, NetworkNumber, X, Y):
        
        Network = self.SwarmPopulations[SwarmNumber][NetworkNumber]
        
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
    def AssessPopulation(self, SwarmNumber, X, Y):
        
        for i in range(len(self.SwarmPopulations[SwarmNumber])):
            
            self.AssessNetworkAccuracy(SwarmNumber, i, X, Y)
        
        bestFitness = 0
        popfitness = 0
        
        for i in range(len(self.SwarmPopulations[SwarmNumber])):
            popfitness += self.SwarmPopulations[SwarmNumber][i].Fitness
            if self.SwarmPopulations[SwarmNumber][i].Fitness > bestFitness:
                bestFitness = self.SwarmPopulations[SwarmNumber][i].Fitness
                bestIndividual = i
        
        popfitness = popfitness / self.SwarmSize
        print("Best Fitness = " + str(bestFitness) + " for swarm " + str(SwarmNumber))
        print("Population Fitness = " + str(popfitness)+ " for swarm " + str(SwarmNumber))
        
        return bestFitness, bestIndividual
    
    def ArrangeByFitness(self, SwarmNumber):
        
        #sort the population in fitness order
        for j in range(len(self.SwarmPopulations[SwarmNumber])):
            
            for k in range(j+1, len(self.SwarmPopulations[SwarmNumber])):
                
                if self.SwarmPopulations[SwarmNumber].Fitness < self.SwarmPopulations[SwarmNumber][k].Fitness:
                    
                    net = self.SwarmPopulations[SwarmNumber][j]
                    self.SwarmPopulations[SwarmNumber][j] = self.SwarmPopulations[SwarmNumber][k]
                    self.SwarmPopulations[SwarmNumber] = net
        
    #uodate velocities
    def UpdateVelocities(self, Network, BestNetwork):
        
        for i in range(len(Network.Layers)):
            
            if i != len(Network.Layers) -1:
                
                for j in range(len(Network.Layers[i])):
                    
                    for k in range(len(Network.Layers[i][j].ConnectionsIn)):
                        Rp = r.random()
                        Rg = r.random()
                        
                        #Pi = (BestNetwork.Layers[i][j].ConnectionsIn[k].Weight - Network.Layers[i][j].ConnectionsIn[k].Weight)
    
    #find the avarage/middle values of the swarm            
    def GlobalPosition(self, SwarmNumber):
        
        #create a placeholder network to deal with the position of the swarm
        GlobalPosition = FFN.FeedForwardNetwork(self.SwarmNetworkSizes[SwarmNumber])
        
        for i in range(len(self.SwarmPopulations[SwarmNumber][0].Layers)):
                if i != len(self.SwarmPopulations[SwarmNumber][0].Layers) - 1:
                    
                    for j in range(len(self.SwarmPopulations[SwarmNumber][0].Layers[i])):
            
        
    
    #optimize the swarms for x iterations
    def Optimize(self, iterations, X, Y):
        bests = []
        
        for i in range(self.TotalSwarms):
            
            for j in range(iterations):
            
                bf, bi = self.AssessPopulation(i, X, Y)
                BestIndiv = self.SwarmPopulations[i][bi]
                
                
            bests.append(BestIndiv)
            return bests
        
  
    
HiveMind = NeuralSwarm(3,2,50,10)            


##TESTING
data = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
targets = [1,0,0,1,0,1,1,0]               


HiveMind.Optimize(1, data, targets)












            