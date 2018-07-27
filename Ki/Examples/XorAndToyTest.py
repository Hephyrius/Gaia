# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Harnick Khera
"""

from Ki.Core import NeuralSwarm as Hive

#Xor and And Toy Example
X = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
Y = [1,0,0,1,0,1,1,0]        

hv = Hive([3,16,2],20)
hv.Fit(X, Y, 100)
