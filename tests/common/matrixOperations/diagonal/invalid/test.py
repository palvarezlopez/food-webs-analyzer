import sympy as sp
from common import matrixOperations as mo

# declare squared matrix (invalid for diagonal)
matrix = sp.Matrix(2, 2, [1, 2, 3, 4])

# create a repeated matrix using repMat
print("Original:")
sp.pprint(matrix)
print("Diagonal:")
sp.pprint(mo.diagonal(matrix))