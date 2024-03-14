import sympy as sp
from common import matrixOperations as mo

# test 1
matrixA1 = sp.MatrixSymbol('X', 3, 3)
matrixA2 = sp.MatrixSymbol('Y', 3, 3)

print("Original:")
sp.pprint(matrixA1)
sp.pprint(matrixA2)
print("Add:")
sp.pprint(sp.Matrix(mo.add(matrixA1, matrixA2)))

print("---------------")

# test 2
matrixB1 = sp.Matrix(1, 1, [2])
matrixB2 = sp.Matrix(1, 1, [3])

print("Original:")
sp.pprint(matrixB1)
sp.pprint(matrixB2)
print("Add:")
sp.pprint(mo.add(matrixB1, matrixB2))

print("---------------")

# test 3
matrixC1 = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
matrixC2 = sp.Matrix(3, 3, [11, 12, 13, 14, 15, 16, 17, 18, 19])

print("Original:")
sp.pprint(matrixC1)
sp.pprint(matrixC2)
print("Add:")
sp.pprint(mo.add(matrixC1, matrixC2))