import math
from neuralnetwork.layer import Layer

class SigmoidLayer(Layer):
    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)
        self.activation       = lambda x: 1 / (1 + math.exp(-x))
        self.activation_prime = lambda x:  self.activation(x) * (1 - self.activation(x))
