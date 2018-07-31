# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 19:40:34 2018

@author: Khera
"""
import numpy as np

class LossFunctions():
    
    f = 0
    
    def __init__(self):
        self.f = 0
        
    #More Traditional Loss Functions        
    def Sigmoid(self, x):
        return 1 / (1 + np.exp(-x))   
    
    def DerivedRelu(self, x):
        return 1. * (x > 0)
    
    #essentially x = x
    def Identity(self, x):
        return x
    
    def Arctan(self, x):
        return np.arctan(x)
    
    #Hyperbolic Losses
    #Cosh, Sinh, Tanh
    def Cosh(self, x):
        return np.cosh(x)
    
    def Sinh(self, x):
        return np.sinh(x)
    
    def Tanh(self, x):
        return np.tanh(x)
    
    #Trig style losses:
    #Sin, Cos, Tan
    
    def Cos(self, x):
        return np.cos(x)
    
    def Sin(self, x):
        return np.sin(x)
    
    def Tan(self, x):
        return np.tan(x)
    
    
losses = LossFunctions()
tan = losses.Arctan(-0.005)
print(tan)
