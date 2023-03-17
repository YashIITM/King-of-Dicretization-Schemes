import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from main import *

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)

def init():
   line.set_data([], [])
   return line,

def animate(i):
   x = np.linspace(0, 1, nx)
   y = u_exact(x,deltaT * i)
   line.set_data(x, y)
   return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=int(2/0.01), interval=200, blit=True)
plt.show()