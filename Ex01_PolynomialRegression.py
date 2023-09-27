# Exercise 01: Polynomial Regression
# ==================================

import random
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

random.seed(42)

# Defining the (hidden) functions to generate the data

def funcA(x):
    return 2*x

def funcB(x):
    return 2*x - 10*x**5 + 15*x**10

def getY(func, mu, sigma, x):
    return func(x) + random.gauss(mu, sigma)

# P is the number of (x, y) tuples
P = 10

# mu is the average value
# sigma is the noise strength
# we initialize both to zero
mu = 0
sigma = 0

# (2) generate 10 pairs of (x, y) with ZERO SIGMA and x in the range [0, 1]
x1 = np.array([random.uniform(0, 1) for i in range(P)]).reshape(-1, 1)
y1A = np.array([getY(funcA, mu, sigma, x) for x in x1]).reshape(-1, 1)
y1B = np.array([getY(funcB, mu, sigma, x) for x in x1]).reshape(-1, 1)

# (3) fit the data
poly1 = PolynomialFeatures(degree=1)
poly3 = PolynomialFeatures(degree=3)
poly10 = PolynomialFeatures(degree=10)

poly1_features = poly1.fit_transform(x1)

print(poly1_features, y1A)

#model1 = LinearRegression()
#model1.fit(poly1, y1A.reshape(-1, 1))
#
#print(model1.coef_)
