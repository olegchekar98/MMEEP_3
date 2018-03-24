import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, minimize
from Settings import INF


# CAPITAL
F = [10600, 10550, 10630, 10790, 10860, 10380, 10630, 10600, 10800, 10740]

# K
K = [25071, 25064, 25226, 25461, 25935, 24700, 25015, 25018, 25626, 25580]

# LABOR
L = [5070, 5000, 5000, 5150, 5260, 4950, 5015, 5020, 5170, 5159]


def cobb_douglas(x, a, b, c):
    return a * (x[0] ** b) * (x[1] ** c)


p0 = [3.155989, 0.68368306, 0.13993322]
coeffs, _ = curve_fit(cobb_douglas, (F, L) , K, p0)
print("Production function K = {} * F ^ {} * L ^ {}".format(coeffs[0], coeffs[1], coeffs[2]))

if abs(coeffs[1] + coeffs[2] - 1) < 1e-3:
    print('Constant returns to scale')
elif coeffs[1] + coeffs[2] > 1:
    print('Increasing returns to scale')
else:
    print('Decreasing returns to scale')

print('Elasticity of substitution for Cobb–Douglas production function is const = 1')


price = 70
w = [100, 100]


def pi(x):
    return w[0] * x[0] + w[1] * x[1] - price * cobb_douglas(x, coeffs[0], coeffs[1], coeffs[2])


bounds1 = (
    (0, INF),
    (0, INF)
)

long_solution = minimize(pi, [1, 1], method='SLSQP', bounds=bounds1, constraints=[])
print(long_solution.x)
print("Long run profit", -pi(long_solution.x))


def constraint1(x):  # sqrt(x[0] * x[0] + x[1] * x[1]) <= 5000
    return 5000 - (x[0] * x[0] + x[1] * x[1]) ** 0.5


con1 = {'type': 'ineq', 'fun': constraint1}

short_solution = minimize(pi, [1, 1], method='SLSQP', bounds=bounds1, constraints=[con1])
print(short_solution.x)
print("Short run profit", -pi(short_solution.x))


def price_func(x):
    return -x / 830 + 8310/83


def wL(x):
    return 0.025 * x[1] - 20


def wF(x):
    return 0.025 * x[0] - 10


def wM(x):
    return (wF(x), wL(x))


def monopoly_pi(x):
    q = cobb_douglas(x, coeffs[0], coeffs[1], coeffs[2])
    mw = wM(x)
    return mw[0] * x[0] + mw[1] * x[1] - price_func(q) * q


monopoly_solution = minimize(monopoly_pi, [1, 1], method='SLSQP', bounds=bounds1, constraints=[])
print(monopoly_solution.x)
print("Monopoly profit", -monopoly_pi(monopoly_solution.x))
print("Monopoly price", price_func(cobb_douglas(monopoly_solution.x, coeffs[0], coeffs[1], coeffs[2])))
print("Monopoly price of resources: F = {}, L = {}".format(wF(monopoly_solution.x), wL(monopoly_solution.x)))
print("Volume of production", cobb_douglas(monopoly_solution.x, coeffs[0], coeffs[1], coeffs[2]))

