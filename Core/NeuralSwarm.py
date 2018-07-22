# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 07:34:01 2018

@author: Harnick Khera
"""
import random as r
import FeedForwardNetwork as FFN

class NeuralSwarm():
    #Hyper Parameters
    InputSize = 0
    OutputSize = 0
    SwarmSize = 0
    TotalSwarms = 0
    
    #store population networks and swarm sizes
    SwarmPopulations = []
    SwarmNetworkSizes = []
    
    def __init__(self, _InputSize, _OutputSize, _SwarmSize, _TotalSwarms):
        
        self.InputSize = _InputSize
        self.OutputSize = _OutputSize
        self.SwarmSize = _SwarmSize
        self.TotalSwarms = _TotalSwarms
        self.SwarmPopulations = []
        self.SwarmNetworkSizes = []
        
        #initialise the networks in the swarms
        self.initSwarms()
    
    #create random sized networks and add them to a population
    def initSwarms(self):
        
        for i in range(self.TotalSwarms):
            NetworkSize = []
            NetworkSize.append(self.InputSize)
            HiddenSize = r.randint(1,2)
            for j in range(HiddenSize):
                NetworkSize.append(r.randint(2,(8*self.InputSize)))
                
            NetworkSize.append(self.OutputSize)
            
            self.SwarmNetworkSizes.append(NetworkSize)
            
            Population = []
            
            for j in range(self.SwarmSize):
                
                partical = FFN.FeedForwardNetwork(NetworkSize)
                Population.append(partical)
            
            self.SwarmPopulations.append(Population)
            
HiveMind = NeuralSwarm(3,2,100,1)            
            

            