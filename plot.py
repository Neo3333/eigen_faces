import matplotlib.pyplot as plt 

if __name__ == "__main__":
	plt.xlim(xmax = 5,xmin = -1)
	plt.ylim(ymax = 5,ymin = -1)
	plt.plot([2,3,3],[2,3,0],'k+')
	plt.plot([0,2,0],[0,0,2],'rx')
	plt.show()