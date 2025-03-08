import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


s = ctrl.TransferFunction.s
G = 9.74 / (s * (s - 1.23))
H=1

T= ctrl.feedback(G, H)


t = np.linspace(0,20,1000)


t, y1 = ctrl.step_response(T, t) #step

t, y2 = ctrl.step_response(T / s, t) #ramp


plt.figure()
plt.plot(t, y1, 'b', label='Step Response')
plt.plot(t, y2, 'r', label='Ramp Response')

plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step and Ramp Response')
plt.legend()
plt.grid()
plt.show()
