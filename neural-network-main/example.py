import data
from neuralnetwork.neuralnetwork import NeuralNetwork

if __name__ == "__main__":
    nn = NeuralNetwork(inputs=6, eta=0.05, momentum=0.9)
    nn.add_relu_layer(16)
    nn.add_relu_layer(8)
    nn.add_sigmoid_layer(1)
    nn.train(data.samples, data.targets, 1000)

    for result, target in nn.predict(data.samples, data.targets):
        print(f"EXPECTED: {target}, RESULT: {result}") 
