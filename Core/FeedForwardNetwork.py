# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:18:40 2018

@author: Khera

Feed Forward Network
"""

import Neuron as Node
import Connection as Con

class FeedForwardNetwork():
    
    Layers = []
    
    def __init__(self, _LayerSizes):
        
        self.Layers = []
        self.CreateNetwork(_LayerSizes)
    
    
    def CreateNetwork(self, _LayerSizes):
        
        for i in _LayerSizes:
            
            Layer = []
            
            for j in range(i):
                N = Node.Neuron()
                Layer.append(N)
            
            self.Layers.append(Layer)
        self.ConnectLayers()
        
    #connect up all the nodes in the network
    def ConnectLayers(self):
        
        Length = len(self.Layers)
        print(Length)
                
        for i in range(len(self.Layers)):
            
            if i != len(self.Layers) -1:
                
                for j in self.Layers[i]:
                    
                    for k in self.Layers[i+1]:
                    
                        connection = Con.Connection(j,k)
                        j.addConnection(connection)
                    
            
            
            
            
            
            
            
            
            
                
                

Network = FeedForwardNetwork([2,5,5,1])