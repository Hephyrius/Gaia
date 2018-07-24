# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:10:56 2018

@author: Harnick Khera
"""

from Ki.Core import GeneticNetwork as Gen

#Xor and And Toy Example
X = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
Y = [1,0,0,1,0,1,1,0]        

GA = Gen(20, [4,16,3])
GA.Fit(X, Y, 500)

























