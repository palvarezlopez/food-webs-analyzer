import sympy as sp

# declare sympy symbols
x, y = sp.symbols('x,y', real=True)

# declare funtion f1(x, y) = -y
f1 = x*y

# print
print("f1(x,y):")
sp.pprint(f1)

# declare function f2(x, y) = x - 3x(1-x^2)
f2 = y

# print
print("f2(x,y):")
sp.pprint(f2)

# declare a matrix with both functions
F = sp.Matrix([f1,f2])

# print
print("F(x,y):")
sp.pprint(F)

# calculate jacobian
J = F.jacobian([x,y])

# print
print("J(x,y):")
sp.pprint(J)

# evaluate jacobian in 0, 0
J_ev = J.subs([(x,0), (y,0)])

# print
print("J(0,0):")
sp.pprint(J_ev)
