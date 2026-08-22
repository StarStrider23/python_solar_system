import numpy as np
import scipy.constants as const


"""

The accel function calculates the acceleration of each celestial body in the solar system due to the gravitational 
forces exerted by all other bodies. It takes as input the current time, the state vector containing positions and 
velocities of all bodies, and their masses. The function returns the derivatives of the state vector, which include 
the velocities and accelerations of each body.

"""

def accel(t, y, mass):
    """

    Parameters
    ----------
    t : 2-tuple, (t0, tf)
        Time interval 
    y : Array-like (x, y, .., v_x, v_y, ...)
        Contains the initial values of cellestial bodies'
        position and velocity components

    Returns
    -------
    dydt : Array-like (v_x, v_y, ..., a_x, a_y, ...)
           Contains derivatives of y, i.e. velocities' and
           accelerations' components

    """

    G = const.G

    l = len(mass)

    dydt = np.zeros(4*l)

    dydt[:2*l] = y[2*l:]

    for i in range(0, l):

        for j in range(0, l):

            if j != i:

                dydt[2*l+2*i] += (G * mass[j] * (y[2*j] - y[2*i])) / (((y[2*j]  - y[2*i])**2 +(y[2*j+1] - y[2*i+1])**2)**(3/2))

                dydt[2*l+1+2*i] += (G * mass[j] * (y[2*j+1] - y[2*i+1])) / (((y[2*j]  - y[2*i])**2 + (y[2*j+1] - y[2*i+1])**2)**(3/2))

    return dydt


"""

The vis_viva function calculates the velocity of a celestial body at a given distance from the focus of its orbit, 
based on the vis-viva equation. It takes as input the semi-major axis of the orbit, the distance from the focus, 
and the mass of the central body. The function returns the velocity of the celestial body at that distance.

"""

def vis_viva(m, a, eps): 
    """

    Parameters
    ----------
    a : float
        Semi-major axis of the orbit (m)
    r : float
        Distance from the focus of the orbit (m)
    m : float
        Mass of the central body (kg)

    Returns
    -------
    v : float
        Velocity of the celestial body at distance r (m/s)

    """

    G = const.G

    v = np.sqrt((G * m * (1 + eps)) / (a * (1 - eps))) 

    return v

"""
Animate function that plots the trajectory of each celestial body in the solar system over time. 
"""

# def animate(i, sol, ax, space_obj, color):
    
#     for j in range(0, len(space_obj)): 
#         ax.plot(sol.y[2*j][:i], sol.y[2*j+1][:i], color=color[j])
        
#     ax.legend(labels=space_obj, loc='upper left')


def animate(i, sol, lines):

    for j, line in enumerate(lines):

        line.set_data(sol.y[2*j][:i], sol.y[2*j+1][:i])