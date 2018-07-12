# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:18:28 2018

@author: Khera

Connection between two neurons
"""

class Connection():
    
    Node1 = ""
    Node2 = ""
    Weight = 0
    
    
    def __init__(self, _Node1, _Node2):
        
        self.Node1 = _Node1
        self.Node2 = _Node2
        