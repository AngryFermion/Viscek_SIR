# Updated on 13/05/2020
# Time : 23:05
# Update made : PBC working but bot the animation 
import numpy as np
import matplotlib.animation as animation
import cmath
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
# SYSTEM GENERAL VARIABLES
L = 7;  # length of the lattice
N = 300;  # No. Of particles
eta = 2;  # Noise
dt = 1;  # time-step
maxtime = 50;  # maximum run time
# VARIABLES
v_0 = 0.03;  # initial velocity = 0.03 according to viscek paper
dtheta = np.random.uniform(-eta / 2, eta / 2, size=N)  # fluctuation in angle
theta0 = np.random.uniform(-np.pi, np.pi, size=N)  # initial direction for each particle
x_0 = np.random.uniform(0, L, size=N)
y_0 = np.random.uniform(0, L, size=N)
r = np.zeros((N, maxtime))
x = np.zeros((N, maxtime))  # all particle x-position
y = np.zeros((N, maxtime))  # all particle y-position
vx = np.zeros((N, maxtime))  # all particle x-velocity
vy = np.zeros((N, maxtime))  # all particle y-velocity
v = np.zeros((N, maxtime))
p = np.zeros((N, maxtime))
q = np.zeros((N, maxtime))
theta = np.zeros((N, maxtime))
av_theta = np.zeros((N, maxtime))  # all particle average angle of velocity
sumtheta = 0
nn = 1
#Periodic boundary conditions
def PBC (x1):
    if (x1 > L):
        x1 = x1 - L
        return x1
    if (x1 < 0):
        x1 = x1 + L
        return x1
    else:
        return x1

# Initialization  for the visualization
plt.style.use('dark_background')
fig = plt.figure()
ax = plt.axes(xlim=(0, 7), ylim=(0, 7))
points, = ax.plot([], [], 'o')
#############################################
z = 0
# initialization function Plot
def init():
    # creating an empty plot/frame
    points.set_data([], [])
    return points,
##############################################
xdata = np.zeros(N)
ydata = np.zeros(N)
for t in range(0, maxtime, dt):
    if (t == 0):
        for i in range(0, N):
            x[i][t] = PBC(x_0[i]);
            y[i][t] = PBC(y_0[i]);
            theta[i][t] = theta0[i];
            vx[i][t] = v_0 * np.cos(theta[i][t]);
            # print("init cos is ", np.cos(theta[i][t]))
            vy[i][t] = v_0 * np.sin(theta[i][t]);
        # print(x[i][t])
        # print(y[i][t])
        # print(vx[i][t])
        # print(vy[i][t])
        # print("next particle")
    else:
        for i in range(0, N):
            for j in range(0, N):
                if (j != i):
                    if (((((x[i][t - 1] - x[j][t - 1]) ** 2) + ((y[i][t - 1] - y[j][t - 1]) ** 2)) ** 0.5) < 1):
                        sumtheta += theta[j][t - 1];
                        # print("sum is ", sumtheta)
                        nn = nn + 1;
            av_theta[i][t] = sumtheta / nn;
            sumtheta = 0;
            nn = 1;
            # print(y[i][t])
            #print("average theta is", av_theta[i][t - 1])
            theta[i][t] = av_theta[i][t - 1] + dtheta[i];
            x[i][t] = PBC(x[i][t - 1] + vx[i][t - 1] * dt);
            y[i][t] = PBC(y[i][t - 1] + vy[i][t - 1] * dt);
            vx[i][t] = v_0 * np.cos(theta[i][t]);
            vy[i][t] = v_0 * np.sin(theta[i][t]);
            #print("vx=", vx[i][t])
            #print("vy=", vy[i][t])


def animate(z):

    for j in range(0,N):
        xdata[j] = x[j][z]
        ydata[j] = y[j][z]

    points.set_data(xdata, ydata)
    return points,
plt.axis('off')
# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=50, interval=25, blit=True)
# save the animation as mp4 video file
plt.show()