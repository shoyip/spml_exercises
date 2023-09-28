# Exercise 01: Polynomial Regression
# ==================================

from scipy.optimize import curve_fit
import numpy as np
import warnings

rng = np.random.default_rng()

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
print("=== (1-3) Generate paris and fit data")

x1 = rng.uniform(0, 1, 10)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for func_name, func in zip(['A', 'B'], [funcA, funcB]):
        print(f'\n--- Printing results for function {func_name}\n')
        
        y1 = getY(func, mu, sigma, x1)
        
        p1 = np.polynomial.Polynomial.fit(x1, y1, deg=1)
        p3 = np.polynomial.Polynomial.fit(x1, y1, deg=3)
        p10 = np.polynomial.Polynomial.fit(x1, y1, deg=10)
    
        print(p1, p3, p10, sep='\n\n')

print("\n=== (4) generate other 20 pairs\n")

x2 = rng.uniform(0, 1.25, 20)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for func_name, func in zip(['A', 'B'], [funcA, funcB]):
        print(f'\n--- Printing results for function {func_name}\n')
        
        y2 = getY(func, mu, sigma, x2)
        
        p1 = np.polynomial.Polynomial.fit(x2, y2, deg=1)
        p3 = np.polynomial.Polynomial.fit(x2, y2, deg=3)
        p10 = np.polynomial.Polynomial.fit(x2, y2, deg=10)
    
        print(p1, p3, p10, sep='\n\n')
