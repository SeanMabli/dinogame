import numpy as np

def Sigmoid(Input):
    return 1 / (1 + np.exp(-Input))

class NEAT:
  def __init__(self, InSize, OutSize, MutationRate, PopulationSize):
    self.Weights = np.random.uniform(-1, 1, (PopulationSize, InSize, OutSize, ))
    # self.Biases = np.random.uniform(0, 0, (PopulationSize, OutSize))
    self.MutationRate, self.PopulationSize = MutationRate, PopulationSize
    
  def ForwardProp(self, In):
    self.In = np.array([In] * self.PopulationSize)
    print(self.In.shape)
    print(self.Weights.shape)
    self.Out = np.transpose(self.Weights, axes=0) @ self.In # + self.Biases
    print(self.Out.shape)
    return Sigmoid(self.Out)

  def Mutate(self, FavorableWeights, FavorableBiases):
    # Copy Weights and Biases
    self.Weights = FavorableWeights
    self.Biases = FavorableBiases

    # Mutate Weights & Biases
    self.Weights += np.random.uniform(-1, 1, self.Weights.shape) * np.random.choice([0, 1], self.Weights.shape, p=[1 - self.MutationRate, self.MutationRate])
    self.Biases += np.random.uniform(-1, 1, self.Biases.shape) * np.random.choice([0, 1], self.Biases.shape, p=[1 - self.MutationRate, self.MutationRate])