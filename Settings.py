import numpy as np
from scipy.misc import derivative

p = [20, 25, 10, 15]

n = 4
x0 = np.zeros(n)
h0 = np.zeros(n)

INF = 20000

I = 1000

def U(x1, x2, x3, x4):
    return 3.3 * (x1 - 8) ** 0.48 + 5.8 * (x2 - 11) ** 0.14 + 15.2 * x3 ** 0.64 + 9 * (x4 - 4) ** 0.43


def partial_derivative(func, var=0, point=[]):
    args = point[:]

    def wraps(x):
        args[var] = x
        return func(*args)

    return derivative(wraps, point[var], dx = 1e-6)