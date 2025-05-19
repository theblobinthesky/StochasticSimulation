import numpy as np
from math import pi
from tqdm import tqdm

def estimate_coprime_fraction(k: int, n: int) -> float:
    a = np.random.randint(1, k+1, size=n)
    b = np.random.randint(1, k+1, size=n)
    return np.mean(np.gcd(a, b) == 1)

k = 10**10
theoretical = 6 / pi**2

for n in [10**2, 10**3, 10**4, 10**5]:
    mean_est = estimate_coprime_fraction(k, n)
    abs_error = np.abs(mean_est - theoretical)
    print(f"n={n:>6}: est={mean_est:.6f}, theo={theoretical:.6f}, error={abs_error:.6f}")
