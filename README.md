# Three-Body Problem – A Simple Simulation  
(2024 Personal Weekend Project, README written and project published to GitHub 2025)

During the summer, every normal university student starts to miss their classes (or... maybe not). But anyway, me being of the *normal* kind, I started to miss my mechanics classes and thought to myself:

**"How can I satisfy my need for Mechanics?"**

The answer was obviously to dive into the chaotic beauty of physics with a classic problem — the Three-Body Problem — and bring it to life using a bit of Python.

## Physical Theories Involved

### The Basics  
If you’ve ever cracked open a physics book (even in high school), the foundations will be familiar. Here’s what I used:

- **Newton’s Second Law:**  
  $$\vec{F} = m \vec{a}$$  
  Used to relate force and acceleration, given mass.

- **Newton’s Law of Gravitation:**  
  $$\vec{F}_g = \frac{GmM}{r^2} \hat{r}$$  
  The inverse square law to calculate gravitational forces between bodies.

- **Discrete approximation of velocity:**  
  $$v = \frac{\Delta x}{\Delta t}$$  
  A simple numerical estimate that gets better as $\Delta t$ gets smaller — a little nod to the derivative definition.

### A Bit More on What I’m Simulating  
The three-body problem — yes, it really is just that — is all about figuring out how three masses move under each other’s gravitational pull. Sounds easy enough until you realize:

> You can't solve it analytically.  
> It’s chaotic. It’s sensitive.  
> Change the starting conditions just a little, and you'll end up with a totally different outcome.

That’s what makes it fascinating. It sits right at the edge of classical mechanics and chaos theory. A seriously beautiful thing.

Of course, there are probably much more elegant ways to approach the problem — like from a pure math perspective — but since this was a project from my first year, I had no idea about such things at the time.

## Basic Function of the Python Code  
(Not a genius (yet) when it comes to Python, but I tried my best)

The simulation follows a rather simple pattern:

1. **Initialization:**  
   The program is given a bunch of initial conditions and parameters. The most important is probably $\Delta t$, which determines the time step for each position calculation.

2. **First frame:**  
   The initial conditions are stored as a single element in a list. Then, in a `for` loop (where the magic happens), the simulation starts to calculate the gravitational forces in all directions for all the masses at time $t = 0$. Using Newton’s second law, acceleration is then computed.

3. **A big "but":**  
   This simulation assumes that the force (and thus acceleration) stays constant during the $\Delta t$ time jump. This means that for large $\Delta t$ values or very rapidly changing systems, the simulation becomes inaccurate. Still, we continue and calculate the new position with:  
   $$x_n = \frac{1}{2}a_{n-1} t^2 + v_{n-1}t + x_{n-1}$$  
   where $x_n$ is the position at time $t = \Delta t \cdot n$.

4. **Appending results:**  
   This position is added to the list of positions $x_n$ for all times $t = \Delta t \cdot n$.

5. **Plotting:**  
   The lists are converted into NumPy arrays and plotted using Matplotlib. The result is an animation showing the full evolution of the system, followed by a static final frame (depending on how many steps $d$ you ask the program to calculate).

## Some Results, With Tiny Analysis  
In all the figures, the initial positions are marked with small dots, and the most recent positions with large dots. Here are some (to me) special cases that I can comment on:

### Approximate Two-Body Problem  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_1.png">
</p>  

Here you can see what happens when the three-body problem approximately reduces to a two-body problem: the blue and yellow masses form a close bond and orbit each other. Their combined center of mass then orbits the green mass as if it were just a single object.

### Total Chaos  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_3.png">
</p>

In this case, the motion seems completely chaotic with no clear pattern. However, so far, the bodies have remained relatively close to each other.

### Full Reduction to Two-Body Problem via Symmetry  
<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_5.png">
</p>

<p align="center">
    <img width="640" height="480" src="https://github.com/miskatormi/Three-body-problem/blob/main/Figure_6.png">
</p>

In these last cases, the three-body problem fully reduces to a two-body scenario due to perfect balancing of forces from very specific initial conditions.

## Future of This Project?

I might, on a rainy (sunny?) day, revisit the simulation — hopefully much wiser — to improve and expand it. Exploring Lyapunov exponents could be an interesting next step. Maybe I’ll even incorporate some data analysis to better understand the results.

Let’s see how busy life makes me...
