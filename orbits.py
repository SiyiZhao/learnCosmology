import numpy as np
from numpy.core.function_base import linspace

q = 0.9
v0 = 1
Lz = 0.2
Energy = -0.8

R0 = 0.39
z0 = 0
Rdot0 = 0
zdot_sign = 1

step = 200
steptime = 0.02
R_l = np.zeros(step)
z_l = np.zeros(step)
Rdot = np.zeros(step)
zdot = np.zeros(step)

R_l[0] = R0
z_l[0] = z0
Rdot[0] = Rdot0
Phi_eff = v0*v0/2*np.log(R0*R0 + z0*z0/q/q) + Lz*Lz/2/R0/R0
zdot2 = (Energy - Phi_eff)*2 - Rdot0*Rdot0 
zdot[0] = zdot_sign * np.sqrt( zdot2 )

for i in range(step-1):
    R = R_l[i]
    z = z_l[i]
    Rddot = Lz*Lz/(R*R*R) - v0*v0*R/(R*R + z*z/q/q)
    zddot = - v0*v0*z / (R*R*q*q + z*z)
    R_l[i+1] = R + Rdot[i] * steptime
    z_l[i+1] = z + zdot[i] * steptime
    Rdot[i+1] = Rdot[i] + Rddot * steptime
    zdot[i+1] = zdot[i] + zddot * steptime
    # print(Rdot[i], end='  ')
    Energy = (zdot[i]*zdot[i] + Rdot[i]*Rdot[i])/2 + v0*v0/2*np.log(R0*R0 + z0*z0/q/q) + Lz*Lz/2/R0/R0
    print(Energy, end='\n')

import sys
class safesub(dict):
# """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

from matplotlib import pyplot as plt
plt.plot( R_l, z_l )
rr = linspace(0.2,0.5,50)
zz = np.sqrt( (rr*rr-0.04)*rr*rr /0.04*q*q )
plt.plot(rr, zz)
plt.plot(rr,-zz)
plt.title(sub("orbit: start with R={R0}, z={z0}, Rdot={Rdot0}"))
plt.xlabel("R")
plt.ylabel("z")
# plt.xlim(0, 0.5)
plt.ylim(-0.2, 0.2)
plt.grid( which="major", linewidth=0.5, color="0.75" )
plt.grid( which="minor", linewidth=0.25, color="0.75" )
plt.legend()
plt.tight_layout()
plt.savefig(sub("results/orbit_R{R0}z{z0}Rd{Rdot0}.PNG"))
