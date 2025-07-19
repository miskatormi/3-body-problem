# $3$-Body Problem – A Simple Simulation  
(Personal weekend project from 2024, README written and project published to GitHub 2025, Updated on 05/2025 for code efficiency)

During the summer, every normal university student starts to miss their classes (or... maybe not). In my case, I started to miss my mechanics classes and thought to myself:

**"How can I satisfy my need for Mechanics?"**

The answer was obviously to dive into the chaotic beauty of physics with a classic problem — the 3-Body Problem — and bring it to life using a bit of Python.

## Physical Theories Involved
  

- **Newton’s Second Law:**  
  $$\vec{F} = m \vec{a}$$  
  Used to relate force and acceleration for a given mass.

- **The $1/r^n$ - acceleration field (with $b=2$ and $a=G$ this is Newton's law of gravitation):**  
  $$\vec{F} = a\frac{mM}{r^b} \hat{r}$$  

- **Discrete approximation of acceleration:**  
  $$a = \frac{\Delta v}{\Delta t} \quad \Leftrightarrow \quad \Delta v= a\Delta t$$  
  A simple numerical estimate that gets better as $\Delta t$ decreases.

### A Bit More on What I’m Simulating  
The $3$-body problem — yes, it really is just that — is all about figuring out how $3$ masses move under each other’s force fields. Why simulate?:

> You can't solve it analytically.  
> It’s chaotic. It’s sensitive.  
> Change the starting conditions just a little, and you'll end up with a totally different outcome.

That’s what makes it fascinating. It sits right at the edge of classical mechanics and chaos theory. A seriously beautiful thing.

## Basic Function of the Python Code  

_Changed 05/2025:_ 

The simulation now mostly uses array operations to speed up the simulation:

### The **ACC-function** and what it does
$$
ACC: \mathcal X \times \mathcal M \rightarrow \mathcal A
$$
The ACC-function takes in two arrays or tensors. One made up of the position vectors of the particles as row vectors: $$ \mathcal X = \begin{bmatrix}
x_1 & y_1 & z_1\\
x_2 & y_2 & z_2 \\
\vdots & \vdots & \vdots \\
x_n & y_n & z_n
\end{bmatrix} $$
And one with made up of the masses of the particles
$$\mathcal M=  \begin{bmatrix} m_1 \\ m_2 \\ \vdots \\ m_n
\end{bmatrix}$$
The function then returns the acceleration vectors as row vectors in another array:
$$ \mathcal A =  \begin{bmatrix}
a_{x,1} & a_{y,1} & a_{z,1}\\
a_{x,2} & a_{y,2} & a_{z,2}\\
\vdots & \vdots & \vdots \\
a_{x,n} & a_{y,n} & a_{z,n}\\
\end{bmatrix}$$

### The Simulation using ACC-function
First, we initialize five tensors/arrays: position, velocity, acceleration, time, and mass. Initially, the first four consist of zeros which we update with a for-loop. The mass array consists of the masses of the $3$-bodies. 
The simulation repeats a simple cycle:
1. Update elapsed time to the time array. 
2. Update the acceleration to the acceleration array.
3. Using the saved acceleration and velocity array update position to the position array.

Finally, we plot all data to visualize the orbits.

## Some Results
In all the figures, the initial positions are marked with small dots, and the most recent with large ones. Here are some special cases:

### Total Chaos  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_3.png">
</p>

In this case, the motion seems completely chaotic with no clear pattern. However, so far, the bodies have remained relatively close to each other.

### Momentary Reduction to the Two-Body Problem  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_1.png">
</p>  

This shows what happens when the 3-body problem momentarily reduces to the two-body problem: the blue and yellow masses form a close bond and orbit each other. Their combined center of mass then orbits the green mass as if it were just a single object.

### Full Reduction to Two-Body Problem via Symmetry  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_5.png">
</p>

<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_6.png">
</p>

In these last cases, the 3-body problem fully reduces to a two-body scenario due to perfect balancing of forces from very specific initial conditions.

## Future of This Project?

I might revisit the simulation to improve and expand it. Exploring Lyapunov exponents could be an interesting next step or perhaps animate the simulation.
