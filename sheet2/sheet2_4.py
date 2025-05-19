import numpy as np
import numpy.random as rand
import counting_problem as c
from typing import List
from numba import njit
from tqdm import tqdm
from tabulate import tabulate


def test_all_on_random_f(algos: List, N: int, n: int, repeats: int):
    gts = []
    approxs = [[] for _ in range(len(algos))]

    rand_nums = (rand.randint(4, size=N) == 0).astype(np.int32)
    for _ in tqdm(range(repeats), desc="Calculating gt. and approx. across random problem instances"):

        # Compute the ground truth result.
        @njit
        def f(i: int) -> int:
            return rand_nums[i]
        gt = c.brute_force_deterministic(f, N)
        gts.append(gt)

        # Compute the approximation algorithms.
        for i, (_, algo_f) in enumerate(algos):
            approx = algo_f(f, N, n, 1)
            approxs[i].append(approx)

    gts = np.asarray(gts)
    approxs = [np.asarray(a) for a in approxs]

    # RMSE per algorithm
    rmses = [np.sqrt(np.mean((a - gts) ** 2)) for a in approxs]

    # who’s best each trial?
    errs = np.vstack([np.abs(a - gts) for a in approxs])        # (k, repeats)
    winners = np.argmin(errs, axis=0)                           # index of best algo per trial
    best_props = np.bincount(winners, minlength=len(algos)) / repeats

    mean_gt = np.mean(gts)
    mean_approx = [np.mean(np.abs(a - gts)) for a in approxs]

    # build table rows, starting with ground truth
    rows = [
        ("Ground truth", "0", f"{mean_gt:.4g}", "-")
    ] + [
        (name,
         f"{rmse:.4g}",
         f"{mae:.4g}",
         f"{prop:.2%}")
        for (name, _), rmse, mae, prop
        in zip(algos, rmses, mean_approx, best_props)
    ]

    print()
    print(f"{N=}, {n=}, {repeats=}")
    print(tabulate(rows, headers=["Algorithm", "RMSE", "Result", "Best %"]))
    print()


algos = [
    ("Deterministic", c.simple_deterministic),
    ("Naive MC", c.naive_monte_carlo),
    ("Blocked MC", c.blocked_monte_carlo),
    ("Fancy MC", c.fancy_monte_carlo)
]

N = 10 ** 8
repeats = 100
test_all_on_random_f(algos, N, 10 ** 2, repeats)
test_all_on_random_f(algos, N, 10 ** 3, repeats)
test_all_on_random_f(algos, N, 10 ** 4, repeats)
test_all_on_random_f(algos, N, 10 ** 5, repeats)
