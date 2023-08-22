from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

def equation(t, y, mu):
    dydt = [y[1], mu * (1-y[0]**2) * y[1] - y[0]]
    return dydt
    

initial_conditions = [1.0]
time_span = (0, 5)


soultion = solve_ivp(equation, time_span, initial_conditions, t_eval=np.linspace(0, 5, 100))


plt.plot(soultion.t, soultion.y[0])
plt.xlabel('Time')
plt.ylabel('y')
plt.title('Solution of the Differential Equation')
plt.show()