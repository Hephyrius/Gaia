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

def ConvolutionNetwork():
    
    Layers = []
    LayerTypes = []
    Activations = []
    NumberOutputs = 0
    Fitness = 0
    
    #get the hyper parameters ready
    def __init__(self, _LayerSizes, _LayerTypes, _NumberOutputs):
        
        self.Layers = []
        self.LayerTypes = []
        self.Activations = []
        self.Fitness = 0
        self.NumberOutputs = _NumberOutputs
        
        self.CreateNetwork(_LayerSizes, _LayerTypes)
    
    #need to make this more dynamic...
    def CreateNetwork(self, _LayerSizes, _LayerTypes):

        Layer1 = []
        Layer2 = []
        Layer3 = []
        Layer4 = []
        Layer5 = []
        Layer6 = []
        
        for i in range(32):
            
            Layer1.append(Filter())
        
        Layer2.append(Pooling())
        
        for i in range(32):
            
            Layer3.append(Filter())
        
        Layer4.append(Pooling())
        
        for i in range(self.NumberOutputs):
            
            Layer6.append(Node())

        
        


    
    
    
    
    
    
    
    
    
    