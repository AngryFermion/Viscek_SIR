import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
fig = plt.figure()
ax = plt.axes(xlim=(0,10), ylim=(0,1))
eta = [0,0.1,0.2,0.3,0.4,0.8,0.9,1.2,1.3,1.4,1.5,1.9,2.1,2.2,2.3,2.5,2.8,3.1,3.5,4,4.5,5,6,10]
v_a = [1,0.9923,0.99,0.9861,0.971,0.923,0.91,0.66,0.69,0.52,0.58,0.6,0.55,0.5,0.5,0.5,0.48,0.45,0.38,0.36,0.36,0.34,0.24,0.18]
plt.plot(eta,v_a,color='red')
plt.xlabel(r'$\eta$')
plt.ylabel(r'$v_{a}$')
plt.title(r'$\eta -vs- v_{a}$')
plt.show()