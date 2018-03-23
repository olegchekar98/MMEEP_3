# Hiks

from scipy.optimize import minimize
from Settings import *


def objective(h):
    return p[0] * h[0] + p[1] * h[1] + p[2] * h[2] + p[3] * h[3]


def constraint1(h):
    return U(h[0], h[1], h[2], h[3]) - U(9, 12, 5, 5)


h0[0] = 8.0246413977
h0[1] = 11.0478955804
h0[2] = 6.59012155772
h0[3] = 4.32101956533

bnds = (
    (8, INF),
    (11, INF),
    (0, INF),
    (4, INF)
)

con1 = {'type': 'ineq', 'fun': constraint1}
cons = ([con1])
solution = minimize(objective, h0, method='SLSQP', bounds=bnds, constraints=cons)

h = solution.x

print('Final Objective: ' + str(objective(h)))

print('Solution')
for i in range(4):
    print('h{} = {}'.format(i + 1, h[i]))
print('U(h) = {}'.format(U(h[0], h[1], h[2], h[3])))

print("\nLagrange multiplier")
L = [p[i] / partial_derivative(U, i, h) for i in range(4)]
for i in range(4):
    print('L{} = {}'.format(i + 1, L[i]))
