# Solving the Solar system

By Alexsey Chernichenko. Summer 2023.

# Project Description

The program simulates the Solar system 100 years from now on. It does so by solving a system of appropriate differential equations that contain gravitational interactions between celestial bodies. Moreover, it shows yet another scenario where a Sun-like star appears in the random location between the Earth and the Neptune and wreaks chaos. The program simulates the scenario and how the new star affects all the bodies in the Solar system. By choosing one of the scenarios, the trajectories of the planets and the star(s) are then animated. 

# Theory 

Our solar system consists of the Sun, the planets and other smaller objects. For simplicity this project will neglect the last category and deal with the Sun and the planets only. Each body, whether it’s the Sun or any of the planets, experiences gravitational forces from other bodies. The total gravitational force ($\textbf{F}_i$) experienced by a body (with index $i$) can be described as following:

$$ \textbf{F}_{i} = \sum^n_{j = 1, j \neq i} \frac{G m_i m_j}{r^3_{ij}}\textbf{r}_{ij} $$

Where $G$ is the gravitational constant, $m_i$ is the  ith body's mass, $m_j$ is a mass of another body in the system, $r_{ij}$ is the distance between the bodies and $\textbf{r}_{ij}$ is the corresponding vector.

As $\textbf{F}_i$ = $m_i\textbf{a}_i$ we can express acceleration of the ith body as

$$ \textbf{a}_i = \sum^n_{j = 1, j \neq i} \frac{G m_j}{r^3_{ij}}\textbf{r}_{ij} $$

Having 1 star and 8 planets (planet nine is yet to be discovered) we have 9 objects and therefore in equation above $n$ = 9. 

The planets, the Sun and all the smaller objects orbit the common center of mass. However, as the center of mass is located inside the Sun it is fairly acceptable to say that everything orbits the Sun. Also it does so in elliptic orbits (that are actually close to circular). A parameter that describes how different an orbit is from circular is called eccentricity ($\epsilon$). If $\epsilon$ = 0 then an orbit is circular. 

Every orbit has the furthest and the closest point to the Sun. They are called $\textit{aphelion}$ and $\textit{perihelion}$ respectively. Due to the Kepler's second law orbital speed of a body at perihelion is the fastest and at aphelion is slowest. In other words, the closer a body is to the Sun, the faster it moves.

Using the so-called $\textit{Vis-viva equation}$ and the formula for ellipse one can find body's speed at a certain point on orbit . This is required to find speed at perihelion as it will be needed further on.

The Vis-Viva equation is:

$$ v^2 = GM\bigg(\frac{2}{r} - \frac{1}{a}\bigg) $$

where $M$ is the mass of the central body (i.e. the Sun) and $r$ is the distance to it at a specific moment. Actually, $r$ describes an ellipse and has the form as below:

$$ r = \frac{l}{1 + \epsilon \cos\theta} $$

Where $l$ is a parameter called $\textit{semi-latus}$ rectum which can be expressed as \textit{l} = a(1-$\epsilon^2$).

Inserting equation above into the Vis-Viva equation with $\theta$ = 0 (i.e. perihelion) and simplifying yields the result below:

$$ v = \sqrt{\frac{GM(1+\epsilon)}{a(1-\epsilon)}} $$

which is speed of a body at its perihelion. 

Yet another essential parameter is the $\textit{semi-major}$ axis ($a$). It is distance either from aphelion or perihelion to center of ellipse. 

# Result

The first step is obviously to write down all the essential constants required for future computations. This is basically all the things written in the theory section.

Since the goal of the project is to plot trajectories of the celestial bodies in the Solar system one needs to solve a system of 8 equations of the form as equation for acceleration. This is essentially a system of differential equations. To proceed one can write a function that takes a time interval and an array (call it $y$) with position and velocities and returns derivative of the array $y$. Each body is then specified by 3 position and 3 velocity components, thus making 6 in total. However, since all the bodies' orbits are (approximately) in the same plane (ecliptic), one can simplify the problem to 2 dimensions. Therefore, each body has now 2 position and 2 velocity components. The array's first half represents position components which are then followed by velocity components for different objects. The array varies depending on the scenario. 

One could write all the acceleration components explicitly, but that is way too laborious and therefore the idea is to use for loops. We'll need a double for loop, one for $i$ and the other $j$. In other words, this is a nested for loop. One thing to note here is the condition $i \neq j$. Otherwise we'd get a factor where a celestial body exerts gravity on itself and this will eventually lead to an error when the code is executed.

To solve a system of differential equations the solve$_$ivp method is used. As the initial conditions all the objects are aligned on the $x$ axis with their velocities pointed in upwards (i.e. parallel to $y$ axis). Except for the Sun which is located at the origin with zero velocity. 

<img width="2400" height="1600" alt="scenario_1" src="https://github.com/user-attachments/assets/feb80948-b99e-4e1e-bcdd-08b8e434c868" />

<img width="2400" height="1600" alt="scenario_2" src="https://github.com/user-attachments/assets/ccae72be-74c3-41e8-ac46-03758af85c68" />
