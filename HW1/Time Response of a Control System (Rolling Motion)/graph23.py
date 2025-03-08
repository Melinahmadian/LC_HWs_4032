import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


Lp = 1.23
LdeltaA = 9.74 


s = ctrl.TransferFunction.s
G = LdeltaA / (s * (s - Lp))
t = np.linspace(0, 1, 100)


t, y = ctrl.step_response(G, t)
unit_step = np.ones_like(t)  

plt.figure()
plt.plot(t, y, label=r'$\phi$') 
plt.plot(t, unit_step, 'k', label=r'$\delta_A$')
plt.xlabel('time')
plt.ylabel('output')
plt.title('Unit-step Response')
plt.legend(loc='best')
plt.grid()
plt.show()