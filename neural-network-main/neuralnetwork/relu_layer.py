from neuralnetwork.layer import Layer

class ReLuLayer(Layer):
    def __init__(self, inputs, outputs):
        super().__init__(inputs, outputs)
        self.activation       = lambda x: 0 if x < 0 else x
        self.activation_prime = lambda x: 0 if x < 0 else 1
