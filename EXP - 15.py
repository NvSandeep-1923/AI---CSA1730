# Feed Forward Neural Network Implementation

import numpy as np

class FeedForwardNN:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Weights initialization
        self.W1 = np.random.randn(self.input_size, self.hidden_size)
        self.W2 = np.random.randn(self.hidden_size, self.output_size)
        
        # Bias initialization
        self.b1 = np.zeros((1, self.hidden_size))
        self.b2 = np.zeros((1, self.output_size))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def feedforward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2

# Example usage
if __name__ == "__main__":
    nn = FeedForwardNN(input_size=3, hidden_size=5, output_size=2)
    X = np.array([[0.1, 0.2, 0.3]])
    output = nn.feedforward(X)
    print(output)
