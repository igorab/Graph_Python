import math

from scipy import optimize
from sympy import *

#def f(x):
#    return 3.0 * ((x ** 2 - 1)**2)**0.5 - x**3


#result = optimize.minimize(f, 0)

#result.success  # check if solver was successful

#x_min = result.fun

#print(x_min)


x = symbols('x', real=True)
f = 3.0 * ((x ** 2 - 1)**2)**0.5 - x**3

zeros = solveset(f, x, domain=Interval(-2, 2))
assert zeros.is_FiniteSet # If there are infinite solutions the next line will hang.
ans = Min(f.subs(x, -2), f.subs(x, 2), *[f.subs(x, i) for i in zeros])


# print("Expression : {}".format(expr))
# Use sympy.limit() method
# limit_expr = limit(expr, x, "oo")
# print("Limit of the expression tends to 3 : {}".format(limit_expr))
