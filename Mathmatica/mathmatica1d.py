import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the rod
T = 1.0  # Total time
Nx = 100  # Number of spatial grid points
Nt = 1000  # Number of time steps
alpha = 0.01  # Thermal diffusivity

# Discretization
dx = L / (Nx - 1)
dt = T / Nt
x = np.linspace(0, L, Nx)
u = np.zeros(Nx)

# Initial condition (e.g., a Gaussian pulse)
u[:] = np.exp(-100 * (x - 0.5)**2)

# Time-stepping loop
for n in range(0, Nt):
    u[1:Nx-1] = u[1:Nx-1] + alpha * (u[2:Nx] - 2*u[1:Nx-1] + u[0:Nx-2]) * (dt / dx**2)

# Plot the solution
plt.plot(x, u)
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('1D Heat Equation')
plt.show()
