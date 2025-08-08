import random
import math

class Layer:
    def __init__(self, inputs, outputs):
        self.input_data     = None
        self.pre_activation = None
        self.init_weights(inputs, outputs)
        self.init_biases(outputs)

    def init_weights(self, inputs, outputs):
        self.weights = []
        for _ in range(outputs):
            self.weights.append([random.gauss(0, math.sqrt(1/inputs)) for _ in range(inputs)])

        self.delta_weights = [[0] * inputs for i in range(outputs)]

    def init_biases(self, outputs):
        self.biases = [[random.uniform(-0.1, 0.1)] for _ in range(outputs)]

    def forward(self, inputs):
        self.dense_forward(inputs)

        activations = []
        for i in range(len(self.pre_activation)):
            for j in range(len(self.pre_activation[0])):
                activations.append([self.activation(self.pre_activation[i][j])])

        return activations

    def dense_forward(self, inputs):
        self.input_data = inputs
        self.pre_activation =  [[0] * len(inputs[0]) for _ in range(len(self.weights))]
        
        for i in range(len(self.weights)):
            for j in range(len(inputs[0])):
                for k in range(len(self.weights[0])):
                    self.pre_activation[i][j] += self.weights[i][k] * inputs[k][j] + self.biases[i][j]
                
    def backward(self, gradient, eta, momentum):
        activation_gradient = []
        for i in range(len(gradient)):
            row = []
            for j in range(len(gradient[i])):
                row.append(gradient[i][j] * self.activation_prime(self.pre_activation[i][j]))
            activation_gradient.append(row)
            
        return self.dense_backward(activation_gradient, eta, momentum)

    def dense_backward(self, gradient, eta, momentum):
        t_inputs = [[0] * len(self.input_data) for _ in range(len(self.input_data[0]))]
        for i in range(len(self.input_data)):
            for j in range(len(self.input_data[0])):
                t_inputs[j][i] = self.input_data[i][j]

        weight_gradients = [[0] * len(t_inputs[0]) for _ in range(len(gradient))]
        for i in range(len(gradient)):
            for j in range(len(t_inputs[0])):
                for k in range(len(gradient[0])):
                    weight_gradients[i][j] += gradient[i][k] * t_inputs[k][j]

        t_weights = [[0] * len(self.weights) for _ in range(len(self.weights[0]))]
        for i in range(len(self.weights)):
            for j in range(len(self.weights[0])):
                t_weights[j][i] = self.weights[i][j]
        
        input_gradients = [[0] * len(gradient[0]) for _ in range(len(t_weights))]
        for i in range(len(t_weights)):
            for j in range(len(gradient[0])):
                for k in range(len(t_weights[0])):
                    input_gradients[i][j] += t_weights[i][k] * gradient[k][j]                
                    
        for i in range(len(self.weights)):
            for j in range(len(self.weights[0])):
                momentum_update = self.delta_weights[i][j] * momentum
                weight_update = weight_gradients[i][j] * eta
                self.weights[i][j] += weight_update + momentum_update
                self.delta_weights[i][j] = weight_update

        for i in range(len(self.biases)):
            for j in range(len(self.biases[0])):
                self.biases[i][j] += gradient[i][j] * eta

        return input_gradients
