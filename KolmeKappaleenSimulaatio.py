import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
fig, axis = plt.subplots()
fig2, axis2 = plt.subplots()
DELTA_t = 0.1
d = 100000
x1 = 0
y1 = 0
x2 = 1.001
y2 = 0
x3 = -1
y3 = 0
m1 = 10000000
m2 = 1000000
m3 = 1000000
v_1_x = 0
v_1_y = 0
v_2_x = 0
v_2_y = 0.03
v_3_x = 0
v_3_y = -0.03
x_1 = [x1]
y_1 = [y1]
x_2 = [x2]
y_2 = [y2]
x_3 = [x3]
y_3 = [y3]
v_1_xM = [v_1_x]
v_1_yM = [v_1_y]
v_2_xM = [v_2_x]
v_2_yM = [v_2_y]
v_3_xM = [v_3_x]
v_3_yM = [v_3_y]
t_t = [0]
axis.scatter(x1,y1,marker='.', color='blue')
axis.scatter(x2,y2,marker='.', color='orange')
axis.scatter(x3,y3,marker='.', color='green')
axis2.scatter(x1,y1,marker='.', color='blue')
axis2.scatter(x2,y2,marker='.', color='orange')
axis2.scatter(x3,y3,marker='.', color='green')

for i in range(1,d,1):
    T=DELTA_t
    t=DELTA_t*i
    t_t.append(t)
    F_1_x = 6.67259e-11*(((m1*m2)/(((np.sqrt((x1-x2)**2+(y1-y2)**2)))**3))*(x2-x1)+((m1*m3)/(((np.sqrt((x1-x3)**2+(y1-y3)**2))**3)))*(x3-x1))
    F_1_y = 6.67259e-11*(((m1*m2)/(((np.sqrt((x1-x2)**2+(y1-y2)**2)))**3))*(y2-y1)+((m1*m3)/(((np.sqrt((x1-x3)**2+(y1-y3)**2)))**3))*(y3-y1))
    F_2_x = 6.67259e-11*(((m1*m2)/(((np.sqrt((x1-x2)**2+(y1-y2)**2)))**3))*(x1-x2)+((m2*m3)/(((np.sqrt((x2-x3)**2+(y2-y3)**2)))**3))*(x3-x2))
    F_2_y = 6.67259e-11*(((m1*m2)/(((np.sqrt((x1-x2)**2+(y1-y2)**2)))**3))*(y1-y2)+((m2*m3)/(((np.sqrt((x2-x3)**2+(y2-y3)**2)))**3))*(y3-y2))
    F_3_x = 6.67259e-11*(((m3*m2)/(((np.sqrt((x3-x2)**2+(y3-y2)**2)))**3))*(x2-x3)+((m1*m3)/(((np.sqrt((x1-x3)**2+(y1-y3)**2)))**3))*(x1-x3))
    F_3_y = 6.67259e-11*(((m1*m3)/(((np.sqrt((x3-x1)**2+(y3-y1)**2)))**3))*(y1-y3)+((m2*m3)/(((np.sqrt((x2-x3)**2+(y2-y3)**2)))**3))*(y2-y3))
    a_1_x = F_1_x/m1
    x1 = 0.5*a_1_x*T**2+v_1_x*(DELTA_t)+x1
    x_1.append(x1)
    v_1_x = a_1_x*(DELTA_t)+v_1_x
    v_1_xM.append(v_1_x)

    a_1_y = F_1_y/m1
    y1 = 0.5*a_1_y*T**2+v_1_y*(DELTA_t)+y1
    y_1.append(y1)
    v_1_y = a_1_y*(DELTA_t)+v_1_y
    v_1_yM.append(v_1_y)

    a_2_x = F_2_x/m2
    x2 = 0.5*a_2_x*T**2+v_2_x*(DELTA_t)+x2
    x_2.append(x2)
    v_2_x = a_2_x*(DELTA_t)+v_2_x
    v_2_xM.append(v_2_x)

    a_2_y = F_2_y/m2
    y2 = 0.5*a_2_y*T**2+v_2_y*(DELTA_t)+y2
    y_2.append(y2)
    v_2_y = a_2_y*(DELTA_t)+v_2_y
    v_2_yM.append(v_2_y)

    a_3_x = F_3_x/m3
    x3 = 0.5*a_3_x*T**2+v_3_x*(DELTA_t)+x3
    x_3.append(x3)
    v_3_x = a_3_x*(DELTA_t)+v_3_x
    v_3_xM.append(v_3_x)

    a_3_y = F_3_y/m3
    y3 = 0.5*a_3_y*T**2+v_3_y*(DELTA_t)+y3
    y_3.append(y3)
    v_3_y = a_3_y*(DELTA_t)+v_3_y
    v_3_yM.append(v_3_y)
    
    continue
x_raja = x_1 + x_2 +x_3
x_raja = np.array(x_raja)
y_raja = y_1 + y_2 + y_3
y_raja = np.array(y_raja)
x_1 = np.array(x_1)
x_2 = np.array(x_2)
x_3 = np.array(x_3)
y_1 = np.array(y_1)
y_2 = np.array(y_2)
y_3 = np.array(y_3)
t_t = np.array(t_t)
v_1_xM = np.array(v_1_xM)
v_1_yM = np.array(v_1_yM)

anim_plot1, = axis.plot(x_1,y_1, label='$m_1$',color='blue')
anim_plot2, = axis.plot(x_2,y_2, label='$m_2$',color='orange')
anim_plot3, = axis.plot(x_3,y_3, label='$m_3$',color='green')
m1p = axis.scatter(x_1[0],y_1[0])
m2p = axis.scatter(x_2[0],y_2[0])
m3p = axis.scatter(x_3[0],y_3[0])
def up_data(frame):
    anim_plot1.set_data(x_1[:frame],y_1[:frame] )
    anim_plot2.set_data(x_2[:frame],y_2[:frame] )
    anim_plot3.set_data(x_3[:frame],y_3[:frame] )
    global m1p
    m1p.remove()
    m1p = axis.scatter(x_1[frame],y_1[frame], color='blue')
    global m2p
    m2p.remove()
    m2p = axis.scatter(x_2[frame],y_2[frame], color='orange')
    global m3p
    m3p.remove()
    m3p = axis.scatter(x_3[frame],y_3[frame], color='green')
    return anim_plot1, anim_plot2, anim_plot3, m1p, m2p, m3p,

animation = ani.FuncAnimation(fig=fig, func=up_data, frames=len(t_t), interval=0.1)

axis.set_xlim(min(x_raja),max(x_raja))
axis.set_ylim(min(y_raja),max(y_raja))
axis2.set_xlim(min(x_raja),max(x_raja))
axis2.set_ylim(min(y_raja),max(y_raja))

axis2.plot(x_1,y_1, label='$m_1$',color='blue')
axis2.plot(x_2,y_2, label='$m_2$',color='orange')
axis2.plot(x_3,y_3, label='$m_3$',color='green')
axis2.scatter(x1,y1, color='blue')
axis2.scatter(x2,y2, color='orange')
axis2.scatter(x3,y3, color='green')
axis2.set_title('Final frame')
axis.grid()
axis.set_xlabel('x')
axis.set_ylabel('y')
axis2.set_xlabel('x')
axis2.set_ylabel('y')
axis2.grid()
axis.legend()
axis2.legend()
plt.show()