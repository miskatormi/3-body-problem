import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import timeit

start = timeit.default_timer()
axis2 = plt.figure().add_subplot(projection='3d')

DELTA_t = 0.0001 # Time jump between steps
d = 300000 # Number of steps
n = 3
colormap = 'Set1'

def Acceleration(x,m,r=2,G=6.67259e-11): #(1/x^r acceleration) This function takes in a position tensor of rank 2 and a mass vector to return a tensor of rank 2 which includes accelerations to all n1 particles in all 3 dimensions.
    x = np.asarray(x, dtype=float)
    m = np.asarray(m, dtype=float)
    d = x[np.newaxis,:,:] - x[:,np.newaxis,:]
    norm = np.sqrt (np.sum(d**2, axis=2 ))
    np.fill_diagonal(norm, np.inf)
    norm_1 = 1/norm**(r+1)
    return np.sum( G * m[np.newaxis , :, np.newaxis] * norm_1[:, :, np.newaxis] * d , axis=1)

x = np.zeros((n,3,d))
v = np.zeros((n,3,d))
a = np.zeros((n,3,d))
t = np.zeros(d)
x[:n,:,0] = np.array([[1,0,0],[0,0,0],[-1,0,0]]) 
v[:n,:,0] = np.array([[0,-0.25,0],[0,0,0],[0,0.25,0]]) #()
m = np.array([100,100,100]) #(m_1,...,m_n)

for i in range(d-1): #The simulation saves time, position, velocity and acceleration data
    t[i]=DELTA_t*i
    a[:,:,i] = Acceleration(x[:,:,i],m,G=6.3e-4)
    x[:,:,i+1] = 0.5*a[:,:,i]*DELTA_t**2+v[:,:,i]*DELTA_t+x[:,:,i]
    v[:,:,i+1] = a[:,:,i]*DELTA_t + v[:,:,i]

axis2.set_ylim(1.1*np.min(x[:,0,:]),1.1*np.max(x[:,0,:]))
axis2.set_xlim(1.1*np.min(x[:,1,:]),1.1*np.max(x[:,1,:]))

colors = mpl.colormaps[colormap](np.linspace(0,1,n))

for i in range(n):
    axis2.plot(x[i,0,:],x[i,1,:],x[i,2,:], label='$m_'+str(i)+'$', color=colors[i])
    axis2.scatter(x[i,0,d-1],x[i,1,d-1],x[i,2,d-1],marker='o', color=colors[i])
    axis2.scatter(x[i,0,0],x[i,1,0],x[i,2,0],marker='.', color=colors[i])

axis2.grid()
axis2.set_xlabel('x')
axis2.set_ylabel('y')
axis2.set_title('Final frame')
axis2.legend()


stop=timeit.default_timer()
print('Runtime:', stop-start)
plt.show()