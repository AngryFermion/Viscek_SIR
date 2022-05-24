import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
fig = plt.figure()
ax = plt.axes(xlim=(0,10), ylim=(0,0.07))
eta = [0,0.1,0.2,0.3,0.4,0.8,0.9,1.2,1.3,1.4,1.5,1.9,2.1,2.2,2.3,2.5,2.8,3.1,3.5,4,4.5,5,6,10]
var = [0.0007,0.006,0.001,0.00087,0.0005,0.00596,0.0056,0.05,0.04,0.05,0.05,0.05,0.05,0.06,0.04,0.05,0.048,0.046,0.037,0.02,0.03,0.02,0.011,0.008]
plt.plot(eta,var,color='red')
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\sigma$')
plt.title(r'$\eta -vs- \sigma$')
plt.show()