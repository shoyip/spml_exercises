# Exercise 01: Polynomial Regression
# ==================================

import numpy as np
import matplotlib.pyplot as plt
import warnings

rng = np.random.default_rng(42)

# Defining the (hidden) functions to generate the data

def funcA(x):
    return 2*x

def funcB(x):
    return 2*x - 10*x**5 + 15*x**10

def getY(func, mu, sigma, x):
    return func(x) + rng.normal(mu, sigma, len(x))

# P is the number of (x, y) tuples
P = 10

# mu is the average value
# sigma is the noise strength
# we initialize both to zero
mu = 0
sigma = 0

# (2) generate 10 pairs of (x, y) with ZERO SIGMA and x in the range [0, 1]
# (3) fit the data

def get_dataset(x_min, x_max, n_pairs, mu, sigma):
    x = rng.uniform(x_min, x_max, n_pairs)
    y_dict = {}

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        for func_name, func in zip(['A', 'B'], [funcA, funcB]):
            y = getY(func, mu, sigma, x)
            y_dict[func_name] = y

    return x, y_dict

def get_polyfunc(deg, func_name):
    x, ys = get_dataset(0, 1, 10, 0, 0)
    y = ys[func_name]
    p = np.polynomial.Polynomial.fit(x, y, deg=deg)
    coefs = p.convert().coef

    return coefs

def get_polyxy(x_min, x_max, deg, func_name):
    coefs = get_polyfunc(deg, func_name)
    x = np.linspace(x_min, x_max, 100)
    y = np.polynomial.polynomial.polyval(x, coefs, tensor=False)
    return (x, y)

x_t, ys_t = get_dataset(0, 1.25, 20, 0, 1)
x_c, y_c = get_polyxy(0, 1.25, 3, 'A')

for func_name in ['A', 'B']:
    plt.figure()
    plt.scatter(x_t, ys_t[func_name], s=3)
    for deg in [1, 3, 10]:
        x_c, y_c = get_polyxy(0, 1.25, deg, func_name)
        plt.plot(x_c, y_c, label=f'Order {deg}')
    plt.legend()
    plt.show()
    plt.close()
