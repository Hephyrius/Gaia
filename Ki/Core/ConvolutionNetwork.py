# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:30:16 2018

@author: Khera
"""
#ConvNet Specific
from .Filter import Filter as Node
from .Pooling import Pooling as Pool

#Traditional FeedForward Structures
from .Neuron import Neuron as Node
from .Connection import Connection as Con

#Cross model classes
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
        


    
    
    
    
    
    
    
    
    
    