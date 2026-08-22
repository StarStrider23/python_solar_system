import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from miscellaneous.constants import *
from miscellaneous.functions import accel, animate
import miscellaneous.scenario_1
import miscellaneous.scenario_2

"""
@author: Alexsey Chernichenko
Summer 2023
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
    
m_i - mass of the ith body (kg)
x_i - x coordinate (at perihelion) (m)
y_i - y coordinate (m)
a_i - semi-major axis of an orbit (m)
eps_i - eccentricity of an orbit (dimensionless)
v_i_x - x component of velocity (at perihelion) (m/s)
v_i_y - y component of velocity (m/s)

The user can choose which scenario to simulate by changing the variable scenario in the main file. 
The default value is 1, which corresponds to the first scenario. This scenario solves the equations 
of motion for the Solar system and plots the trajectory of each planet for the next 100 years. 
The second scenario adds a level of complexity by including another Sun-like star which flies by the
Solar system and wreaks chaos. It also solves the necessary equations and plots the trajectory
of the planets and stars. To choose it, set the scenario variable to 2.

"""

mult = 10 #number of years
time = (0, mult * t_year)
teval = np.linspace(0, mult * t_year, 1000)

scenario = 1

if scenario == 1:
    data = miscellaneous.scenario_1
    title = f'Simulation of the Solar system ({mult} year)'
elif scenario == 2:
    data = miscellaneous.scenario_2
    title = f'Simulation of a fly-by of a Sun-like star through the Solar system ({mult} years)'

start = data.start
mass = data.mass
space_obj = data.space_obj
color = data.color
l = len(mass)

"Solving --------------------------------------------------------"

sol = solve_ivp(accel, time, start, t_eval=teval, rtol=1e-10, atol=1e-10, args=(mass,))

"Plotting -------------------------------------------------------"

#Animation plot
#Knows automatically which scenario is chosen

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()

plt.xlabel('x axis (m)')
plt.ylabel('y axis (m)')
plt.title(title)
plt.grid(linestyle='--', linewidth=0.5)

ax.set_ylim(-4.5e12, 4.5e12)
ax.set_xlim(-4.5e12, 4.5e12)

lines = []

for j in range(len(space_obj)):
    line, = ax.plot([], [], color=color[j], label=space_obj[j])
    lines.append(line)

ax.legend(loc='upper left')

solar_animation = animation.FuncAnimation(fig, animate, fargs=(sol, lines), interval=50, cache_frame_data=False)

# If you want to save the animation as a GIF, uncomment the line below. Make sure you have the 'pillow' library installed.
# Also, make sure to insert this inside the FuncAnimation: frames=range(0, len(sol.t), 10)
# This will skip frames to make the GIF smaller and faster. Adjust the step size as needed.

# solar_animation.save(f"scenario_{scenario}.gif", writer="pillow", fps=15)

plt.show()
