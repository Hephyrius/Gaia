# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:18:40 2018

@author: Khera

Feed Forward Network
"""

import Neuron as Node
import Connection as Con
import numpy as np
import math

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
                        j.addOutConnection(connection)
                        k.addInConnection(connection)
                        
    
    #Feed Forward
    def predict(self, _inputs):
        
        #print("Feeding Forward!")
        
        for i in range(len(_inputs)):
            self.Layers[0][i].Value = _inputs[i]
            self.Layers[0][i].ActivatedAdjustedValue = self.sigmoid(self.Layers[0][i].Value)
        
        for i in range(1, len(self.Layers)):
            
            for j in self.Layers[i]:
                
                nodeValue = 0
                
                for k in j.ConnectionsIn:
                    
                    nodeValue += (k.Weight * k.Node1.ActivatedAdjustedValue) #+ k.Node2.Bias
                
                #print(nodeValue)
                j.Value = nodeValue
                j.ActivatedAdjustedValue = self.sigmoid(j.Value)
                
        outputs = []
        
        for i in self.Layers[len(self.Layers)-1]:
            
            outputs.append(i.ActivatedAdjustedValue)
        
        return outputs
                

    def sigmoid(self, x):
        
        return 1 / (1 + math.exp(-x))           
    
                    
#Network = FeedForwardNetwork([1,5,5,10])
#preds = Network.predict([8])
#prediction = np.argmax(preds)

























