# Leapfrog, trajectory plot
import numpy as np
import matplotlib.pyplot as plt

h = 0.02  # timestep
N = 3 # how many periods
T = 2 * np.pi # the time period would be 2pi.
size = int(N *T /h) # the approx. time

q = 0.9
v0 = 1
Lz = 0.2
Energy = -0.8

R0 = 0.15
z0 = -0.09
ratio2 = 3
Rdot_sign = 1
zdot_sign = 1

x = np.zeros(size) # x position
y = np.zeros(size) # y position
vx = np.zeros(size) # velocity of x
vy = np.zeros(size) # velocity of y
r = np.zeros(size)
pr = np.zeros(size)
k = 0

## initial set
x[0] = R0 
y[0] = z0
Phi_eff = v0*v0/2*np.log(R0*R0 + z0*z0/q/q) + Lz*Lz/2/R0/R0
print(Phi_eff)
zdot2 = (Energy - Phi_eff)*2 / (ratio2+1)
vx[0] = Rdot_sign * np.sqrt( ratio2 * zdot2 )
vy[0] = zdot_sign * np.sqrt( zdot2 )

## calculate the particle trajectory for $N orbital periods 
for n in range(size-1):
    xmid = x[n] + h/2 * vx[n]  # middle x
    ymid = y[n] + h/2 * vy[n]  # middle y
    r2 = xmid *xmid + ymid *ymid # the square of r at middle
    vx[n+1] = vx[n] + h * ( Lz*Lz/(xmid*xmid*xmid) - v0*v0*xmid/(xmid*xmid+ymid*ymid/q/q) )
    vy[n+1] = vy[n] - h * ( v0*v0*ymid/(xmid*xmid*q*q+ymid*ymid))
    x[n+1] = xmid + h/2 * vx[n+1]
    y[n+1] = ymid + h/2 * vy[n+1]
    if y[n]<=0 and y[n+1]>0:
        r[k] = ( x[n]*y[n+1] - x[n+1]*y[n] ) / (y[n+1]-y[n])
        pr[k] = ( x[n+1] - x[n] )/h
        k = k + 1

r = r[0:k]
pr = pr[0:k]

import sys
class safesub(dict):
# """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

## plot the particle trajectory
plt.plot(x,y)
## plot information and save
plt.title(sub("orbit: start with R={R0}, z={z0}, k^2={ratio2}"))
plt.axis("equal")
plt.xlabel("R")
plt.ylabel("z")
plt.xlim(0, 0.5)
plt.ylim(-0.2, 0.2)
plt.grid( which="major", linewidth=0.5, color="0.75" )
plt.grid( which="minor", linewidth=0.25, color="0.75" )
plt.legend()
plt.tight_layout()
plt.savefig(sub("results/orbit_R{R0}z{z0}k{ratio2}.PNG"))
plt.clf()

## plot the surfaces of section
plt.scatter(r, pr)
plt.title(sub("surfaces of section: start with R={R0}, z={z0}, Rdot={Rdot0}"))
plt.axis("equal")
plt.xlabel("R")
plt.ylabel("$p_R$")
plt.ylim(-0.9, 0.9)
plt.xlim( 0, 0.5 )
plt.grid( which="major", linewidth=0.5, color="0.75" )
plt.grid( which="minor", linewidth=0.25, color="0.75" )
# plt.legend()
plt.tight_layout()
plt.savefig(sub("results/SoS_R{R0}z{z0}k{ratio2}.PNG"))
plt.clf()
