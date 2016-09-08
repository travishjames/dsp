# Matrix Algebra

import numpy as np

A = np.matrix([[1, 2, 3], [2, 7, 4]])
B = np.matrix([[1, -1], [0, 1]])
C = np.matrix([[5, -1], [9, 1], [6, 0]])
D = np.matrix([[3, -2, -1], [1, 2, 3]])
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([[1], [8], [0], [5]])

#1. Matrix Dimensions

print(A.shape)
#(2, 3)
print(B.shape)
#(2, 2)
print(C.shape)
#(3, 2)
print(D.shape)
#(2, 3)
print(u.shape)
#(4,) (1x4 vector)
print(w.shape)
#(4, 1)

#2.Vector Operations

print(np.add(u, v))
#[ 9  7 -4  9]
print(np.subtract(u,v))
#[ 3 -3 -2  1]
alpha = 6
print(np.multiply(alpha, u))
#[ 36  12 -18  30]
print(np.dot(u,v))
#51
print(np.linalg.norm(u))
#8.60232526704

#3. Matrix Operations

#print(np.add(A,C)) not defined
print(np.subtract(A,C.transpose()))
#[[-4 -7 -3]
# [ 3  6  4]]
print(np.add(C.transpose(), np.multiply(3,D)))
#[[14  3  3]
# [ 2  7  9]]
print(np.dot(B,A))
#[[-1 -5 -1]
# [ 2  7  4]]
#print(np.dot(B,A.transpose())) not defined
#print(np.dot(B,C)) not defined
print(np.dot(C,B))
#[[ 5 -6]
# [ 9 -8]
# [ 6 -6]]
print(np.linalg.matrix_power(B,4))
#[[ 1 -4]
# [ 0  1]]
print(np.dot(A,A.transpose()))
#[[14 28]
# [28 69]]
print(np.dot(D.transpose(),D))
#[[10 -4  0]
# [-4  8  8]
# [ 0  8 10]]
