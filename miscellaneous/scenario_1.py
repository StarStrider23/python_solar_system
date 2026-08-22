import numpy as np

from miscellaneous.constants import *


"""
This scenario contains data for solving the solar system and plotting each of the planets trajectory
for the next 100 years
"""

mass = [m_S, m_mer, m_v, m_e, m_m, m_j, m_s, m_u, m_n]

#Initial conditions for the celestial bodies. Essentially, they all start
#from the corresponding perehelium with velocities pointed in the y direction

# start = np.array([r_S, r_mer, r_v, r_e, r_m, r_j, r_s, r_u, r_n,
#                     v_S, v_mer, v_v, v_e, v_m, v_j, v_s, v_u, v_n])

# print(len(start))

start = np.concatenate([r_S, r_mer, r_v, r_e, r_m, r_j, r_s, r_u, r_n, 
                        v_S, v_mer, v_v, v_e, v_m, v_j, v_s, v_u, v_n])

# print(len(start))

#Each cellestial body has its ows color

color = ['yellow', 'gray', 'brown', 'green',
         'orange', 'tan', 'slategray',
         'cyan', 'royalblue']

#And its own label

space_obj = ['Sun', 'Mercury', 'Venus', 'Earth',
             'Mars', 'Jupiter', 'Saturn', 'Uranus', 
             'Neptune']