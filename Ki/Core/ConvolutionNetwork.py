# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:30:16 2018

@author: Khera
"""
#ConvNet Specific
from Filter import Filter
from Pooling import Pooling

#Traditional FeedForward Structures
from Neuron import Neuron as Node
from Connection import Connection as Con

#Cross model classes
from ActivationFunctions import ActivationFunctions as Act

import numpy as np

class ConvolutionNetwork():
    
    Layers = []
    LayerTypes = []
    Activations = []
    NumberOutputs = 0
    InputSize = []
    Fitness = 0
    
    #get the hyper parameters ready
    def __init__(self, _LayerSizes, _LayerTypes, _InputSize, _NumberOutputs):
        
        self.Layers = []
        self.LayerTypes = []
        self.Activations = []
        self.Fitness = 0
        self.NumberOutputs = _NumberOutputs
        self.InputSize = _InputSize
        
        self.CreateNetwork(_LayerSizes, _LayerTypes)
    
    def AddLayers(self, FilterSize=[3,3], NumberFilters=8, NumberLayers=2):
        
        for i in range(NumberLayers):
            Layer = []
            
            for i in range(NumberFilters):
                Layer.append(Filter(FilterSize))
        
        self.Layers.append(Layer)
        self.LayerTypes.append(0)
        
        Layer = [Pooling()]
        self.Layers.append(Layer)
        self.LayerTypes.append(1)
    
    #Dynamically add Filter and Pooling Layers
    def CreateNetwork(self, _LayerSizes, _LayerTypes):
        
        for i in range(2):
            self.AddLayers([3+i,3+i], 16, 1)

        
        
    def CalculateNumberNeurons(self):
        
        zeros = np.zeros(self.InputSize)
        
        #for i in range(self.LayerTypes):
            

CNN = ConvolutionNetwork(0,0, [256,256], 3) 
    
    
    
    
    
    
    
    
    