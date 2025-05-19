import math
from counting_problem import naive_monte_carlo

N = 10 ** 10
n = 1024
f = lambda i, j: math.gcd(i, j) == 1

print(naive_monte_carlo(f, N, n, 2))

