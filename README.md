# Gaia 

Nature inspired ML and Heuristic Combos. For fun and science!

## Summary:

This repo is just me experimenting with Heuristics, Machine Learning and other ideas. 
I don't intend for it to be used in any manner, for now atleast.
Although if you do use it in anything accademic, please cite me! it would be appreciated!

## Structure:

### Folders:

/Core/ - This contains the Algorithms

/Core/TestData/ - This folder contains data used in testing

### NeuroEvolutionary Classes:

/Core/Neuron.py - This class is used for the neurons within the neural network
/Core/Connection.py - This class stores connection values between neurons
/Core/FeedForward.py - This class is a basic feed forward neural network WITHOUT back propergation
/Core/GeneticNetwork.py - This class is the GA optomiser for the FeedForward neural network!

## Algorithm Scores

### NeuroEvolutionary:
* Iris: 98% 
* Xor / AND : 75%

## Sources: 
[1] IRIS dataset - https://archive.ics.uci.edu/ml/datasets/iris [TestData/Iris]

## Requirements:

*Python 3.6
*Numpy
*Pandas

## Useage Notes:

* Data must be given as python lists
* Test data is a list of list of numbers
* Class data is a list of numbers
* All data must be numeric!
* The Neuro Evolution Algorithm tries to MAXIMISE the fitness function. The fitness function is the ACCURACY of the individual model.

## Usage:

### Init a Neuro Evolution :

```python

import GeneticNetwork as GA

LayerSizes = [4,16,3]
PopSize = 20
NeuroEvo = GA.GeneticNetwork(PopSize,LayerSizes)

```

### "Fitting"


```python

X = TrainingFeatures
Y = ClassLabels
Iterations = 1000

NeuroEvo.Neat(X, Y, Iterations)

```

### Using The Results

```python
import numpy as np

Network = NeuroEvo.Population[0]
NewData = [21231,12313,1231, 1]

preds = Network.predict(NewData)
class = np.argmax(preds)

```

## Citation

@misc{Khera2018Gaia,
  title={Hephyrion},
  author={Khera, Harnick},
  year={2018},
  howpublished={\url{https://github.com/hephyrius/hephyrion}},
}





