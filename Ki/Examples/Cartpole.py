# -*- coding: utf-8 -*-
"""
@author: Harnick Khera
"""

import gym
import sys
from Ki.Core import GeneticNetwork as Gen
import numpy as np

def assessIndividual(network, render=False):
    
    fitness = 0
    
    env = gym.make('CartPole-v0')
    observation = env.reset()
    prevObservation = []
    steps = 0
    for _ in range(200):
        if render == True:
            env.render() 
            
        steps +=1
        #time.sleep(0.001)
        if _ == 0:
            action = network.predict(observation)
        else:
            action = network.predict(prevObservation)
       
        #action = env.action_space.sample() # your agent here (this takes random actions)
        action = np.argmax(action)
        prevObservation, reward, done, info = env.step(action)
        
        fitness += reward
        
        if done == True:
            #fitness += 1000
            env.close()
            #network.Fitness  /= steps
            network.Fitness = fitness#/steps
            print(network.Fitness)
            break
        
        
    print("_")
    network.Fitness = fitness
    #network.Fitness /= steps
    env.close()
    return fitness

def AssessPopulation(Networks, X, Y):
    
    for i in Networks.Population:
        
        assessIndividual(i, True)
        
    popFit = 0
    bestFit = 0
    idx = 0
    for i in Networks.Population:
        
        popFit += i.Fitness
        
        if i.Fitness > bestFit :
            
            bestFit = i.Fitness
            idx = Networks.Population.index(i)
            
    popFit /= len(Networks.Population)
    print("Population Fitness = " + str(popFit))
    print("Best Fitness " + str(bestFit))
    
    if bestFit == 200:
        
        avg = 0
        
        for i in range(100):
            net = Networks.Population[idx]
            avg += assessIndividual(net, True)
        
        avg /=100
        
        if avg>=195:
            print("SOLVED")
            print(idx)
            sys.exit()
            
        else:
            print("NOT SOLVED")
            
        
    

GA = Gen(20, [4,16,2])
X = [1]
Y = [1]
GA.Fit(X, Y, 5, True, AssessPopulation)
