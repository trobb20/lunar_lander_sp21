import numpy as np

def launch_rocket(m,x0,v0,t,dt):
	#Get thrusts
	forces = []
	numThrusts=int(input('How many thrusts?: '))
	for i in range(0,numThrusts):
		print('Thrust number %d'%(i+1))
		print('------------------------')

		thrustTime = float(input('Time to start thrust in seconds: '))
		thrustDur = float(input('Duration of thrust in seconds: '))

		thrustX = float(input('Force (N) to thrust in X: '))
		thrustY = float(input('Force (N) to thrust in Y: '))

		force = np.array([thrustX,thrustY])
		forces.append([force,thrustTime,thrustDur])

	
	#Start sim
	g=-9.81 #Gravity
	length = int(t/dt) #Number of steps
	X=np.zeros(length) #initialize data vectors
	Y=np.zeros(length)
	T=np.zeros(length)

	#Force vector is only gravity for now
	current_force = np.array([0,g*m])
	force_index = 0

	#Initialize position and velocity vectors
	x = x0
	v = v0

	#Thrusting
	thrusting = 0

	#Conduct simulation
	for i in range(length):

		current_time = i*dt

		if force_index<len(forces):
			if current_time==forces[force_index][1]:
				thrusting=1
				current_force=current_force+forces[force_index][0]
			elif current_time==forces[force_index][1]+forces[force_index][2]:
				thrusting=0
				current_force=current_force-forces[force_index][0]
				force_index=force_index+1

		v = v + (current_force*dt)/m #Newton's second law rewritten
		x = x + v*dt	     #update position

		if x[1]<0: #If we hit the ground, end the simulation
			X=X[0:i]
			Y=Y[0:i]
			T=T[0:i]
			break
		X[i] = x[0] #Update data
		Y[i] = x[1]
		T[i] = thrusting


	return np.array([X,Y,T])
