import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction.s
G = 2 / (s + 1)  
H = 1  
T = ctrl.feedback(G, H)  

Kp = ctrl.dcgain(G)  
ess = 1 / (1 + Kp) 

t = np.linspace(0,10, 1000)
t, y = ctrl.step_response(T, t)  
r = np.ones_like(t)     # assume Unit step! (for step we have 2*np.ones_like(t))
error_signal = r - y  

#t2, y2= ctrl.step_response(G,t) open loop Response: G => open loop TF
plt.figure()

plt.subplot(2,1,1)
plt.plot(t, y)
plt.xlabel('Time(s)')
plt.ylabel('Output')
plt.title('Unit Step Response')
plt.grid(True) 
 
plt.subplot(2,1,2)
plt.plot(t, error_signal,'r')
plt.xlabel('Time (s)')
plt.ylabel('Error')
plt.title('Steady-State Error')
plt.grid(True)
plt.ylim([0.1, 1])  #to make error more visible

plt.tight_layout()
plt.show()