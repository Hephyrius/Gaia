# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:42:15 2018

@author: Khera
"""

import numpy as np
import random as r

#Filter to be used as part of a Convolution Networks' Node
class Filter():
    
    Filter = []
    FilterX = 0
    FilterY = 0
    Stride = 0
    Padding = 0
    
    def __init__(self, _FilterX=3, _FilterY=3, _Stride=1, _Padding=1):
        
        self.FilterX = _FilterX
        self.FilterY = _FilterY
        self.Stride = _Stride
        self.Padding = _Padding
        #self.Filter = np.zeros([self.FilterX, self.FilterY])
        self.Filter = np.random.uniform(low =-1, high=1, size=[self.FilterX, self.FilterY])
    
fil = Filter(15,15)
print(fil.Filter)