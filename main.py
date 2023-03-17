import numpy as np

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
from IPython import display


#Take Inputs
CFL = float(input("Enter CFL number: "))#0.5,1,1.2
nx = int(input("Enter number of grid points: "))#11,21,51,101
L = 1
T = 2#duration till which we want to see the simulation
deltaT = 0.01
deltaX = L/(nx-1) #Grid Spacing
nt = int(T/deltaT)#number of time steps
c = CFL*deltaX/deltaT
#Create the domain
x = np.linspace(0,1,nx)
#INITIAL CONDITION AND EXACT SOLUTION
u0 = np.sin(2*np.pi*x)
def u_exact(x,t):
    return np.sin(2*np.pi*(x-c*t))
#Creating an empty array to store u
u = np.empty((nt+1,nx))
u[0] = u0.copy()