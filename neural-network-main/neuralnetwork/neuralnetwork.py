import random
import math

from neuralnetwork.sigmoid_layer import SigmoidLayer
from neuralnetwork.relu_layer import ReLuLayer

class NeuralNetwork:
    def __init__(self, inputs, eta=0.01, momentum=0):
        self.input_neurons = inputs
        self.layers   = []
        self.eta      = eta
        self.momentum = momentum

    def train(self, inputs, targets, epochs=1):
        assert len(inputs[0]) == self.input_neurons
        assert len(targets[0]) == len(self.layers[-1].weights)

        gradient = [[0] * len(targets[0][0]) for i in range(len(targets[0]))]
        
        for epoch in range(epochs):
            training_data = list(zip(inputs, targets))
            random.shuffle(training_data)
            for data, target in training_data:
                result = self.feedforward(data)
                
                error = self.mean_squared_error(result, target)
                gradient = self.mean_squared_error_prime(result, target)             

                self.backward(gradient)

            print(f"EPOCH: {str(epoch).ljust(10)} ERROR: {round(error, 8)}")

    def predict(self, inputs, targets):
        for data, target in zip(inputs, targets):
            result = self.feedforward(data)
            yield result, target

    def feedforward(self, inputs):
        current_results = inputs
        
        for layer in self.layers:
            current_results = layer.forward(current_results)

        return current_results

    def backward(self, gradient):
        current_gradient = gradient
        for layer in reversed(self.layers):
            current_gradient = layer.backward(current_gradient, self.eta, self.momentum)

    def find_number_of_inputs(self):
        if len(self.layers) == 0:
            inputs = self.input_neurons
        else:
            inputs = len(self.layers[-1].weights)

        return inputs

    def add_relu_layer(self, neurons):
        inputs = self.find_number_of_inputs()
        self.layers.append(ReLuLayer(inputs, neurons))

    def add_sigmoid_layer(self, neurons):
        inputs = self.find_number_of_inputs()
        self.layers.append(SigmoidLayer(inputs, neurons))

    def mean_squared_error(self, results, targets):
        errors = 0
        for i in range(len(results)):
            for j in range(len(results[0])):
                errors += pow(targets[i][j] - results[i][j], 2)

        return errors / len(results)

    def mean_squared_error_prime(self, results, targets):
        result = []
        size = len(results)
        for i in range(len(results)):
            row = []
            for j in range(len(results[0])):
                row.append(2 * (targets[i][j] - results[i][j]) / size)

            result.append(row)

        return result
