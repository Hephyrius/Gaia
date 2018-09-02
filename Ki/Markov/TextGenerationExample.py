# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 01:24:07 2018

@author: Khera

this example generates text based on an example input sequence/corpus
"""
import MarkovModel
import numpy as np
import random as r

#basic testing
mk = MarkovModel.MarkovModel(16)
seq = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
#seq = seq.replace(" ", "")
mk.fit(seq)

for i in range(1000):
    lastn = seq[len(seq)-17:]
    prediction, val = mk.Predict(lastn)
    selection = []
    maxVal = np.max(prediction)
    
    for i in range(len(prediction)):
        if prediction[i] >(maxVal*0.25):
            selection.append(i)
            
    rand = r.randint(0, len(selection)-1)
    value = selection[rand]
    predictedval = val[value]
    #print(lastn)
    seq += str(predictedval)

print(seq)