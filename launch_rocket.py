import numpy as np

def launch_rocket(m,x0,v0,t,dt):

	#	Launch a "rocket" that is capable of thrusting
	#	Inputs:
	#		m: mass (kg)
	#		x0: initial position vector (m)
	#		v0: initial velocity vector (m/s)
	#		t: length of simulation (s)
	#		dt: Timestep of simulation (s)
	#	Description:
	#		This function prompts the user to input the
	#		forces they'd like to have on their body
	#		user gives a start and end time for each
	#		force/thrust and then impulse and momentum laws
	#		are applied to simulate the body's flight
	#
	#		NOTE: time to thrust is rounded to decimal size of dt.
	#		Meaning you cannot thrust for 0.99s if your step is 0.1s
	#	Output:
	#		Function outputs a matrix (X,Y,T)
	#		with x position coords, y position coords
	#		and the thrusting boolean, 0 or 1 depending on 
	#		whether the body is thrusting at that timestep

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

	#Get number of decimal places in dt so that we can round force times
	decimals = len(str(dt).split('.')[1])

	#Conduct simulation
	for i in range(length):

		current_time = i*dt #Increment time

		if force_index<len(forces): #If there are still forces to process

			# Start and end times of the thrust
			# Rounded to number of decimals in dt to ensure they are processed.
			thrust_start_time = round(forces[force_index][1],decimals)
			thrust_end_time = thrust_start_time + round(forces[force_index][2],decimals)

			if current_time==thrust_start_time: #If we're at the start of a thrust
				thrusting=1 								
				current_force=current_force+forces[force_index][0]	 #Add that force to our force sum
			elif current_time==thrust_end_time: #If we're at the end of a thrust
				thrusting=0
				current_force=current_force-forces[force_index][0] #Subtract that force from our force sum
				force_index=force_index+1		#Go to the next thrust

		v = v + (current_force*dt)/m 	#Impulse = change in momentum
		x = x + v*dt	     		 	#update position

		if x[1]<0: #If we hit the ground, end the simulation
			X=X[0:i]
			Y=Y[0:i]
			T=T[0:i]
			break

		X[i] = x[0] #Update data
		Y[i] = x[1]
		T[i] = thrusting


	return np.array([X,Y,T])
