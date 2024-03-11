import sympy as sp
from common import matrixOperations as mo

# test
matrix1 = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
matrix2 = sp.Matrix(3, 3, [11, 0, 13, 14, 15, 16, 17, 18, 19])

print("Original:")
sp.pprint(matrix1)
sp.pprint(matrix2)
print("Hadamard_division (alternative):")
sp.pprint(mo.hadamard_division(matrix1, matrix2, 0.1))