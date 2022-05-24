import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use('dark_background')
col = ['red', 'green', 'blue']
SIR = [0, 1, 2]
graph, = plt.plot([], [], color=[])
fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(0, 1))
t = np.linspace(0,100,100)
y = np.zeros(100)
y = t
print(y,t)

plt.scatter(t,y,color=col)

plt.show()