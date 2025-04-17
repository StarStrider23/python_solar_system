"""
@author: Alexsey Chernichenko
The program simulates the Solar system 100 years from now on. It
does so by solving a system of appropriate differential equations
that contain gravitational interraction between celestial bodies. 
Moreover, it shows yet another scenario where a Sun-like star
appears in the random location between the Earth and the Neptune.
The program simulates the scenario and how the new star affects
all the bodies in the Solar system. Both scenarios are then plotted.

Notation:
    
i and j are indices that can be any of the follwoing:
    S - Sun
    mer - Mercury
    v - Venus
    e - Earth
    m - Mars
    j - Jupiter
    s - Saturn
    u - Uranus
    n - Neptune
    star - Sun-like star
    
m_i - mass of the ith body
x_i - x coordinate (at perihelion)
y_i - y coordinate
a_i - semi-major axis of an orbit
eps_i - eccentricity of an orbit
v_i_x - x component of velocity (at perihelion)
v_i_y - y component of velocity

"""
#%% Packages and some constants

import numpy as np
import scipy.constants as const
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

G = const.G #gravitational constant, N m^2 kg^-2

t_year = 365.25*24*60*60 #1 year in seconds

#%% Celestial objects

"Sun (S)--------------------------------------------------------"

m_S = 1.9885e30 #all mass in kg

x_S = 0 #all position components in meters
y_S = 0

v_S_x = 0 #all velocity components in m/s
v_S_y = 0

r_S = (x_S, y_S) #tuple with coordinate components
v_S = (v_S_x, v_S_y) #tuple with velocity components

"Mercury (mer)--------------------------------------------------------"

m_mer = 3.302e23

x_mer = 46001272e3
y_mer = 0

eps_mer = 0.20563069 #eccentricity is a dimensionless parameter
a_mer = 57909050e3 #all semi-major axes in meters

v_mer_x = 0
v_mer_y = np.sqrt((G * m_S * (1 + eps_mer)) / (a_mer * (1 - eps_mer))) 
#Vis-viva eq, speed at perehelium

r_mer = (x_mer, y_mer)
v_mer = (v_mer_x, v_mer_y)

"Venus (v)--------------------------------------------------------"

m_v = 4.8685e24

x_v = 107476002e3
y_v = 0

eps_v = 0.00677323
a_v = 108208926e3

v_v_x = 0
v_v_y = np.sqrt((G * m_S * (1 + eps_v)) / (a_v * (1 - eps_v)))

r_v = (x_v, y_v)
v_v = (v_v_x, v_v_y)

"Earth (e)--------------------------------------------------------"

m_e = 5.9722e24

x_e = 147098074e3
y_e = 0

eps_e = 0.0167086 
a_e = 149597887.5e3

v_e_x = 0
v_e_y = np.sqrt((G * m_S * (1 + eps_e)) / (a_e * (1 - eps_e)))

r_e = (x_e, y_e)
v_e = (v_e_x, v_e_y)

"Mars (m)--------------------------------------------------------"

m_m = 6.4174e23 

x_m = 206644545e3 
y_m = 0

eps_m = 0.09341233
a_m = 227936637e3

v_m_x = 0
v_m_y = np.sqrt((G * m_S * (1 + eps_m)) / (a_m * (1 - eps_m)))

r_m = (x_m, y_m)
v_m = (v_m_x, v_m_y)

"Jupiter (j)--------------------------------------------------------"

m_j = 1.899e27

x_j = 740742598e3
y_j = 0

eps_j = 0.04839266
a_j = 778412027e3

v_j_x = 0
v_j_y = np.sqrt((G * m_S * (1 + eps_j)) / (a_j * (1 - eps_j)))

r_j = (x_j, y_j)
v_j = (v_j_x, v_j_y)

"Saturn (s)--------------------------------------------------------"

m_s = 5.6846e26

x_s = 1349467375e3
y_s = 0

eps_s = 0.05415060
a_s = 1426725413e3

v_s_x = 0
v_s_y = np.sqrt((G * m_S * (1 + eps_s)) / (a_s * (1 - eps_s)))

r_s = (x_s, y_s)
v_s = (v_s_x, v_s_y)

"Uranus (u)--------------------------------------------------------"

m_u = 8.6832e25

x_u = 2735555035e3
y_u = 0

eps_u = 0.04716771
a_u = 2870972220e3

v_u_x = 0
v_u_y = np.sqrt((G * m_S * (1 + eps_u)) / (a_u * (1 - eps_u)))

r_u = (x_u, y_u)
v_u = (v_u_x, v_u_y)

"Neptune (n)--------------------------------------------------------"

m_n = 1.0243e26

x_n = 4459631496e3
y_n = 0

eps_n = 0.00858587
a_n = 4498252900e3

v_n_x = 0
v_n_y = np.sqrt((G * m_S * (1 + eps_n)) / (a_n * (1 - eps_n)))

