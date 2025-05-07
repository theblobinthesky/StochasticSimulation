import numpy as np, math
import numpy.random as rndm
from tabulate import tabulate

initial_seed = 1
num_items = 1024 * 1024
results = []

def test_exp_value(nums: np.ndarray) -> float:
    # Strong law of big numbers.
    return np.abs(nums.mean() - 0.5)

def test_std_dev(nums: np.ndarray) -> float:
    return np.abs(nums.std() - 1 / np.sqrt(12.0))

def test_cond_prob(nums: np.ndarray):
    probs = nums[np.roll(nums, -1) >= 0.5]
    prob = (probs <= 0.5).sum() / probs.size
    return np.abs(prob - 0.5)

def test_all_bins_hit(nums: np.ndarray) -> float:
    n = nums.size
    # approximate solution of m·ln(m)=n via m ≈ n/(ln(n)−ln ln(n))
    m = int(n / (math.log(n) - math.log(math.log(n))))
    idx = np.minimum((nums * m).astype(int), m - 1)
    counts = np.bincount(idx, minlength=m)
    return np.mean(counts == 0)

def test_all(name: str, nums: np.ndarray):
    exp = test_exp_value(nums)
    std_dev = test_std_dev(nums)
    cond_prob = test_cond_prob(nums)
    empty_bins_fraction = test_all_bins_hit(nums)

    results.append([name, exp, std_dev, cond_prob, empty_bins_fraction])


def lcg(a, c, mask, n, seed):
    def lcg(state):
        return (a * state + c) & mask
    out = np.empty((n,), dtype=np.float64)
    s = seed
    denom = mask + 1 # 2**k
    for i in range(n):
        s = lcg(s)
        out[i] = s / denom
    return out

test_all("Mersenne Twister", rndm.Generator(rndm.MT19937(seed=initial_seed)).random((num_items,)))
test_all("Permuted congruential generator", rndm.Generator(rndm.PCG64(seed=initial_seed)).random((num_items,)))
test_all("GLIBC LCG", lcg(1664525, 1013904223, 0xFFFFFFFF, num_items, initial_seed))
# test_all("Broken LCG", lcg(2000000, 1000000000, 0xFFFFFFFF, num_items, initial_seed))
test_all("IBM RANDU", lcg(65539, 0, 2 ** 31 - 1, num_items, initial_seed))

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

print(tabulate(table, headers=["Name", "|E[X] - 0.5|", "|Var[X] - 1.0 / sqrt(12)|", "|P[X_i >= 0.5 | X_{i-1} <= 0.5] - 0.5|", "Empty Bins Fraction Where Exp. is 0"], tablefmt="grid"))
