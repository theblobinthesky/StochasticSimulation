Results for question `3)`:
<pre>
n=   100: est=0.580000, theo=0.607927, error=0.027927
n=  1000: est=0.597000, theo=0.607927, error=0.010927
n= 10000: est=0.608600, theo=0.607927, error=0.000673
n=100000: est=0.609730, theo=0.607927, error=0.001803
</pre>


Results for question `4)`:

<pre>
Calculating gt. and approx. across random problem instances: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:30<00:00,  3.23it/s]

N=100000000, n=100, repeats=100
Algorithm           RMSE     Result  Best %
-------------  ---------  ---------  --------
Ground truth   0          0.5        -
Deterministic  1.441e-05  1.441e-05  100.00%
Naive MC       0.04811    0.0379     0.00%
Blocked MC     0.05322    0.0436     0.00%
Fancy MC       0.04498    0.03473    0.00%

Calculating gt. and approx. across random problem instances: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:31<00:00,  3.16it/s]

N=100000000, n=1000, repeats=100
Algorithm           RMSE     Result  Best %
-------------  ---------  ---------  --------
Ground truth   0          0.5        -
Deterministic  1.797e-05  1.797e-05  100.00%
Naive MC       0.01836    0.01418    0.00%
Blocked MC     0.01513    0.01143    0.00%
Fancy MC       0.01483    0.01127    0.00%

Calculating gt. and approx. across random problem instances: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:30<00:00,  3.33it/s]

N=100000000, n=10000, repeats=100
Algorithm          RMSE    Result  Best %
-------------  --------  --------  --------
Ground truth   0         0.5       -
Deterministic  4.16e-06  4.16e-06  98.00%
Naive MC       0.005197  0.004182  0.00%
Blocked MC     0.004422  0.003369  2.00%
Fancy MC       0.005316  0.004165  0.00%

Calculating gt. and approx. across random problem instances: 100%|█████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:31<00:00,  3.13it/s]

N=100000000, n=100000, repeats=100
Algorithm           RMSE     Result  Best %
-------------  ---------  ---------  --------
Ground truth   0          0.4999     -
Deterministic  0.0001007  0.0001007  89.00%
Naive MC       0.001566   0.001236   6.00%
Blocked MC     0.001601   0.001345   0.00%
Fancy MC       0.001649   0.001308   5.00%
</pre>