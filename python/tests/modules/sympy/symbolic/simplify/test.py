import sympy as sp

# declare two symbols x and y
x = sp.Symbol('x')
y = sp.Symbol('y')

# declare function f(x,y) = (6x^2 + 3y^2 + 3x + 12x^2) / (2x + 1)
f = (6*x**2 + 3*y**2 + 3*x + 12*y**2) / (2*x + 2)

# print
sp.pprint(f)

print("------------------------------")

# simpifly function
f_simplified = sp.simplify(f)

# print
sp.pprint(f_simplified)