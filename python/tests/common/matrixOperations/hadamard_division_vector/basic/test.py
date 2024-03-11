import sympy as sp
from common import matrixOperations as mo

# test 1
matrixA1 = sp.MatrixSymbol('X', 3, 3)
matrixA2 = sp.MatrixSymbol('Y', 3, 1)

print("Original:")
sp.pprint(matrixA1)
sp.pprint(matrixA2)
print("hadamard_division_vector:")
sp.pprint(sp.Matrix(mo.hadamard_division_vector(matrixA1, matrixA2)))

print("---------------")

# test 2
matrixB1 = sp.Matrix(1, 1, [2])
matrixB2 = sp.Matrix(1, 1, [3])

print("Original:")
sp.pprint(matrixB1)
sp.pprint(matrixB2)
print("hadamard_division_vector:")
sp.pprint(mo.hadamard_division_vector(matrixB1, matrixB2))

print("---------------")

# test 3
matrixC1 = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
matrixC2 = sp.Matrix(3, 1, [11, 12, 13])

print("Original:")
sp.pprint(matrixC1)
sp.pprint(matrixC2)
print("hadamard_division_vector:")
sp.pprint(mo.hadamard_division_vector(matrixC1, matrixC2))