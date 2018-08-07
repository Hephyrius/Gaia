# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 00:14:41 2018

@author: Khera
"""
import numpy as np

class Pooling():
    
    WindowSize = [2,2]
    
    def __init__(self, _WindowSize=[2,2]):
        
        self.WindowSize = _WindowSize
    
    def MaxPoolData(self, Data):
        
        X = int(Data.shape[0] / self.WindowSize[0]) +1
        Y = int(Data.shape[1] / self.WindowSize[1]) +1
        
        Out =  np.zeros([X,Y])
        
        for i in range(0, Data.shape[0], self.WindowSize[0]):
            for j in range(0, Data.shape[1], self.WindowSize[1]):
                
                Window = Data[i:i+self.WindowSize[0], j:j+self.WindowSize[1]]
                Value = np.max(Window)
                x = int(i/self.WindowSize[0])
                y = int (j/self.WindowSize[1])
                Out[x,y] = Value
    
        return Out
        
    def Flatten(self, data):
        
        return np.ravel(data)
        
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

pool = Pooling()
pooled = pool.MaxPoolData(data)
pooled2 = pool.MaxPoolData(pooled)
flat = pool.Flatten(pooled2)



