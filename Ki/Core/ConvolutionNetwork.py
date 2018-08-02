# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:30:16 2018

@author: Khera
"""
from .Neuron import ConvolutionNeuron as Node
from .Connection import Connection as Con
from .ActivationFunctions import ActivationFunctions as Act
import numpy as np

def ConvolutionNetwork():
    
    Layers = []
    Activations = []
    Fitness = 0
    
    #Convolution Features
    Filters = []
    FilterSizes = []
    
    def __init__(self, _LayerSizes, _FilterSizes=[3,3]):
        
        self.Layers = []
        self.Activations = []
        self.Fitness = 0
        
        #Conv Parameters
        self.Filters = []
        self.FilterSizes = _FilterSizes
        
        self.CreateNetwork(_LayerSizes)
    
    #Create the networks nodes
    def CreateNetwork(self, _LayerSizes):
        
        for i in _LayerSizes:
            self.Activations.append(6)
            Layer = []
            
            for j in range(i):
                N = Node()
                Layer.append(N)
            
            self.Layers.append(Layer)
        self.ConnectLayers()
    
    #connect up all the nodes in the network
    def ConnectLayers(self):
        
        Length = len(self.Layers)
        #print(Length)
                
        for i in range(len(self.Layers)):
            
            if i != len(self.Layers) -1:
                
                for j in self.Layers[i]:
                    
                    for k in self.Layers[i+1]:
                    
                        connection = Con(j,k)
                        j.addOutConnection(connection)
                        k.addInConnection(connection)

    
    
    
    
    
    
    
    
    
    
    
    
    