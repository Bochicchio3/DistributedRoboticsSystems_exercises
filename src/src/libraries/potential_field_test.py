#!/usr/bin/env python

import random
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



rdn=[random.uniform(0,11) for i in range (15)]
turtle=rdn[0:3]
obs1=rdn[3:5]
obs2=rdn[5:7]
goal=rdn[7:9]

radius=3
k_goal=1
k_t=0.5

def pot_field(X,Y):
    
    pot_field_target=k_goal*compute_distance(X,Y,goal[0],goal[1])
    
    # if compute_distance(X,Y,obs1[0],obs1[1])<radius:
    pot_field_obs1=1/2*k_t*(compute_distance(X,Y,obs1[0],obs1[1])**2)
    
    # if compute_distance(X,Y,obs2[0],obs2[1])<radius:
    pot_field_obs2=1/2*k_t*(compute_distance(X,Y,obs2[0],obs2[1])**2)
           
    pot_field_tot= pot_field_target+pot_field_obs1+pot_field_obs2
    
    return pot_field_target

def obs_field(X,Y):
    
    # if compute_distance(X,Y,obs1[0],obs1[1])<radius:
    pot_field_obs1=1/2*k_t*(compute_distance(X,Y,obs1[0],obs1[1])**2)
    
    # if compute_distance(X,Y,obs2[0],obs2[1])<radius:
    pot_field_obs2=1/2*k_t*(compute_distance(X,Y,obs2[0],obs2[1])**2)
           
    pot_field_tot= pot_field_obs1+pot_field_obs2
    
    return pot_field_tot

def compute_distance(x,y,x_t,y_t):
    return ((y-y_t)**2+(x-x_t)**2)**1/2

fig = plt.figure(figsize=(10, 7))
ax = fig.gca(projection='3d')
x = np.linspace(0, 11, 110)
y = x
print('Goal location is:',goal)

X,Y = np.meshgrid(x, y)
Z = pot_field(X, Y)
Z1=obs_field(X,Y)
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm,
        linewidth=0, antialiased=False)

# ax.set_zlim(0, 20)

ax.zaxis.set_major_locator(plt.LinearLocator(10))
ax.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=7, cmap=plt.cm.coolwarm)

plt.show()


fig2 = plt.figure(figsize=(10, 7))
ax2 = fig2.gca(projection='3d')

surf2 = ax2.plot_surface(X, Y, Z1, rstride=1, cstride=1, cmap=plt.cm.coolwarm,
        linewidth=0, antialiased=False)

# ax.set_zlim(0, 20)

ax2.zaxis.set_major_locator(plt.LinearLocator(10))
ax2.zaxis.set_major_formatter(plt.FormatStrFormatter('%.02f'))

fig2.colorbar(surf2, shrink=0.5, aspect=7, cmap=plt.cm.coolwarm)

plt.show()

