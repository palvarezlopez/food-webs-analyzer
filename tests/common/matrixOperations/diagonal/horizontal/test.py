import sympy as sp
from common import matrixOperations as mo

# declare matrix
matrixA = sp.Matrix(1, 1, [0])
matrixB = sp.Matrix(1, 3, [1, 2, 3])
matrixC = sp.Matrix(1, 5, [4.1, 5.2, 6.3, 7.8, 8.9])

# create a repeated matrix using repMat
print("Original:")
sp.pprint(matrixA)
print("Diagonal:")
sp.pprint(mo.diagonal(matrixA))

print("---------------")

print("Original:")
sp.pprint(matrixB)
print("Diagonal:")
sp.pprint(mo.diagonal(matrixB))

print("---------------")

print("Original:")
sp.pprint(matrixC)
print("Diagonal:")
sp.pprint(mo.diagonal(matrixC))