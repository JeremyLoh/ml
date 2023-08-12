# n-dimensional arrays are called tensors
# tensor class (ndarray in MXNet, Tensor in PyTorch and TensorFlow)
# resembles NumPy ndarray, but with some key features
# Tensor class supports automatic differentiation
# Tensor class leverages GPUs to accelerate numerical computation, whereas NumPy runs only on CPUs

import torch

# 2.1.1 Getting Started

# tensor represents a (possibly multidimensional) array of numerical values
# with one axis, a tensor is called a vector
# with two axes, a tensor is called a matrix
# with k > 2 axes, we drop the specialized names and just refer to the object as a k^th order tensor

# PyTorch has functions for creating new tensors prepopulated with values
# e.g. arange(n) creates a vector (one axis) of evenly spaced values,
#      starting at 0 (included) and ending at n (excluded), default interval size is 1
# Unless specified, new tensors are stored in main memory and designated for CPU based computation

x = torch.arange(12, dtype=torch.float32)
print(x)
# each value is an element of tensor
# we can check the total number of elements in a tensor via numel method
print("x number of elements in tensor using x.numel(): ", end="")
print(x.numel())

# we can access tensor's shape (length along each axis) by inspecting shape attribute
# for a vector, the shape contains one element and is identical to the size
print("x shape (length along each axis): ", end="")
print(x.shape)

# we can change the shape of a tensor without altering its size or values, by using reshape
# e.g. transform vector x whose shape is (12,) to a matrix X with shape (3, 4)
# the new tensor retains all elements but reconfigures them into a matrix
# the elements of our vector are laid out one row at a time and thus x[3] == X[0, 3]
X = x.reshape(3, 4)
print(X)
print(X.numel())

# specifying every shape component to reshape() is redundant because we already know our tensor's size
# we can work out one component of the shape when we give the rest
# e.g. given tensor of size n and target shape (h, w), we know that w = n / h
# to automatically infer one component of the shape,
# we can place -1 for the shape component that should be inferred automatically
# e.g. x.reshape(3, 4) can be x.reshape(-1, 4) or x.reshape(3, -1)

# practitioners often need to work with tensors initialized to all zeros or ones
# we can make a tensor with all elements set to zero with a shape of (2, 3, 4) with the zeros function
print(torch.zeros((2, 3, 4)))
print(torch.ones((2, 3, 4)))

# we often want to sample each element randomly (and independently) from a given probability distribution
# e.g. parameters of neural networks are often initialized randomly
# torch.randn(3, 4) creates a tensor with elements drawn from a standard Gaussian (normal) distribution with mean 0 and
# standard deviation 1
print(torch.randn((3, 4)))

# we can make tensors by supplying exact values for each element by supplying (possibly) nested python list(s)
# that have numerical literals
print(torch.tensor([[2, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]]))
