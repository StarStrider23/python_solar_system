import numpy as np

from miscellaneous.constants import *
from miscellaneous.scenario_1 import mass as mass_1, start as start_1, color as color_1, space_obj as space_obj_1

"""
This scenario adds a level of complexity by including another Sun-like star which flies by the
Solar system and wreaks chaos. It also solves the necessary equations and plots the trajectory
of the planets and stars. To choose it, uncomment out the lines below and comment out the lines 
between 'Solar system IC' and 'Sun-like star (star) and IC'
"""

#The new star of the same mass as the Sun

m_star = m_S

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

#Velocity components. Note the correction

v_star_x = -V_star * np.cos(theta - phi)
v_star_y = -V_star * np.sin(theta - phi)

r_star = (x_star, y_star)
v_star = (v_star_x, v_star_y)

mass = mass_1.copy()
mass += [m_star]

start = start_1.copy()
start = np.insert(start, 18, r_star)
start = np.insert(start, 38, v_star)

color = color_1.copy()
color += ['black'] 

space_obj = space_obj_1.copy()
space_obj += ['Sun-like star']