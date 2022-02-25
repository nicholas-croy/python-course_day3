# Program to multiply two matrices using nested loops
import random
import numpy as np

N = 250

# NxN matrix
#@profile
mat_X = (np.random.rand(N,N))*100
mat_X = mat_X.astype(int)


# Nx(N+1) matrix
#@profile
mat_Y = (np.random.rand(N,N+1))*100
mat_Y = mat_Y.astype(int)

# result is Nx(N+1)
@profile
def matmult(X,Y):
    result = np.matmul(X,Y)
    return result

matmult(mat_X,mat_Y)