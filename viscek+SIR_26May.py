# Updated on 25/05/2020
# Time : 21:10 AM
# Update made : Version 2.0.0 Viscek plus the infected flock using SIR implemented.
#We fixed the update but the graph is not good yet.
import numpy as np
import matplotlib.animation as animation
import cmath
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import random as rndm
# VICSEK VARIABLES
L = 3;  # length of the lattice
N = 40;  # No. Of particles
eta = 5;  # Noise
dt = 1;  # time-step
maxtime = 50;  # maximum run time
v_0 = 0.03;  # initial velocity = 0.03 according to viscek paper
# INFECTION VARIABLES
I_0 = 10; #initial number of susceptibles
S_0 = N - I_0; #initial number of infected+
R_0 = 0;#initial number of recovered
I = I_0
S = S_0
R = R_0
a = 0.2; #recovery rate
r = 0.6; #infection rate
dtheta = np.random.uniform(-eta/2, eta/2, size=N)  # fluctuation in angle
theta0 = np.random.uniform(-np.pi, np.pi, size=N)  # initial direction for each particle
x_0 = np.random.uniform(0, L, size=N)
y_0 = np.random.uniform(0, L, size=N)
x = np.zeros((N, maxtime))  # all particle x-position
y = np.zeros((N, maxtime))  # all particle y-position
c = np.zeros((N, maxtime))  # infection information
vx = np.zeros((N, maxtime))  # all particle x-velocity
vy = np.zeros((N, maxtime))  # all particle y-velocity
v = np.zeros((N, maxtime))
p = np.zeros((N, maxtime))
q = np.zeros((N, maxtime))
theta = np.zeros((N, maxtime))
av_theta = np.zeros((N, maxtime))  # all particle average angle of velocity
nn = 1
mm = 1
sum_sintheta = 0
sum_costheta = 0
av_sin = np.zeros((N, maxtime))
av_cos = np.zeros((N, maxtime))
v_ax = np.zeros((maxtime))
v_ay = np.zeros((maxtime))
v_ax2 = np.zeros((maxtime))
v_ay2 = np.zeros((maxtime))
S_p = np.zeros((maxtime))
I_p = np.zeros((maxtime))
R_p = np.zeros((maxtime))
T = np.linspace(0, maxtime, num=maxtime)
SIR = [0, -1, +1]
# Periodic boundary conditions
def PBC(x1):
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
ax = plt.axes(xlim=(0, L), ylim=(0, L))
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
def init_infection(t):
    for i in range(0, I_0):
        a1 = np.random.randint(0, N)
        c[a1][t] = SIR[1];
def decay_infection(t):
    global R
    global I
    global S
    #print('I = ',I)
    for i in range(0,N):
        if (c[i][t] == SIR[1]):
            #if(rndm.uniform(0, 1) < np.exp(-(1-a)/t)): #acceptance rate
            if(rndm.uniform(0, 1) < a): #acceptance rate
                for o in range(0, maxtime):
                    c[i][o] = SIR[2]
                #c[i][t + 1] = SIR[2];
                print("INSIDE at t = ", t)
                R = R + 1
                I = I - 1

for t in range(0, maxtime - 1, dt):
    if (t == 0):
        for i in range(0, N):
            x[i][t] = PBC(x_0[i])
            y[i][t] = PBC(y_0[i])
            c[i][t+1] = SIR[0]
            theta[i][t] = theta0[i]
            vx[i][t] = v_0 * np.cos(theta[i][t])
            vy[i][t] = v_0 * np.sin(theta[i][t])
        init_infection(t+1)
        S_p[t] = S_0
        I_p[t] = I_0
        R_p[t] = R_0
    else:
        for i in range(0, N):
            for j in range(0, N):
                if (j != i):
                    if (((((x[i][t - 1] - x[j][t - 1]) ** 2) + ((y[i][t - 1] - y[j][t - 1]) ** 2)) ** 0.5) < 1):
                        sum_sintheta += np.sin(theta[j][t - 1])
                        sum_costheta += np.cos(theta[j][t - 1])
                        # print("sum is ", sumtheta)
                        nn = nn + 1;

                        #if (c[i][t] != 0):
                            #print(c[i][t])
                        if (c[i][t] == SIR[1] and c[j][t] == SIR[0]):

                            if (rndm.uniform(0, 1) < r):
                                for o in range(0, maxtime):
                                    c[j][o] = SIR[1]
                                print('HERE AT t=',t)
                                I = I + 1
                                if(S!=0):
                                    S = S - 1


                        #if (c[i][t] == SIR[0] and c[j][t] == SIR[1]):
                         #   if (rndm.uniform(0, 1) < (1-np.exp(-r/t))):
                          #      c[i][t] = SIR[1]
                           #     I = I + 1
                            #    S = S - 1
            av_sin[i][t - 1] = sum_sintheta / nn
            av_cos[i][t - 1] = sum_costheta / nn
            av_theta[i][t - 1] = np.arctan2(av_sin[i][t - 1] , av_cos[i][t - 1])
            sumtheta = 0
            sum_sintheta = 0
            sum_costheta = 0
            nn = 1
            # print(y[i][t])
            #print("random theta is", dtheta[i])
            theta[i][t] = av_theta[i][t - 1] + dtheta[i]
            x[i][t] = PBC(x[i][t - 1] + vx[i][t - 1] * dt)
            y[i][t] = PBC(y[i][t - 1] + vy[i][t - 1] * dt)
            vx[i][t] = v_0 * np.cos(theta[i][t])
            vy[i][t] = v_0 * np.sin(theta[i][t])
        decay_infection(t)
        S_p[t] = S
        I_p[t] = I
        R_p[t] = R
'''
def animate(z):
    for j in range(0,N):
        xdata[j] = x[j][z]
        ydata[j] = y[j][z]
    points.set_data(xdata, ydata)
    return points,
plt.axis('off')
# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=maxtime, interval=10, blit=True)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
# save the animation as mp4 video file
plt.show()
#anim.save('vicsek.mp4', writer='ffmpeg', dpi=200)
'''
print("S =", S)
print("I =", I)
print("R =", R)
print("N =", N)
print("S + R + I = ", S+I+R)
plt.plot(T, S_p, color="green")
plt.plot(T, I_p, color = "red")
plt.plot(T, R_p, color = "blue")
plt.xlim(0,maxtime)
plt.ylim(0,N)
plt.show()