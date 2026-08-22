import numpy as np
import scipy.constants as const

from miscellaneous.functions import vis_viva

"""

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

"""

"Constants -----------------------------------------------------"

G = const.G #gravitational constant, N m^2 kg^-2

t_year = 365.25*24*60*60 #1 year in seconds

"""

CELESTIAL BODIES' DATA

"""

"Sun (S)--------------------------------------------------------"

m_S = 1.9885e30

x_S = 0 
y_S = 0

v_S_x = 0 
v_S_y = 0

r_S = (x_S, y_S)
v_S = (v_S_x, v_S_y)

"Mercury (mer)-----------------------------------------------------"

m_mer = 3.302e23

x_mer = 46001272e3
y_mer = 0

eps_mer = 0.20563069 
a_mer = 57909050e3 

v_mer_x = 0
v_mer_y = vis_viva(m_S, a_mer, eps_mer)

r_mer = (x_mer, y_mer)
v_mer = (v_mer_x, v_mer_y)

"Venus (v)--------------------------------------------------------"

m_v = 4.8685e24

x_v = 107476002e3
y_v = 0

eps_v = 0.00677323
a_v = 108208926e3

v_v_x = 0
v_v_y = vis_viva(m_S, a_v, eps_v)

r_v = (x_v, y_v)
v_v = (v_v_x, v_v_y)

"Earth (e)--------------------------------------------------------"

m_e = 5.9722e24

x_e = 147098074e3
y_e = 0

eps_e = 0.0167086 
a_e = 149597887.5e3

v_e_x = 0
v_e_y = vis_viva(m_S, a_e, eps_e)

r_e = (x_e, y_e)
v_e = (v_e_x, v_e_y)

"Mars (m)--------------------------------------------------------"

m_m = 6.4174e23 

x_m = 206644545e3 
y_m = 0

eps_m = 0.09341233
a_m = 227936637e3

v_m_x = 0
v_m_y = vis_viva(m_S, a_m, eps_m)

r_m = (x_m, y_m)
v_m = (v_m_x, v_m_y)

"Jupiter (j)--------------------------------------------------------"

m_j = 1.899e27

x_j = 740742598e3
y_j = 0

eps_j = 0.04839266
a_j = 778412027e3

v_j_x = 0
v_j_y = vis_viva(m_S, a_j, eps_j)

r_j = (x_j, y_j)
v_j = (v_j_x, v_j_y)

"Saturn (s)--------------------------------------------------------"

m_s = 5.6846e26

x_s = 1349467375e3
y_s = 0

eps_s = 0.05415060
a_s = 1426725413e3

v_s_x = 0
v_s_y = vis_viva(m_S, a_s, eps_s)

r_s = (x_s, y_s)
v_s = (v_s_x, v_s_y)

"Uranus (u)--------------------------------------------------------"

m_u = 8.6832e25

x_u = 2735555035e3
y_u = 0

eps_u = 0.04716771
a_u = 2870972220e3

v_u_x = 0
v_u_y = vis_viva(m_S, a_u, eps_u)

r_u = (x_u, y_u)
v_u = (v_u_x, v_u_y)

"Neptune (n)--------------------------------------------------------"

m_n = 1.0243e26

x_n = 4459631496e3
y_n = 0

eps_n = 0.00858587
a_n = 4498252900e3

v_n_x = 0
v_n_y = vis_viva(m_S, a_n, eps_n)

r_n = (x_n, y_n)
v_n = (v_n_x, v_n_y)