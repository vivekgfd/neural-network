# Basic Neural Network from Scratch

This repository contains a basic neural network implemented entirely from scratch in Python, without relying on external libraries such as NumPy or TensorFlow. The primary goal of this project is to provide an educational tool for understanding the fundamental concepts behind neural networks by building one step-by-step.

While this implementation may not be as efficient as those using specialized libraries, it serves as a valuable resource for learning and experimenting with neural networks at a low level.

---

## Features

### Core Functionality
- **Activation Functions**:
  - Supports **Sigmoid** and **ReLU** activations.
- **Learning Algorithm**:
  - Utilizes **Stochastic Gradient Descent (SGD)** for training.
- **Hyperparameter Customization**:
  - Allows users to set a custom learning rate (`eta`) and momentum.

### Example Use Case: Logical Operators
The repository includes an example where the network is trained to perform logical operations. The inputs provided to the network consist of 6 bytes:
- **First 4 bytes**: Represent the logical operator (e.g., AND, OR, XOR, NOR, etc.).
- **Last 2 bytes**: Represent the operands `p` and `q`.

The network's goal is to predict the output of the logical operation, which will always be either `0` or `1`. This example demonstrates how the network can learn and make predictions based on given inputs.

---

## File Structure

### Main Files
- **`neuralnetwork/__init__.py`**:
  Contains the core implementation of the neural network, including forward propagation, backpropagation, and weight updates.

- **`data.py`**:
  Defines the dataset for training and testing the network. The dataset includes samples representing logical operations and their expected outputs.

- **`example.py`**:
  Demonstrates how to train the neural network using the logical operators dataset and evaluate its predictions.

### Supporting Files
- **`README.md`**:
  Documentation for the project.
- **Other files**:
  Additional scripts or configurations may be included for testing or extending the functionality.

---

## How to Run the Neural Network

### Prerequisites
- Python 3.x installed on your system.

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   cd neural-network-main
   ```

2. Run the example script:
   ```bash
   python example.py
   ```

3. Observe the output:
   - The script trains the neural network on the logical operators dataset.
   - After training, it prints the expected and predicted outputs for each sample.

---

## Example Output

During training, the network will output the error (loss) for each epoch. After training, it will display predictions compared to the expected values. For example:

```
Epoch 1: Error = 0.25
Epoch 2: Error = 0.18
...
EXPECTED: [[1]], RESULT: [[0.98]]
EXPECTED: [[0]], RESULT: [[0.02]]
```

### How to Interpret the Output
- **EXPECTED**: The target output from the dataset.
- **RESULT**: The neural network's prediction.
- If `RESULT` is close to `EXPECTED`, the network is performing well.

---

## Customization

### Modify Hyperparameters
You can adjust the learning rate (`eta`) and momentum in the neural network implementation to experiment with different training behaviors.

### Extend the Dataset
The dataset in `data.py` can be modified to include additional logical operations or other types of inputs.

---

## Educational Value

This project is ideal for:
- Beginners looking to understand neural networks at a fundamental level.
- Developers interested in exploring how neural networks work without relying on external libraries.
- Educators seeking a simple example to teach neural network concepts.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as needed.

---

## Contributions

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to open an issue or submit a pull request.

---

## Contact

For questions or feedback, please reach out to [punjabivivek15@gmail.com].