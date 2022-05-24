# Updated on 18/05/2020
# Time : 20:14
# Update made : Version 1.0 with order parameter almost working
import numpy as np
import matplotlib.animation as animation
import cmath
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

# SYSTEM GENERAL VARIABLES
L = 3;  # length of the lattice
N = 40;  # No. Of particles
eta = 0.03;  # Noise
dt = 1;  # time-step
maxtime = 500;  # maximum run time
delta_eta = 0.05
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
nn = 1
theta0 = np.degrees(theta0)
dtheta = np.degrees(dtheta)
sum_sintheta = 0
sum_costheta = 0
av_sin = np.zeros((N, maxtime))
av_cos = np.zeros((N, maxtime))
v_a = 0
v_ax = 0
v_ay = 0
v_a_final = 0;
T = np.linspace(0, maxtime, num=500)


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


"""
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
"""
xdata = np.zeros(N)
ydata = np.zeros(N)
for t in range(0, maxtime, dt):
    if (t == 0):
        for i in range(0, N):
            x[i][t] = PBC(x_0[i]);
            y[i][t] = PBC(y_0[i]);
            theta[i][t] = theta0[i];
            vx[i][t] = v_0 * np.cos(theta[i][t]);
            vy[i][t] = v_0 * np.sin(theta[i][t]);

    else:
        for i in range(0, N):
            for j in range(0, N):
                if (j != i):
                    if (((((x[i][t - 1] - x[j][t - 1]) ** 2) + ((y[i][t - 1] - y[j][t - 1]) ** 2)) ** 0.5) < 1):
                        sum_sintheta += np.sin(theta[j][t - 1]);
                        sum_costheta += np.cos(theta[j][t - 1]);
                        # print("sum is ", sumtheta)
                        nn = nn + 1;
            av_sin[i][t - 1] = sum_sintheta / nn;
            av_cos[i][t - 1] = sum_costheta / nn;
            if (av_cos[i][t - 1] == 0):
                av_theta[i][t] = np.pi/2
            else:
                av_theta[i][t] = np.arctan(av_sin[i][t - 1]/av_cos[i][t - 1]);
            sumtheta = 0;
            sum_sintheta = 0;
            sum_costheta = 0;
            nn = 1;
            # print(y[i][t])
            #print("average theta is", av_theta[i][t - 1])
            theta[i][t] = av_theta[i][t] + dtheta[i];
            x[i][t] = PBC(x[i][t - 1] + vx[i][t - 1] * dt);
            y[i][t] = PBC(y[i][t - 1] + vy[i][t - 1] * dt);
            vx[i][t] = v_0 * np.cos(theta[i][t]);
            vy[i][t] = v_0 * np.sin(theta[i][t]);

for k in range(0,N):
    v_ax += vx[k][maxtime-1]
    v_ay += vy[k][maxtime-1]


    v_a_final = abs(np.sqrt((v_ay * v_ay) + (v_ax * v_ax)))
        #print(v_a[t])
# print(v_a[t])
v_a_final = v_a_final / (N*v_0);
print("Average velocity is :", v_a_final)
plt.plot(T, v_a)
plt.show()