r_n = (x_n, y_n)
v_n = (v_n_x, v_n_y)

#%% Mooon (moon)
#Not included, please read the report

m_moon = 7.342e22

x_moon = x_e + 362600e3
y_moon = 0

eps_moon = 0.0549
a_moon = 384399e3

v_moon_x = 0
v_moon_y = v_e_y + np.sqrt((G * m_e * (1 + eps_moon)) / (a_moon * (1 - eps_moon)))

r_moon = (x_moon, y_moon)
v_moon = (v_moon_x, v_moon_y)


#%% Solar system IC

mass = [m_S, m_mer, m_v, m_e, m_m, m_j, m_s, m_u, m_n] #contains masses of all celestial bodies 


#Initial conditions for the celestial bodies. Essentially, they all start
#from the corresponding perehelium with velocities pointed in the y direction
start = np.append(np.zeros(0), [r_S, r_mer, r_v, r_e, r_m, r_j, r_s, r_u, r_n, 
                                v_S, v_mer, v_v, v_e, v_m, v_j, v_s, v_u, v_n])

#Each cellestial body has its ows color
color = ['yellow', 'gray', 'brown', 'green',
         'orange', 'tan', 'slategray',
         'cyan', 'royalblue']

#And its own label
space_obj = ['Sun', 'Mercury', 'Venus', 'Earth',
             'Mars', 'Jupiter', 'Saturn', 'Uranus', 
             'Neptune']

#%% Sun-like star (star) and IC

m_star = m_S #The new star of the same mass as the Sun

#Assume that neptune's perihelium is the frontier of the solar system
#The star appears in a random location between the Earth and the Neptune
rad = np.random.uniform(x_e, x_n) 
theta = np.random.uniform(0, 2 * np.pi)

#x and y components of the new star
x_star = rad * np.cos(theta)
y_star = rad * np.sin(theta)

#This angle corrects the new star's trajectory towards the Earth's orbit
#and not towards the Sun 
phi = np.arcsin(x_e / rad)

#The velocity of the new star s.t. it takes 100 years to cross the elliptic
#(in this case elliptic is the circle with radius of the neptune's perihelium)
V_star = (2 * x_n) / (100 * t_year)

#Velocity components. Note the correction.
v_star_x = -V_star * np.cos(theta - phi)
v_star_y = -V_star * np.sin(theta - phi)

r_star = (x_star, y_star)
v_star = (v_star_x, v_star_y)

mass = [m_S, m_mer, m_v, m_e, m_m, m_j, m_s, m_u, m_n, m_star]

start = np.append(np.zeros(0), [r_S, r_mer, r_v, r_e, r_m, r_j, r_s, r_u, r_n, r_star, 
                                v_S, v_mer, v_v, v_e, v_m, v_j, v_s, v_u, v_n, v_star])

color = ['yellow', 'grey', 'brown', 'green',
         'orange', 'tan', 'slategray',
         'cyan', 'royalblue', 'black']

space_obj = ['Sun', 'Mercury', 'Venus', 'Earth', 
             'Mars', 'Jupiter', 'Saturn', 'Uranus', 
             'Neptune', 'Sun-like star']

#%% Function, ode solver

mult = 100 #number of years
time = (0, mult * t_year)
teval = np.linspace(0, mult * t_year, 10000)

l = len(mass)

#The function automatically sees which of the scenarios is choosen
#Calculates acceleration of celestial bodies in the Solar system
#This essentially can be seen as a system of differential eqs
def accel(t, y):
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
    dydt = np.zeros(4*l)
    dydt[:2*l] = y[2*l:]
    for i in range(0, l):
        for j in range(0, l):
            if j != i:
                dydt[2*l+2*i] += (G * mass[j] * (y[2*j] - y[2*i])) / (((y[2*j]  - y[2*i])**2 +(y[2*j+1] - y[2*i+1])**2)**(3/2))
                dydt[2*l+1+2*i] += (G * mass[j] * (y[2*j+1] - y[2*i+1])) / (((y[2*j]  - y[2*i])**2 + (y[2*j+1] - y[2*i+1])**2)**(3/2))
    return dydt

#Solves a system of differential equations above to plot trajectories
sol = solve_ivp(accel, time, start, t_eval=teval, rtol=1e-10, atol=1e-10)

#%% Plotting

#Also knows which scenario is chosen
plt.figure(figsize=(12,8))
for i in range(0, len(mass)):  
    plt.plot(sol.y[2*i], sol.y[2*i+1], color = color[i], label = space_obj[i])
plt.xlabel('x axis (m)')
plt.ylabel('y axis (m)')
plt.legend()
if l == 9:
    plt.title('Simulation of the Solar system (100 years)')
#    plt.savefig('Solar100y.png')
elif l ==10:
    plt.title('Fly-by of a Sun-like star through the Solar system')
#    plt.savefig('Chaos100y.png')
plt.show()

