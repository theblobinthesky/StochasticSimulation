import numpy as np
import numpy.random as rand
from typing import Callable
from numba import njit


@njit
def brute_force_deterministic(f: Callable[[int, int], int], N: int, num_dims_per_sample: int) -> float:
    if num_dims_per_sample == 1:
        sum = 0
        for i in range(N):
            sum += f(i)
    else:
        raise ValueError("Higher dimensional samples not supported.")

    return sum * 1.0 / N


# Known as: M_n^*
@njit
def simple_deterministic(f: Callable[[int, int], int], N: int, num_samples: int, num_dims_per_sample: int) -> float:
    if num_dims_per_sample == 1:
        sum = (N - num_samples) / 2.0
        for i in range(num_samples):
            sum += f(i)
    else:
        raise ValueError("Higher dimensional samples not supported.")

    return sum * 1.0 / N


# Known as: M_n
@njit
def naive_monte_carlo(f: Callable[[int, int], int], N: int, num_samples: int, num_dims_per_sample: int) -> float:
    rand_numbers = rand.randint(0, N, (num_samples, num_dims_per_sample))

    sum = 0
    for rand_num in rand_numbers:
        sum += f(*rand_num)

    return sum * 1.0 / num_samples


# Known as: M_n^tilde
@njit
def blocked_monte_carlo(f: Callable[[int, int], int], N: int, num_samples: int, num_dims_per_sample: int) -> float:
    assert N % num_samples == 0
    k = N // num_samples
    assert num_dims_per_sample == 1

    rand_numbers = rand.randint(0, k, (num_samples,))

    sum = 0
    for i, rand_num in enumerate(rand_numbers):
        sum += f(i * k + rand_num)

    return sum * 1.0 / num_samples

# Known as: M_{(c, n)}
@njit
def fancy_monte_carlo(f: Callable[[int, int], int], N: int, num_samples: int, num_dims_per_sample: int) -> float:
    assert N % num_samples == 0
    k = N // num_samples

    rand_numbers = rand.randint(0, N, (num_samples, num_dims_per_sample))
    sum = 0
    for rand_num in rand_numbers:
        sum += f(rand_num[0])

    n = num_samples 
    c = 1.0 / (n + np.sqrt(n * (N - n) / (N - 1)))
    return 0.5 + c * (sum - n * 0.5)

