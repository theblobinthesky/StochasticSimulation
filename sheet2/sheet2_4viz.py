import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

N = 10 ** 4
n = 10 ** 1
rand_nums = ((rand.randint(4, size=N) == 0).astype(np.int32)).reshape((100, 100))
plt.imshow(rand_nums)
plt.savefig("sheet2_4viz_function.png")


rand_numbers = rand.randint(0, N, size=n)
output = np.zeros((N,))
output[rand_numbers] = 1
plt.imshow(output.reshape((100, 100)))
plt.savefig("sheet2_4viz_uniform_distr.png")

k = N // n
rand_numbers = rand.randint(0, k, size=n)
output = np.zeros((N,))
output[np.arange(n) * k + rand_numbers] = 1
plt.imshow(output.reshape((100, 100)))
plt.savefig("sheet2_4viz_stratified.png")