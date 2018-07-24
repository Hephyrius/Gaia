# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 05:50:07 2018

@author: Harnick Khera
"""
from Ki.Core import GeneticNetwork as Gen
import numpy as np
import pandas as pd
import mido
import os
import random as r
from mido import MidiFile, MidiTrack, Message


def CustomAssessor(Nets, Net, X,Y):
    
    result = []
    inds = r.randint(0,len(X)-1)
    
    for i in X[inds]:
        result.append(i)
    
    for i in range(100):
        
        pre = Nets.Population[Net].predict(result[i:i+16])
        result.append(np.argmax(pre))
    
    print(result)
    
    steps = convertSequenceToMidi(result, "File", 100)
    
    if steps > 10:
        os.system("start "+ "File" + ".mid")
        try:
            fit = input("Fitness Value For Network:")
            
            fit = int(fit)
            
            Nets.Population[Net].Fitness = fit
        except Exception as e:
            Nets.Population[Net].Fitness = 0
    else:
        Nets.Population[Net].Fitness = 0
    
def convertSequenceToMidi(generatedSequence, filename, timetick):
        #code to convert back to midi
    print("converting back to midi")

    prevNotes = []
    notes = []
    pr = np.asarray(notes)
    
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    time = 0
    numSteps = 0
    for n in generatedSequence:

    
        if n ==128:
            time = timetick
            msg = mido.Message('note_off')
            mgtime = int(time)
            msg.time = mgtime
            track.append(msg)
            no = np.asarray(notes)
            for x in no:
                
                if not (x in pr):
                    msg = mido.Message('note_on', note=x, velocity=100)
                    track.append(msg)
            
            for x in pr:
                
                if not (x in no):
                    msg = mido.Message('note_off', note=x)

                    track.append(msg)
                
            pr = no.copy()
            numSteps+=1
        
            notes = []
        elif n in notes:
            
            time = timetick
            msg = mido.Message('note_off')
            mgtime = int(time)
            msg.time = mgtime
            track.append(msg)
            no = np.asarray(notes)
            for x in no:
                
                if not (x in pr):
                    msg = mido.Message('note_on', note=x, velocity=100)
                    track.append(msg)
            
            for x in pr:
                
                if not (x in no):
                    msg = mido.Message('note_off', note=x)

                    track.append(msg)
                
            pr = no.copy()
            numSteps+=1
        
            notes = []
        else:
            notes.append(n)
    
    mid.save(filename+'.mid') 
    return numSteps
    
def AssessAllNetworks(Nets, X, Y):

    for i in range(len(Nets.Population)):
        
        CustomAssessor(Nets, i, X, Y)

GA = Gen(20, [16,32,129])

seed = []
seed.append([62, 81, 128, 62, 78, 81, 128,62, 74, 78, 81, 128,74, 78, 81, 128])
seed.append([45, 57, 60,  64, 128, 45, 52, 57, 60, 64, 128, 45, 52, 57, 60, 128])
seed.append([67, 71, 79,128, 67, 71, 128,128,67, 128, 74, 128,74, 79, 128,71])
seed.append([71, 76, 128,71, 128,71, 74, 128,74, 128,72, 74,128, 72,128, 69])
y = [1]
#%%
GA.Fit(seed, y, 10, True, AssessAllNetworks)



























