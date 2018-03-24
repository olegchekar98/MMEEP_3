import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# K
K = [10600, 10550, 10630, 10790, 10860, 10380, 10630, 10600, 10800, 10740]

# FUND
F = [25071, 25064, 25226, 25461, 25935, 24700, 25015, 25018, 25626, 25580]

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