# Ki 

Nature inspired ML and Heuristic Combos. For fun and science!
Named after the Sumerian god of earth.

## Summary:

This repo is just me experimenting with Heuristics, Machine Learning and other ideas. 
I don't intend for it to be used in any manner, for now atleast.
Although if you do use it in anything accademic, please cite me! it would be appreciated!

## Structure:

### Folders:

/Ki/Core/ - This contains the Algorithms

/Ki/Examples/TestData/ - This folder contains data used in testing

### Python Classes:

/Core/Neuron.py - This class is used for the neurons within the neural network
/Core/Connection.py - This class stores connection values between neurons
/Core/FeedForward.py - This class is a basic feed forward neural network WITHOUT back propergation
/Core/GeneticNetwork.py - This class is the GA optomiser for the FeedForward neural network
/Core/NeuralSwarm.py - This class combines Particle Swarm Optimisation with neural networks
/Ki/Examples/TestModels.py - This class tests the models across common datasets

### Reinforcement-Learning Branches

/Core/ReinforcementTest.py - This class tests the Genetic model on the OpenAI gym cartpole challenge. - See the Reinforcement-Learning branch for this

### Reinfrocement Music Branch

/Core/GeneticMusic.py - This class generates MIDI music by generating compositions and asking the user for a fitness score for each generated output. See the Music branch for this file.

## Requirements:

* Python 3.6
* Numpy

### Test/Example Requirements

* Mido
* Pandas
* OpenAi Gym

## Useage Notes:

* Data must be given as python lists
* Test data is a list of list of numbers
* Class data is a list of numbers
* All data must be numeric!
* The Neuro Evolution Algorithm tries to MAXIMISE the fitness function. The fitness function is the ACCURACY of the individual model.
* The Particle Swarm also tries to maxmise the accuracy function.

## Usage:

### Init a Neuro Evolution :

```python

From Ki.Core import GeneticNetwork as GA

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
PredictionClass = np.argmax(preds)

```
## License:

Eclipse Public License 2.0 (EPL-2.0)

## Citation

@misc{Khera2018Ki,
  title={Ki},
  author={Khera, Harnick},
  year={2018},
  howpublished={\url{https://github.com/hephyrius/Ki}},
}





