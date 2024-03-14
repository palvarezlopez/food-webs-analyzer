import sympy as sp

# declare two symbols
x = sp.Symbol('x')
y = sp.Symbol('y')

# declare function f(x, y) = x^2 + y^2
f = x**2+y**2

# print
sp.pprint(f)

print("------------------------------")

# evaluate with 20 digits of precission (expected result = 13)
sp.pprint(f.evalf(20, subs={x:2, y:3}))