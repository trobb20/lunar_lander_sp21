#Run
import numpy as np
from animation import animate
from launch_rocket import launch_rocket
from IPython.display import HTML

# Test #
#Drop a 10kg rocket from 100m with small initial x velocity

m=10
x0=np.array([0,100])
v0=np.array([1,0])
t=5
dt=0.1
myLaunch = launch_rocket(m,x0,v0,t,dt)

#length of animation in seconds
animation_time = 4

ani=animate(myLaunch,dt,animation_time)

print('#########################')
print('####### Animation #######')
print('#########################')

HTML(ani.to_jshtml())