import sympy as sp
from common import matrixOperations as mo

# test
matrix = sp.Matrix(3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
vector = sp.Matrix(2, 1, [10, 11])

print("Original:")
sp.pprint(matrix)
sp.pprint(vector)

print("hadamard_product_vector (invalid):")
sp.pprint(sp.Matrix(mo.hadamard_product_vector(matrix, vector)))