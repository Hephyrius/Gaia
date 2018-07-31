# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 22:13:16 2018

@author: Khera
"""

class LossFunctions():
    
    Regression = False
    
    def __init__(self, _Regression):
        self.Regression = _Regression

    
    def Accuracy(self, Y, Predictions):
        
        value = 0
        
        if self.Regression == False:
            
            for i in range(Y):
                
                if Y[i] == np.argmax(Predictions[i]):
                    
                    value +=1
        value /= len(Y)
        return value
                
        
        