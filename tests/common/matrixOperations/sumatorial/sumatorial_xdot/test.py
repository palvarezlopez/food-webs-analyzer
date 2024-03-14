import sympy as sp
from common import matrixOperations as mo

matrixA = sp.Matrix([[1, 2], [3, 4]])
print (mo.sumatorial_xdot(matrixA))

matrixB = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print (mo.sumatorial_xdot(matrixB))