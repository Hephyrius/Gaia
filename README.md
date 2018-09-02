# Ki 

Machine Learning, Heuristic  and other ideas. For fun and science!

## Summary:

This library is a general experiment with Heuristics, Machine Learning and other AI related ideas. 
The library is in a very early stage (ie alpha) and is focused more on exploring novel ideas rather than a specific focus on providing production-ready code.
Although if you do use it in anything accademic, please cite me! it would be appreciated!

## Installation:

```python
pip install Ki
```

## Build from source:

Run from the root directory:

```
python setup.py bdist_wheel
```

Install the compiled file by running

```
pip install dist/Ki-0.2.2-py3-none-any.whl
```

## Structure:

### Folders:

/Ki/Core/ - This contains the Algorithms

/Ki/Examples/TestData/ - This folder contains data used in testing

### Feed Forward Neural Network Classes:

/Core/Neuron.py - This class is used for the neurons within the neural network

/Core/Connection.py - This class stores connection values between neurons

/Core/FeedForward.py - This class is a basic feed forward neural network WITHOUT back propergation

/Core/GeneticNetwork.py - This class is the GA optomiser for the FeedForward neural network

/Core/NeuralSwarm.py - This class combines Particle Swarm Optimisation with neural networks

/Core/LossFunction.py - Standard loss functions such as accuracy and log loss

/Core/ActivationFunctions.py - Activation functions that are applied within neural net models to transform values - Relu, Sigmoid ect.


### Convolution Neural Network Classes:

/Core/Filter.py - This class contains the functionality needed to apply a filter to a larger matrix

/Core/Pooling.py - This class contains pooling functions that help reduce a matrix's size

/Core/ConvolutionNetwork.py - CNN implementation - This is currently being worked on

### Markov Chain/Probability Model:

/Markov/MarkovModel.py - Implemented Markov Model. This file can be fitted to a corpus of data and then use another sequence to make a prediction.

/Markov/TextGenerationExample.py - A worked example that shows the useage of the Markov Model to generate text at a character-by-character level. This is fitted on lorem ipsom.

### Fuzzy Models:

/Fuzzy/MembershipFunctions.py - An interface for using Sk-Fuzzy' membership functions. This may change to fully incorporate implementations of membership functions natively.

/Fuzzy/ANFIS.py - A WIP implementation of an Adaptive Neural Fuzzy Inference Model.

### Examples:

/Ki/Examples/XorAndToyTest.py - This class tests the Neural Swarm Algorithm on the Xor/And Toy Example

/Ki/Examples/Music.py - This class generates MIDI music by generating compositions and asking the user for a fitness score for each generated output

/Ki/Cartpole.py - This class tests the Genetic model on the OpenAI gym cartpole environment.

## Requirements:

* Python 3.6
* Numpy

### Test/Example Requirements

* Mido
* Pandas
* OpenAi Gym

## FF-NN Useage Notes:

* Data must be given as python lists
* Test data is a list of list of numbers
* Class data is a list of numbers
* All data must be numeric!
* The Neuro Evolution Algorithm tries to MAXIMISE the fitness function. The fitness function is the ACCURACY of the individual model.
* The Particle Swarm also tries to maxmise the accuracy function.

## Markov Model Notes:

*the length of the data used in a prediction MUST be the same length as the number of models selected when the model was defined.

## Example Feed Forward NN Usage:

### Init a Neuro Evolution :

```python

from Ki.Core import GeneticNetwork as GA

LayerSizes = [4,16,3]
PopSize = 20
NeuroEvo = GA.GeneticNetwork(PopSize,LayerSizes)

```

### "Fitting"


```python

X = TrainingFeatures
Y = ClassLabels
Iterations = 1000

NeuroEvo.Fit(X, Y, Iterations)

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





