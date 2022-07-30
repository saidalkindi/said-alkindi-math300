
# Mathh300 Final project 

import numpy as np
import matplotlib.pyplot as plt 

# Parameters:
L = 10             # length of the rod 
nx = 51            # number of locations on the rod
dx = L / (nx - 1)  # distance between two locations
alpha = 0.25       # thermal diffusivity of the rod

# The locations along the rod.
x = np.linspace(0.0, L, num=nx)

# The initial temperature along the rod.
T0 = np.zeros(nx)
T0[0] = 300.0

def ftcs(T0, nt, dt, dx, alpha):
    T = T0.copy()
    sigma = alpha * dt / dx**2
    for n in range(nt):
        T[1:-1] = (T[1:-1] + sigma * (T[2:] - 2.0 * T[1:-1] + T[:-2]))
    return T

# The time-step size.
nt = 100  # number of time steps
sigma = 0.5
dt = sigma * dx**2 / alpha  # time-step size
T = ftcs(T0, nt, dt, dx, alpha) # The temperature along the rod
# Plot the temperature along the rod:
plt.figure(figsize=(8, 4))
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (C)')
plt.grid()
plt.plot(x, T,'b', linestyle='-', linewidth=2)
plt.xlim(0.0, L)
plt.ylim(0.0, 300.0);
plt.title('With a size of 100 time step')

# Increase the number of time steps.
nt = 1000
# Compute the temperature along the rod.
T = ftcs(T0, nt, dt, dx, alpha)
# Plot the temperature along the rod.
plt.figure(figsize=(8, 4))
plt.xlabel('Distance (m)')
plt.ylabel('Temperature (C)')
plt.grid()
plt.plot(x, T,'r', linestyle='-', linewidth=2)
plt.xlim(0.0, L)
plt.ylim(0.0, 300.0)
plt.title('With a size of 1000 time step')
