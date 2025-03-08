import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


s = ctrl.TransferFunction.s
G = 2 / (s + 1)  
H = 1  
T = ctrl.feedback(G, H)  

Kv = ctrl.dcgain(s * G)  
ess = 1/Kv  

t = np.linspace(0, 10, 1000)  
ramp_input = t  

t, y = ctrl.forced_response(T, t, ramp_input)  
error_signal = ramp_input - y  

plt.figure() 

plt.subplot(1, 2, 1)
plt.plot(t, y)
plt.plot(t, ramp_input)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Unit ramp')
plt.legend()
plt.grid(True)


plt.subplot(1, 2, 2)
plt.plot(t, error_signal, 'r--')
plt.xlabel('Time (s)')
plt.ylabel('Error')
plt.title('Steady-State Error')
plt.grid(True)

plt.tight_layout()
plt.show()
