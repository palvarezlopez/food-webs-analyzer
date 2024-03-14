import sympy as sp

# declare two matrices
A = sp.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = sp.Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
C = sp.Matrix([[19, 20, 21]])
D = sp.Matrix([[22], [23], [24]])

# print multiplication
print("Original A, B:")
sp.pprint(A)
sp.pprint(B)
print("A*B:")
sp.pprint(A * B)

# declare symbolic matrix
X = sp.MatrixSymbol('X', 3, 3)
Y = sp.MatrixSymbol('Y', 3, 3)

# multiply
C = sp.Matrix(X * Y)

# print symbolic multiplication
print("Original X, Y:")
sp.pprint(X)
sp.pprint(Y)
print("X*Y:")
sp.pprint(C)

# subs values
C = C.subs({X: A, Y:B})

# print
print("X(A)*Y(B):")
sp.pprint(C)

# show different multiplications
print("Original C, A:")
sp.pprint(C)
sp.pprint(A)
print("C*A")
sp.pprint(C*A)

print("Original A, D:")
sp.pprint(A)
sp.pprint(D)
print("A*D:")
sp.pprint(A*D)

print("Original C, D:")
sp.pprint(C)
sp.pprint(D)
print("C*D:")
sp.pprint(C*D)
