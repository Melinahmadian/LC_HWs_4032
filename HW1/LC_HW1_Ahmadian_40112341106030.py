import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
t = np.linspace(0, 5, int(5 / dt))
N = len(t)

M_alpha, M_q, M_deltaE = -8.790, -2.075, -11.87
delta_E_values = [-5, 0, 10]

theta_0, theta_dot_0 = 0, 0

responses = {}

for delta_E in delta_E_values:
    theta = np.zeros(N)
    theta_dot = np.zeros(N)
    
    theta[0], theta_dot[0] = theta_0, theta_dot_0
    
    for i in range(N - 1):
        theta_doubledot = M_alpha * theta[i] + M_q * theta_dot[i] + M_deltaE * delta_E
        theta_dot[i + 1] = theta_dot[i] + theta_doubledot * dt
        theta[i + 1] = theta[i] + theta_dot[i + 1] * dt  

    responses[delta_E] = theta

plt.figure()
for delta_E, theta in responses.items():
    plt.plot(t, theta, label=f'δE = {delta_E}°')

plt.xlabel('Time (s)')
plt.ylabel('Theta (rad)')
plt.title('System Response for Different δE Values')
plt.legend()
plt.grid()
plt.show()
