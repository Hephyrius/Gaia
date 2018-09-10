# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 19:19:24 2018

@author: Harnick Khera

This class deals with the independant membership functions.
"""

import skfuzzy as fz
import numpy as np
from .Core.Connection import Connection as con

class MembershipFunction():
    
    inited = False
    MF = None
    MFType = 0
    MFValues = [0,1,2,3]
    
    def __init__(self, _MFType=0, abcd = [0,1,2,3]):
        self.inited = True
        self.MFType = _MFType
        self.MFValues = np.asarray(abcd)
    
    #dynamic MF Evaluation, This is done so that Neural Fuzzy type models can use heuristics with ease
    def EvaluateMF(self, X):
        
        #S Function
        if self.MFType == 0:
            return fz.membership.smf(X, self.MFValues[0], self.MFValues[1])
        
        #trapizoidal Function
        if self.MFType == 1:
            return fz.membership.trapmf(X, self.MFValues)
    
        #traingular Function
        if self.MFType == 2:
            return fz.membership.trimf(X, self.MFValues[0:3])
        
        #sigmoid Function
        if self.MFType == 3:
            return fz.membership.sigmf(X, self.MFValues[0], self.MFValues[1])
        
        #gaussmf Function
        if self.MFType == 4:
            return fz.membership.gaussmf(X, self.MFValues[0], self.MFValues[1])
        
        #bell Function
        if self.MFType == 5:
            return fz.membership.gbellmf(X, self.MFValues[0], self.MFValues[1], self.MFValues[2])
        
        #Z shaped Function
        if self.MFType == 6:
            return fz.membership.zmf(X, self.MFValues[0], self.MFValues[1])
        
## Crude Testing
#mf = MembershipFunction(6,[0,2,4,6])
#i = mf.EvaluateMF(np.asarray([2]))