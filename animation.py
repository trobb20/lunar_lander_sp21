import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate(data,length):

	# Animate a dataset for time length
	# Dataset format (X,Y) where X,Y are 1D vectors
	# Length of time in s

	#Calculate interval
	inter = int(1000*length/data.shape[1])

	#Set up plot
	fig, ax = plt.subplots()
	xdata, ydata = [], []
	ln, = plt.plot([], [], 'b-')

	#Initialize limits
	def init():
		ax.set_ylim(0, 5)
		ax.set_xlim(0, 10)
		return ln,

	#Data gen loops through data vector and returns individual values
	def data_gen(data):
		for i in range(data.shape[1]):
			yield (data[0,i],data[1,i])

	#Updates animation frames
	def update(frame):
		x,y=frame
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
		return ln,

	#Conduct animation using matplotlib
	ani = FuncAnimation(fig, update, data_gen(data),
					init_func=init, interval=inter, repeat=False, blit=True)

	return ani,plt