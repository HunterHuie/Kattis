import numpy as np
import matplotlib.pyplot as plt

# Parameters
Lx = 1.0  # Length of the domain in the x-direction
Ly = 1.0  # Length of the domain in the y-direction
T = 1.0  # Total time
Nx = 100  # Number of spatial grid points in the x-direction
Ny = 100  # Number of spatial grid points in the y-direction
Nt = 1000  # Number of time steps
alpha = 0.01  # Thermal diffusivity


# Discretization
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = T / Nt

# Create grids for x and y
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)

# Create an array to represent temperature at each grid point
u = np.zeros((Nx, Ny))

# Initial condition (e.g., a Gaussian pulse)
u[:,:] = np.exp(-100 * ((x[:, np.newaxis] - 0.5)**2 + (y - 0.5)**2))

# Time-stepping loop
for n in range(0, Nt):
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[i, j] = u[i, j] + alpha * ((u[i + 1, j] - 2 * u[i, j] + u[i - 1, j]) / dx**2 +
                                        (u[i, j + 1] - 2 * u[i, j] + u[i, j - 1]) / dy**2) * dt

# Plot the solution as a heatmap
plt.imshow(u, extent=[0, Lx, 0, Ly], origin='lower', cmap='hot', aspect='auto')
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Heat Equation')
plt.show()
