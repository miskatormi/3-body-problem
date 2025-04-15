# Three-Body Problem – A Simple Simulation (2024, Personal Weekend Project, Readme written and project published to Github 2025)

During the summer, every normal university student starts to miss their classes (or... maybe not). But anyway, me being of the *normal* kind, I started to miss my mechanics classes and thought to myself:

**"How can I satisfy my need for Mechanics?"**

The answer was obviously to dive into the chaotic beauty of physics with a classic problem — **the Three-Body Problem** — and bring it to life using a bit of Python.



##  Physical Theories Involved

### The Basics
If you’ve ever cracked open a physics book (even in high school), the foundations will be familiar. Here’s what I used:

- **Newton’s Second Law:**  
  $$\vec{F} = m \vec{a}$$  
  Used to relate force and acceleration, given mass.

- **Newton’s Law of Gravitation:**  
  $$\vec{F}_g = \frac{GmM}{r^2} \hat{r}$$  
  The good ol’ inverse square force field to calculate gravitational forces between bodies.

- **Discrete approximation of velocity:**  
  $$v = \frac{\Delta x}{\Delta t}$$  
  A simple numerical estimate that gets better as $\Delta t$ gets smaller — a little nod to the derivative definition.



### A Bit More on What I’m Simulating

The three-body problem — yes, it really is just that — is all about figuring out how three masses move under each other’s gravitational pull. Sounds easy enough until you realize:

> You **can’t solve it analytically**.  
> It’s chaotic. Sensitive. 
> Change the starting conditions just a *little*, and you'll end up with a totally different outcome.

That’s what makes it fascinating. It sits right at the edge of classical mechanics and chaos theory. A seriously beautiful thing...

To note that there most likely are more beautiful ways of looking at the problem, like from a pure math point of view, but since it is a project from my first year I had no idea of such things.



##  Basic Function of the Python Code  
*(Not a genius (yet) when it comes to Python, but I tried my best)*

The simulation follows a rather simple pattern:  
1. Firstly the program is given a massive amount of initial conditions and parameters. Most imporant of them is probably the $\Delta t$ which determines when the next position is calculated.
2. Secondly it takes these initial conditions which are added as an only element to a list. Then the program proceeds to a for loop, where the magic happends. In the loop we start to calculate the force in all direction for all the masses at the time $$t=0$$, then using Newtons 2nd law we calculate acceleration.
3. Now the big "but". This simulation assumes that the force stays (i.e acceleration stays) constant during the $\Delta t$ time jump we do in time with every position calculated. This means for big $\Delta t$ or for extremely fast changing systems this simulation is not really good for anything... Despite this we continue to calculate the new position with the formula:
  $$x_{n}=1/2*a_{n-1} t^2+v_{n-1}t +x_{n-1}$$, the position $x_n$ begin the position at the time $t= \Delta  t \cdot n$
4. This position is the added to the list of the positions $x_n$ at the times $t= \Delta  t \cdot n$
5. Then the lists are converted to Numpy arrays and plotted using Matplotlib. Matplotlib shows a animation of the full evolution and then the final frame (depending how many steps $d$ you inserted for the program to calculate)



##  Some Results, with tiny analysis  






##  Future of This Project?

I might, on a rainy (sunny?) day, revisit the simulation (hopefully much wiser) to improve and expand it (Lyapunov exponents could be something that the project could get still). Maybe I’ll even incorporate some data analysis into the results to understand the system better.

Let’s see how busy life makes me...
