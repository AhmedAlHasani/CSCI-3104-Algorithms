import random
import string
from random import randint
import matplotlib.pyplot as plt
import numpy as np

class HashMap():
	def __init__(self):
		self.size = 5701 #fixed
		self.map1 = [None] * self.size
		self.map2 = [None] * self.size
		self.maxBucket1 = [] #list that will hold max buckets per 'n' for h1(x)
		self.maxBucket2 = [] #list that will hold max buckets per 'n' for h2(x)
		self.iList = []
		i = 0
		while i < 88799:
			self.iList.append(i)
			i+=1

	def Hash_Function1(self, name):
		total = 0
		for letter in name:
			total += (ord(letter)-64) #ascii values for capital letters
		return total

	def Hash_Function2(self, name):
		total = 0
		for letter in name:
			total += (ord(letter)-64) #ascii values for capital letters
		# print(total*randint(0, 5700))
		return total*randint(0, 5700)

	def addPlot_h1(self, name):
		h1Value = self.Hash_Function1(name)
		index1 = h1Value%self.size
		if self.map1[index1] is None:
			self.map1[index1] = list([h1Value]) #list(), so to create a linkedList in case of collisions
			return True
		else:
			self.map1[index1].append(h1Value)
			return True

	def addPlot_h2(self, name):
			h2Value = self.Hash_Function2(name)
			index2 = h2Value%self.size
			if self.map2[index2] is None:
				self.map2[index2] = list([h2Value]) #create a linkedList in case of collisions
				return True
			else:
				self.map2[index2].append(h2Value)
				return True

	def findMaxBucket1(self):
		i = 0
		maximumNumber = -100
		while i < self.size:
			if self.map1[i] is not None:
				if len(self.map1[i]) > maximumNumber:
					maximumNumber = len(self.map1[i])
				#print(self.maxBucket1[i])
			i+=1
		self.maxBucket1.append(maximumNumber)

	def findMaxBucket2(self):
		i = 0
		maximumNumber = -100
		while i < self.size:
			if self.map2[i] is not None:
				if len(self.map2[i]) > maximumNumber:
					maximumNumber = len(self.map2[i])
				#print(self.maxBucket1[i])
			i+=1
		self.maxBucket2.append(maximumNumber)

	def linePlot1(self):
		plt.plot(self.iList, self.maxBucket1)
		plt.title("n elements vs. longest chain h1(x)")
		plt.xlabel("n elements")
		plt.ylabel("longest chain")
		plt.show()

	def linePlot2(self):
		plt.plot(self.iList, self.maxBucket2)
		plt.title("n elements vs. longest chain h2(x)")
		plt.xlabel("n elements")
		plt.ylabel("longest chain")
		plt.show()

h = HashMap()
sequence = []
counter = 0
with open("dist.all.last.txt") as file:
	for line in file:
		sequence.append(line.split(None, 1)[0]) #take the word only


#count = 0

for name in sequence:
	h.addPlot_h1(name)
	h.addPlot_h2(name)
	h.findMaxBucket1()
	h.findMaxBucket2()
	#print("Calling Bucket :" + str(count))
	#h.addPlot_h2(name)
	#h.findMaxBucket2()
	#count += 1
#print(count)

h.linePlot1()
h.linePlot2()