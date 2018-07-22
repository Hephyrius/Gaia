# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 07:34:01 2018

@author: Harnick Khera
"""

class NeuralSwarm():
    
    InputSize = 0
    OutputSize = 0
    SwarmSize = 0
    TotalSwarms = 0
    SwarmSizes = []
    
    def __init__(self, _InputSize, _OutputSize, _SwarmSize, _TotalSwarms):
        
        self.InputSize = _InputSize
        self.OutputSize = _OutputSize
        self.SwarmSize = _SwarmSize
        self.TotalSwarms = _TotalSwarms
        self.SwarmSizes = []
        
        
    def initSwarms(self):
        
        