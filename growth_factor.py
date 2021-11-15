# we calculate the linear growth factor as a function of redshift.
# this code is  from a translation of the C++ code in the ESMRbHII/cosmotool
# see the result as a plot

import numpy as np
from matplotlib import pyplot as plt

# zmax = 20
# zp1 = np.arange(1, zmax+1, 0.2)

zp1 = np.array( [ 7, 15, 1100 ] )

h = 0.7
# H0 = h*100/3.08568e19  #unit:s^-1
# omeganu = 0
# omegab = 0.046
omega0 = 0.28
lambda0 = 0.72
om0hh = omega0*h*h
# ombhh = omegab*h*h
thetaCMB = 2.726/2.7

zEquality = 2.50e4*om0hh / thetaCMB**4 - 1.0

omZ = omega0* zp1**3 / (omega0* zp1**3+ lambda0 + (1-omega0-lambda0)*zp1**2)
lamZ = lambda0/(lambda0 + omega0* zp1**3 + ((1 - omega0 - lambda0)* zp1**2))

D1 = (1.0 + zEquality)/zp1*5.0*omZ/2.0 / ( omZ**(4/7) - lamZ + (1.0+omZ/2.0)*(1.0+lamZ/70.0) )
D2 = (1.0 + zEquality)*5.0/2.0*omega0 / ( omega0**(4/7) - lambda0 + (1.0+omega0/2.0)*(1.0+lambda0/70.0) )
Dz = D1/D2

print(Dz)

# ## plot
# # plt.yscale('log')
# plt.plot( zp1, Dz, label='linear growth factor')
# plt.title("the linear growth factor-redshift")
# plt.xlabel("z+1")
# plt.ylabel("D(z)")
# plt.legend()
# plt.tight_layout()
# plt.savefig("results/growth_f-z%d.PNG"%(zmax))

