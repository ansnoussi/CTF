# sexy primes are prime numbers that differ from each other by six
# let's try to solve this equation: x*(x+6) = N

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
solve (x**2+6*x-N,x)
