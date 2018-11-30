#Name: Vidhathri
#Roll Number: CED15I014
#Question : Ellipse inside a circle touching the circle at two points


import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import random

def main():
	x = int(random.random()*10)
	y = int(random.random()*10)

	cen = (x,y)

	width = 10			#Horizontal axis of ellipse
	height = 4			#Vertical axis of ellipse

	if width>height:
		r = width/2
	elif width<height:
		r = height/2
	else:
		height+=1
		r = height/2

	plt.figure()
	plt.axes()
	ell = Ellipse(xy=cen,width=width,height=height,fill = 0)
	plt.gca().add_patch(ell)
	circle = plt.Circle(cen,r,fill=0)
	plt.gca().add_patch(circle)
	plt.axis('scaled')
	plt.title('Ellipse inside circle')
	plt.show()

main()