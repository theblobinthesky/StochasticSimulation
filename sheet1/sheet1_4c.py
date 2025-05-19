import numpy as np
import numpy.random as rndm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
initial_seed = 1
pair_sample = 5_000  # sample size for clarity

def lcg(a, c, mask, n, seed):
    def lcg(state):
        return (a * state + c) & mask
    out = np.empty(n, dtype=np.float64)
    s = seed
    denom = mask + 1
    for i in range(n):
        s = lcg(s)
        out[i] = s / denom
    return out

# Generate sequences
seqs = {
    "Mersenne Twister": rndm.Generator(rndm.MT19937(seed=initial_seed)).random(pair_sample),
    "PCG64":            rndm.Generator(rndm.PCG64(seed=initial_seed)).random(pair_sample),
    "glibc LCG":        lcg(1664525, 1013904223, 0xFFFFFFFF, pair_sample, initial_seed),
    "Broken LCG":       lcg(2_000_000, 1_000_000_000, 0xFFFFFFFF, pair_sample, initial_seed),
    "IBM RANDU":        lcg(65539, 0, 2**31 - 1, pair_sample, initial_seed),
}

# 2D lag-1 scatter plots (one row per PRNG)
fig, axes = plt.subplots(len(seqs), 1, figsize=(6, 3 * len(seqs)))
for ax, (name, s) in zip(axes, seqs.items()):
    ax.scatter(s[:-1], s[1:], s=5, alpha=0.5)
    ax.set_title(f"{name} — lag 1")
    ax.set_xlabel("$x_i$")
    ax.set_ylabel("$x_{i+1}$")
plt.tight_layout()
plt.savefig("sheet1_4c_2dplot.png")
plt.show()

# Separate 3D triplet plot for IBM RANDU
fig = plt.figure(figsize=(6, 6))
ax3d = fig.add_subplot(111, projection="3d")
r = seqs["IBM RANDU"]
ax3d.scatter(r[:-2], r[1:-1], r[2:], s=5, alpha=0.5)
ax3d.set_title("IBM RANDU — triplets")
ax3d.set_xlabel("$x_i$")
ax3d.set_ylabel("$x_{i+1}$")
ax3d.set_zlabel("$x_{i+2}$")
ax3d.view_init(elev=10, azim=55)
plt.tight_layout()
plt.savefig("sheet1_4c_3dplot.png")
plt.show()
