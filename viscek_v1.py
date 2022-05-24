import numpy as np
import cmath
import matplotlib.pyplot as plt

#SYSTEM GENERAL VARIABLES
L = 1; # length of the lattice
N = 500; # No. Of particles
eta = 1; # Noise
dt = 1; # time-step
maxtime = 5; #maximum run time

#VARIABLES
v_0 = 0.03; # initial velocity = 0.03 according to viscek paper
dtheta = np.random.uniform(-eta/2, eta/2, size=N) # fluctuation in angle
theta0 = np.random.uniform(-np.pi, np.pi, size=N) # intial direction for each particle
x_0 = np.random.uniform(0, L, size=N)
y_0 = np.random.uniform(0, L, size=N)
r = np.zeros((N, maxtime))
x = np.zeros((N, maxtime)) # all particle x-position
y = np.zeros((N, maxtime)) # all particle y-position
vx = np.zeros((N, maxtime)) # all particle x-velocity
vy = np.zeros((N, maxtime)) # all particle y-velocity
v = np.zeros((N, maxtime))
theta = np.zeros((N, maxtime))
av_theta = np.zeros((N, maxtime)) # all particle average angle of velocity
sumtheta = 0;
nn = 1;






for t in range (0, maxtime, dt):
    if (t == 0):
        for i in range(0, N):
            x[i][t] = x_0[i];
            y[i][t] = y_0[i];
            theta[i][t] = theta0[i];
            vx[i][t] = v_0*np.cos(theta[i][t]);
            #print("init cos is ", np.cos(theta[i][t]))
            vy[i][t] = v_0*np.sin(theta[i][t]);
            r[i][t] = (x[i][t]*2 + y[i][t]*2)*(0.5);
           # print(x[i][t])
           # print(y[i][t])
            #print(theta[i][t])
            print(vx[i][t])
            print(vy[i][t])
            #print("next particle")
    else:
        for i in range(0, N):
            for j in range (0, N):
                if (((((x[i][t] - x[j][t])*2) + ((y[i][t]-y[j][t])*2))*0.5) < 1):
                    sumtheta += theta[j][t];
                    nn = nn+1;

                av_theta[i][t] = sumtheta/nn;
                sumtheta = 0;
                nn = 1;
                #print("av is",  av_theta[i][t])
            #print(y[i][t])

            theta[i][t] = av_theta[i][t - 1] + dtheta[i];
            vx[i][t] = vx[i][t - 1] * np.cos(theta[i][t]);
            vy[i][t] = vy[i][t - 1] * np.sin(theta[i][t]);
            x[i][t] = x[i][t - 1] + vx[i][t] * dt;
            y[i][t] = y[i][t - 1] + vy[i][t] * dt;


            #print(" average is ", av_theta[i][t]);
            #print("theta is ", theta[i][t])
            print(vx[i][t])
            print(vy[i][t])
            print("next particle")
    plt.plot(x, y, 'ro')
    plt.show()
