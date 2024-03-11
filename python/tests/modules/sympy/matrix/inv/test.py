import sympy as sp

# declare matrix
A = sp.Matrix([[1, 5, 3], [4, 5, 6], [2, 8, -3]])

# print
print("Original A:")
sp.pprint(A)
print("inv(A):")
sp.pprint(A.inv())

# declare symbolic matrix
X = sp.MatrixSymbol('X', 3, 3)

# print
print("Original X")
sp.pprint(X)
print("inv(X):")
sp.pprint(X.inv())

# declare non invertible matrix
B = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print
print("Original Non invertible B")
sp.pprint(B)
print("inv(B):")
sp.pprint(B.inv())