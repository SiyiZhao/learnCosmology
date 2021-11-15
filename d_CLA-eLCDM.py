# For a LambdaCDM universe with (0.28, 0.72), calculate and make a plot showing 
# d_C (line-of-sight comoving distance), d_L (luminosity distance), d_A (angular-diameter distance)
# comparing with those of an EdS universe.

import numpy as np
from astropy.cosmology import LambdaCDM
from matplotlib import pyplot as plt

zmax = 10
z = np.arange(0, zmax, 0.2)

## LambdaCDM universe
LCDM = LambdaCDM(H0=72, Om0=0.28, Ode0=0.72)
d_C = LCDM.comoving_distance(z).value #Mpc
d_L = d_C * ( 1 + z )
d_A = d_C / ( 1 + z )

## EdSuniverse
EdS = LambdaCDM(H0=72, Om0=1, Ode0=0)
d_C1 = EdS.comoving_distance(z).value #Mpc
d_L1 = d_C1 * ( 1 + z )
d_A1 = d_C1 / ( 1 + z )

## plot
color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e337c2', '#7f7f7f', '#bcbd22', '#17becf']
plt.yscale('log')
plt.plot( z, d_C, color=color[0], label='d_C, $\Lambda$CDM')
plt.plot( z, d_L, color=color[1], label='d_L, $\Lambda$CDM')
plt.plot( z, d_A, color=color[2], label='d_A, $\Lambda$CDM')
plt.plot( z, d_C1, linestyle="dashed", color=color[0], label='d_C, EdS')
plt.plot( z, d_L1, linestyle="dashed", color=color[1], label='d_L, EdS')
plt.plot( z, d_A1, linestyle="dashed", color=color[2], label='d_A, EdS')
plt.text(2.5, 1e5, "H0=72 km / (Mpc s)")
plt.title("distances-redshift")
plt.xlabel("z")
plt.ylabel("d [Mpc]")
plt.legend()
plt.tight_layout()
plt.savefig("results/d_CLA-z%d.PNG"%(zmax))