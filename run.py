#Run
import numpy as np
from animation import animate
from launch import launch_body

# Test #
#Hit a 60g tennis ball at 100mph from height 2m

m=60/1000
x0=np.array([0,2])
v0=np.array([44,0])
t=5
dt=0.01
myLaunch = launch_body(m,x0,v0,t,dt)

#length of animation in seconds
animation_time = 4

animate(myLaunch,animation_time)