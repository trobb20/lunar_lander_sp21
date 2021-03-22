import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.collections import LineCollection

def animate(data,dt,length):

	# Animate a dataset for time length
	# Dataset format: (X,Y,thrusting) where X,Y are 1D vectors 
	#  		and thrusting reports whether the vehicle is
	#		thrusting (1 or 0)
	# dt: timestep
	# Length of time for animation to run in s


	sz = data.shape[1]
	if sz==0:
		print('No data, are you sure your object moved?')

	#Calculate interval
	inter = int(1000*length/sz)

	#Calculate time steps
	time = sz*dt
	time_points = [[],[]]
	ind=0
	for i in range(int(time)+1): #This plots the points that signify 1 s of time
		ind = int(i/dt)
		try:
			time_points[0].append(data[0,ind])
			time_points[1].append(data[1,ind])
		except IndexError:
			ind = int(i/dt)-1
			time_points[0].append(data[0,ind])
			time_points[1].append(data[1,ind])


	#Set up plot
	fig, ax = plt.subplots()
	colors=[] #these are the colors for thrusting or not thrusting
	segments=[] #segments are the points in the plot to add to the line collection
	xdata, ydata = [], [] #for animation
	ln, = plt.plot([], [], 'b-', alpha=0) #main line for animation (translucent as we are plotting line collection)
	lc = LineCollection(segments,colors=colors) #initialize the line collection
	ax.add_collection(lc) # add the line collection to the axis
	plt.plot(time_points[0],time_points[1],'ok') #plot time points

	#Initialize limits
	def init():
		ax.set_ylim(0, 5)
		ax.set_xlim(0, 10)
		return ln,

	#Data gen loops through data vector and returns individual values
	def data_gen(data):
		for i in range(sz):
			yield (data[0,i],data[1,i],data[2,i])

	#Updates animation frames
	def update(frame):
		x,y,thrusting=frame #each frame contains coords and thrust state
		xdata.append(x)
		ydata.append(y)

		# Resetting limits if approaching bounds
		xmin, xmax = ax.get_xlim()
		ymin, ymax = ax.get_ylim()

		if x >= xmax:
			ax.set_xlim(xmin,1.1*x)
			ax.figure.canvas.draw()
		if y >= ymax:
			ax.set_ylim(ymin,1.1*y)
			ax.figure.canvas.draw()

		#Update our line
		ln.set_data(xdata, ydata)

		#Color & line collection processing
		if thrusting and not len(xdata)<2:
			segments.append(((xdata[-2],ydata[-2]),(xdata[-1],ydata[-1])))
			colors.append((1,0,0)) #red
		elif not thrusting and not len(xdata)<2:
			segments.append(((xdata[-2],ydata[-2]),(xdata[-1],ydata[-1])))
			colors.append((0,0,1)) #blue

		lc.set_segments(segments) #add the segment to the line collection
		lc.set_color(colors)	  #add the color to the line collection

		return ln,

	#Conduct animation using matplotlib
	ani = FuncAnimation(fig, update, data_gen(data),
					init_func=init, interval=inter, repeat=False, blit=True, save_count=sz)

	return ani