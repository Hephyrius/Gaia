# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:42:15 2018

@author: Khera
"""

import numpy as np
import ActivationFunctions as act
#from scipy import signal
import random as r

#Filter to be used as part of a Convolution Networks' Node
class Filter():
    
    Filter = []
    FilterSize = []
    Stride = []
    Padding = []
    
    def __init__(self, _FilterSize=[3,3], _Stride=[1,1], _Padding=[1,1,1,1]):
        
        self.FilterSize = _FilterSize
        self.Stride = _Stride
        self.Padding = _Padding

        self.Filter = np.random.uniform(low =-1, high=1, size=[self.FilterSize[0], self.FilterSize[1]])
    
    #Apply a filter to some input data
    def ApplyFilter(self, InputArray):
        
        xStride = int(InputArray.shape[0]/self.Stride[0])
        yStride = int(InputArray.shape[1]/self.Stride[1])
        
        filterOutput = np.zeros([xStride,yStride])
        
        #Apply the filter to the input
        for i in range(xStride):
            for j in range(yStride):
                
                padded = np.zeros([self.FilterSize[0], self.FilterSize[1]])                
                cube = InputArray[i:i+self.FilterSize[0],j:j+self.FilterSize[1]]
                
                padded[:cube.shape[0], :cube.shape[1]] = cube
                Filtered = padded*self.Filter
                filterOutput[i,j] = np.sum(Filtered)
        
        return filterOutput
    
    #apply activations to filtered results
    def ApplyActivation(self, Data):
        a = act.ActivationFunctions(0)
        for i in range(Data.shape[0]):
            for j in range(Data.shape[1]):
                Data[i,j] = a.Relu(Data[i,j])

#Test Data of a Cube
data = [[1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1]]

data = np.asarray(data)

#Multiple filters
filts = []
outs = []
for i in range(5):
    
    filts.append(Filter())
    out = filts[i].ApplyFilter(data)
    filts[i].ApplyActivation(out)
    outs.append(out)
    print(out)











