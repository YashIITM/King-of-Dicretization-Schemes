import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from main import *

def FTFS(u,CFL,deltaX,deltaT = 0.01):
    nx = len(u[0])
    nt = len(u)-1
    c = CFL*deltaX/deltaT
    for n in range(nt):
        for i in range(nx-1):
            u[n+1,i] = u[n,i] - (c*deltaT/deltaX)*(u[n,i+1]-u[n,i])
        #enforcing boundary conditions
        u[n+1,nx-1] = u[n,nx-1] - (c*deltaT/deltaX)*(u[n,1]-u[n,nx-1])
    return u
#Plot animation required
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2,label='Exact Solution')
line2, = ax.plot([], [], lw=2,label='Numerical Solution using FTFS')
def init():
   line.set_data([], [])
   line2.set_data([],[])
   return line,line2,
def animate(i):
   x = np.linspace(0, 1, nx)
   y = u_exact(x,deltaT * i)
   y2 = FTFS(u,CFL,deltaX,deltaT)
   line.set_data(x, y)
   line2.set_data(x,y2[i][:])
   return line,line2,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(2/0.01), interval=200, blit=True)
plt.legend(loc=1,prop={'size': 6})
plt.title("Numerical Solution using FTFS ")
plt.show()
