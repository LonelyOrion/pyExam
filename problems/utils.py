import time
import random

class IDGenerator():
	def getRandomID(self):
		myID = str(int(time.time()))
		for i in range(0, 8):
			myID += (random.choice('0123456789'))
		return myID