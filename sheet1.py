import numpy as np
import numpy.random as rndm
from tabulate import tabulate

initial_seed = 1
num_items = 1024 * 1024
results = []

def test_exp_value(nums: np.ndarray) -> float:
    return np.abs(nums.mean() - 0.5)

def test_std_dev(nums: np.ndarray) -> float:
    return np.abs(nums.std() - 1 / np.sqrt(12.0))

def test_independence(nums: np.ndarray):
    pass

def test_strong_law_of_big_numbers(nums: np.ndarray):
    pass

def test_all(name: str, nums: np.ndarray):
    exp = test_exp_value(nums)
    std_dev = test_std_dev(nums)
    test_independence(nums)
    test_strong_law_of_big_numbers(nums)
    results.append([name, exp, std_dev])


# Make a bad PRNG for testing purposes:
def bad_rand(n, seed):
    def lcg(state):
        # glibc-style LCG: state = (a*state + c) mod 2**32
        return (1664525 * state + 1013904223) & 0xFFFFFFFF
    out = np.empty((n,), dtype=np.float64)
    s = seed
    for i in range(n):
        s = lcg(s)
        out[i] = s / 2**32
    return out

test_all("Mersenne Twister", rndm.Generator(rndm.MT19937(seed=initial_seed)).random((num_items,)))
test_all("Permuted congruential generator", rndm.Generator(rndm.PCG64(seed=initial_seed)).random((num_items,)))
test_all("Bad Linear Congruential Generator", bad_rand(num_items, initial_seed))

# compute mins/maxs for each error‐column
errs = list(zip(*results))[1:]
mins = [min(col) for col in errs]
maxs = [max(col) for col in errs]

# build and print table
table = []
for name, *vals in results:
    row = [name]
    for v, mn, mx in zip(vals, mins, maxs):
        row.append(f"{v:.1e}" + (" *" if v==mn else "") + (" †" if v==mx else ""))
    table.append(row)

print(tabulate(table, headers=["Generator","Independence","SLLN"], tablefmt="grid"))
