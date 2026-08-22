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

Using the so-called `Vis-viva equation` and the formula for ellipse one can find body's speed at a certain point on orbit . This is required to find speed at perihelion as it will be needed further on.

The Vis-Viva equation is:

$$ v^2 = GM\bigg(\frac{2}{r} - \frac{1}{a}\bigg) $$

where $M$ is the mass of the central body (i.e. the Sun) and $r$ is the distance to it at a specific moment. Actually, $r$ describes an ellipse and has the form as below:

$$ r = \frac{l}{1 + \epsilon \cos\theta} $$

Where $l$ is a parameter called `semi-latus` rectum which can be expressed as $l = a(1 - \epsilon^2)$.

Inserting equation above into the Vis-Viva equation with $\theta$ = 0 (i.e. perihelion) and simplifying yields the result below:

$$ v = \sqrt{\frac{GM(1+\epsilon)}{a(1-\epsilon)}} $$

which is speed of a body at its perihelion. 

Yet another essential parameter is the `semi-major axis` ($a$). It is distance either from aphelion or perihelion to center of ellipse. 

# Method

The first step is obviously to write down all the essential constants required for future computations. This is basically all the things written in the theory section.

Since the goal of the project is to plot trajectories of the celestial bodies in the Solar system one needs to solve a system of 8 equations of the form as equation for acceleration. This is essentially a system of differential equations. To proceed one can write a function that takes a time interval and an array (call it $y$) with position and velocities and returns derivative of the array $y$. Each body is then specified by 3 position and 3 velocity components, thus making 6 in total. However, since all the bodies' orbits are (approximately) in the same plane (ecliptic), one can simplify the problem to 2 dimensions. Therefore, each body has now 2 position and 2 velocity components. The array's first half represents position components which are then followed by velocity components for different objects. The array varies depending on the scenario. 

One could write all the acceleration components explicitly, but that is way too laborious and therefore the idea is to use for loops. We'll need a double for loop, one for $i$ and the other $j$. In other words, this is a nested for loop. One thing to note here is the condition $i \neq j$. Otherwise we'd get a factor where a celestial body exerts gravity on itself and this will eventually lead to an error when the code is executed.

To solve a system of differential equations the solve_ivp method is used. As the initial conditions all the objects are aligned on the $x$ axis with their velocities pointed in upwards (i.e. parallel to $y$ axis). Except for the Sun which is located at the origin with zero velocity. 

# Result

## Scenario 1

The first part is about simulating the Solar system only. The interval of simulation is said to be 100 years. The gif below confirms that the trajectories of the celestial bodies in the Solar System agree qualitatively with the expected orbits as we observe elliptical orbits around the Sun

<img width="2400" height="1600" alt="scenario_1" src="https://github.com/user-attachments/assets/faa12472-f26e-455d-af47-59f8d7319741" />

## Scenario 2

In this part, a Sun-like star appears somewhere between the Earth and the Neptune. It has a velocity such that it'd 100 years for the star to cross the ecliptic (in this case, the distance which is equal to 2 perihelion of the Neptune). The direction of its motion is chosen such that it avoids a head-to-head collision with the Sun, but rather goes somewhat to the side so that it passes the Sun as close as the Earth does (roughly). As the initial coordinates of the star are chosen randomly every simulation shows a different picture, yet all of them have a common feature - a total disruption of the system as some planets fly away from the Solar system. This is a fascinating, but not a surprising result. The gif below demonstrates the consequences of such a scenario.

<img width="2400" height="1600" alt="scenario_2" src="https://github.com/user-attachments/assets/d8a11596-c324-4971-97fb-0852ec1e8f08" />

# Discussion

The results show that the numerical model successfully reproduces the expected behaviour of the Solar system, with the planets following approximately elliptical orbits around the Sun. The second scenario demonstrates how the introduction of a massive passing star can significantly disturb this otherwise stable system, causing some planets to be ejected. The different outcomes between simulations are due to the random initial position of the passing star.

However, one thing can be noticed - the orbit of the planets seems to cease to go through the same points as the planets go for their sequential turns. A closer look at the inner planets (i.e. Mercury, Venus, Earth and Mars) confirms it. The Sun, which had no velocity whatsoever, starts to slowly swirl upwards which causes a shift in all orbits, but specifically in the orbits of the inner planets since they are closer and less heavier. This means that the whole system is not in equilibrium. The reason for this is the initial conditions where all planets start at the same position on the $y$ axis with positive velocity along the $x$ axis. As the bodies move, they exert force on the Sun and therefore the whole system gains a positive momentum upwards. To resolve this issue, one could either balance the system by choosing different initial conditions or counter balance the system by giving it a momentum downwards.

The model is of course a simplified representation of the Solar system, as it is restricted to two dimensions and relies on several assumptions regarding the initial conditions and the passing star's trajectory. Nevertheless, the simulations effectively demonstrate the complex and sensitive nature of gravitational interactions and the usefulness of numerical methods for studying them.
