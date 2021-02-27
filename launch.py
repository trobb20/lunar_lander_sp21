import numpy as np

def launch_body(m,x0,v0,t,dt):
	# Launch a body with parameters
	# mass m (kg)
	# initial position vector x0 (m,m)
	# initial velocity vector y0 (m/s,m/s)
	# length of simulation t (s)
	# simulation step size (s)

	g=-9.81 #Gravity
	length = int(t/dt) #Number of steps
	X=np.zeros(length) #initialize data vectors
	Y=np.zeros(length)

	#Force vector is only gravity for now
	force = np.array([0,g*m])

	#Initialize position and velocity vectors
	x = x0
	v = v0

	#Conduct simulation
	for i in range(length):

		v = v + (force*dt)/m #Newton's second law rewritten
		x = x + v*dt	     #update position

		if x[1]<0: #If we hit the ground, end the simulation
			X=X[0:i]
			Y=Y[0:i]
			break

		X[i] = x[0] #Update data
		Y[i] = x[1]

	return np.array([X,Y])
