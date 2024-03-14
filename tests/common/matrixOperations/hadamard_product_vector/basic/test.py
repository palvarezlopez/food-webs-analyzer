import sympy as sp
from common import matrixOperations as mo

# test A
matrixSA = sp.MatrixSymbol('X', 2, 2)
vectorSA = sp.MatrixSymbol('Y', 2, 1)

print("Symbolic original 2x2:")
sp.pprint(matrixSA)
sp.pprint(vectorSA)

print("hadamard_product_vector 2x2:")
sp.pprint(sp.Matrix(mo.hadamard_product_vector(matrixSA, vectorSA)))

# test B
matrixSB = sp.MatrixSymbol('X', 3, 3)
vectorSB = sp.MatrixSymbol('Y', 3, 1)

print("Symbolic original 3x3:")
sp.pprint(matrixSB)
sp.pprint(vectorSB)

print("hadamard_product_vector 3x3:")
sp.pprint(sp.Matrix(mo.hadamard_product_vector(matrixSB, vectorSB)))

# test C
matrixA = sp.Matrix(2, 2, [1, 2, 3, 4])
vectorA = sp.Matrix(2, 1, [5, 6])

print("Original 2x2:")
sp.pprint(matrixA)
sp.pprint(vectorA)

print("hadamard_product_vector 2x2:")
sp.pprint(sp.Matrix(mo.hadamard_product_vector(matrixA, vectorA)))

# test D
matrixB = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
vectorB = sp.Matrix(3, 1, [10, 11, 12])

print("Original 3x3:")
sp.pprint(matrixB)
sp.pprint(vectorB)

print("hadamard_product_vector 3x3:")
sp.pprint(sp.Matrix(mo.hadamard_product_vector(matrixB, vectorB)))