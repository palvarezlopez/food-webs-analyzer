import sympy as sp
from common import matrixOperations as mo

# test
matrix1 = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
matrix2 = sp.Matrix(3, 3, [1, 3, 3, 4, 2, 6, 5, 8, 9])

print("Original:")
sp.pprint(matrix1)
sp.pprint(matrix2)
print("comparing:")
sp.pprint(mo.equals(matrix1, matrix2))