
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50))
line, = ax.plot([], [], lw=2)

# initialization function 
def init():
    # creating an empty plot/frame
    line.set_data([], [])
    return line,

# lists to store x and y axis points 
xdata, ydata = [1,2,3], [3,2,1]

# animation function 
def animate(i):

    line.set_data(xdata, ydata,'r')
    xdata[0] = xdata[0] + i
    xdata[1] = xdata[1] + i
    xdata[2] = xdata[2] + i

    ydata[0] = ydata[0] + i
    ydata[1] = ydata[1] + i
    ydata[2] = ydata[2] + i
    return line,


# setting a title for the plot

# hiding the axis details 
plt.axis('off')

# call the animator	 
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=500, interval=20, blit=True)

# save the animation as mp4 video file 
plt.show()