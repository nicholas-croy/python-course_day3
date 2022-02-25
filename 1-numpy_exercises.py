# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 16:40:48 2022

@author: niccr151
"""

import numpy as np

#1-a
a = np.zeros(10)
a[4] = 1

#1-b
b = np.arange(10,50)

#1-c
c = np.flip(b)

#1-d
d = np.arange(0,9).reshape([3,3])

#1-e
e = np.array([1,2,0,0,4,0])
e_ind = np.where(e != 0)

#1-f
f = np.random.rand(30)
f_mean = np.mean(f)

#1-g
x = 8
y = 8
g = np.zeros([x,y])
g[0,:] = 1
g[:,0] = 1
g[x-1,:] = 1
g[:,y-1] = 1

#1-h
h = np.zeros([8,8])
h[1::2, ::2] = 1
h[::2, 1::2] = 1

#1-i
i = np.array([[0,1],[1,0]])
i_tile = np.tile(i, [4,4])

#1-j
j = np.arange(11)
for i in j:
    if 9>i>3:
        j[i] = -1*i
print(j)

#1-k
k = np.random.random(10)
k.sort()
print(k)

#1-l
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = A == B
print("A =" + str(A))
print("B =" + str(B))
print(equal)

#1-m
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = Z.astype(dtype=np.float32, copy=False)
print(Z.dtype)

#1-n
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diag(np.dot(A,B))
print(D)

