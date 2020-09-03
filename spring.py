# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []
x_verlet_list = [0]
v_verlet_list = [0]

# Euler integration
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

x = 0
v = 1

for t in enumerate(t_array):
    x_verlet_list.append(x)
    v_verlet_list.append(v)

    f = -k * x
    if t[0] == 0:
        x = x + v*dt + dt**2 * f/(2 * m)
    else:
        x = 2*x - x_verlet_list[t[0]] + dt**2 * f/m
    v = (x - x_verlet_list[t[0]])/(2 * dt)

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)

x_verlet_array = np.array(x_verlet_list[1:])
v_verlet_array = np.array(v_verlet_list[1:])

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
#plt.plot(t_array, x_array, label='x_euler (m)')
#plt.plot(t_array, v_array, label='v_euler (m/s)')
plt.plot(t_array, x_verlet_array, label='x_verlet (m)')
plt.plot(t_array, v_verlet_array, label='v_verlet (m/s)')
plt.legend()
plt.show()
