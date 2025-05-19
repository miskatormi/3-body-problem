import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import matplotlib as mpl
from scipy.optimize import curve_fit
import timeit

start = timeit.default_timer()
fig2, axis2 = plt.subplots()

DELTA_t = 0.0001 # Time jump between steps
d = 300000 # Number of steps
tm = 0 # Number of test masses
sp = 0.1 # Perturbation of test masses
n = 3+tm # Enter number of masses
colormap = 'Set1'

def EUCNORM(x):
    n1, n2, n3 = np.shape(x)
    result = np.zeros((n1,n3))
    for i in range(n1):
        for j in range(n3):
            result[i,j]=np.sqrt(np.sum(x[i,:,j]**2))
    return result

def ACC(x,m,r=2,G=6.67259e-11): #(1/x^r acceleration) This function takes in a placement tensor of rank 2 and a mass vector to return a tensor of rank 2 which includes accelerations to all n1 particles in all 3 dimensions.
    n1, n2 = np.shape(x)
    result = np.zeros((n1, n2))
    d = r+1
    for r in range(n2):
        for j in range(n1):
            for i in range(n1):
                if i==j:
                    continue
                else:
                    result[j,r] = result[j,r] + G*(((m[i])/((np.sqrt(np.sum(np.square(x[i,:]-x[j,:]))))**d))*(x[i,r]-x[j,r]))
    return result

x = np.zeros((n,2,d))
v = np.zeros((n,2,d))
a = np.zeros((n,2,d))
t = np.zeros(d)
x[:n,:,0] = np.array([[1,1],[0,0],[-1,-1]]) 
v[:n,:,0] = np.array([[-0.5,0.5],[0,0],[0.5,-0.5]]) #()
m = np.array([100,1000,100]) #(m_1,...,m_n)
  
for i in range(d-1): #The actual simulation saves time, position, velocity and acceleration data
    t[i]=DELTA_t*i
    a[:,:,i] = ACC(x[:,:,i],m,G=6.3e-3)
    x[:,:,i+1] = 0.5*a[:,:,i]*DELTA_t**2+v[:,:,i]*DELTA_t+x[:,:,i]
    v[:,:,i+1] = a[:,:,i]*DELTA_t + v[:,:,i]

axis2.set_ylim(1.1*np.min(x[:,0,:]),1.1*np.max(x[:,0,:]))
axis2.set_xlim(1.1*np.min(x[:,1,:]),1.1*np.max(x[:,1,:]))

colors = mpl.colormaps[colormap](np.linspace(0,1,n))

for i in range(n):
    axis2.plot(x[i,0,:],x[i,1,:], label='$m_'+str(i)+'$', color=colors[i])
    axis2.scatter(x[i,0,d-1],x[i,1,d-1],marker='o', color=colors[i])
    axis2.scatter(x[i,0,0],x[i,1,0],marker='.', color=colors[i])

axis2.grid()
axis2.set_xlabel('x')
axis2.set_ylabel('y')
axis2.set_title('Final frame')
axis2.legend()


stop=timeit.default_timer()
print('Runtime:', stop-start)
plt.show()