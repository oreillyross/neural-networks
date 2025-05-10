import numpy as np 

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0] ])

np.random.seed(0)
input_size = 2
hidden_size = 2
output_size = 1



