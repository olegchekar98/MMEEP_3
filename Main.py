# marshall

from Settings import *
from scipy.optimize import minimize


def objective(x):
    return - U(x[0], x[1], x[2], x[3])


def constraint1(x):
    return I - x[0] * p[0] - x[1] * p[1] - x[2] * p[2] - x[3] * p[3]


x0[0] = 8.542182111332473
x0[1] = 11.002924221720034
x0[2] = 48.75634535455467
x0[3] = 4.434653245650891

bnds = (
    (8, INF),
    (11, INF),
    (0, INF),
    (4, INF)
)

con1 = {'type': 'ineq', 'fun': constraint1}
cons = ([con1])
solution = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

x = solution.x

print('Final Objective: ' + str(-objective(x)))

print('\nSolution')
for i in range(4):
    print('x{} = {}'.format(i + 1, x[i]))

print("\nLagrange multiplier")
L = [partial_derivative(U, i, x) / p[i] for i in range(4)]
for i in range(4):
    print('L{} = {}'.format(i + 1, L[i]))
