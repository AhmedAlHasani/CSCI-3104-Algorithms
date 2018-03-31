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
		self.map3 = [None] * self.size #test table for plot with h1(x)
		self.map4 = [None] * self.size #test table for plot with h2(x)
		self.maxBucket1 = [] #list that will hold max buckets per 'n' for h1(x)
		self.maxBucket2 = [] #list that will hold max buckets per 'n' for h2(x)

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

	def add1(self, name):
			h1Value = self.Hash_Function1(name)
			index1 = h1Value%self.size
			if self.map1[index1] is None:
				self.map1[index1] = list([h1Value]) #list(), so to create a linkedList in case of collisions
				return True
			else:
				self.map1[index1].append(h1Value)
				return True

	def add2(self, name):
			h2Value = self.Hash_Function2(name)
			index2 = h2Value%self.size
			if self.map2[index2] is None:
				self.map2[index2] = list([h2Value]) #list(), so to create a linkedList in case of collisions
				return True
			else:
				self.map2[index2].append(h2Value)
				return True

	def print(self):
		for item in self.map1:
			if item is not None:
				print(str(item))
	
	def testPrint(self):
		i = 0
		for elements in self.map1:
			i+=1
		print(i)
		print(self.map1[self.size-1]) #last item is in 5700
	
	def histogram1(self):
		Xindices = np.arange(len(self.map1))		
		i = 0
		Yindices = []
		while i < self.size:
			if self.map1[i] is not None:
				Yindices.append(len(self.map1[i]))
			else:
				Yindices.append(0)
			i+=1
		plt.bar(Xindices, Yindices, color='g')
		plt.axis((0,300,0,800))
		plt.title("h1(x)")
		plt.xlabel("Buckets")
		plt.ylabel("No. of Names in Bucket")
		plt.show()

	def histogram2(self):
		Xindices = np.arange(len(self.map1))		
		i = 0
		Yindices = []
		while i < self.size:
			if self.map2[i] is not None:
				Yindices.append(len(self.map2[i]))
			else:
				Yindices.append(0)
			i+=1
		plt.bar(Xindices, Yindices, 2/3, color='g')
		plt.title("h2(x)")
		plt.xlabel("Buckets")
		plt.ylabel("No. of Names in Bucket")
		plt.axis((0,self.size,0,30))
		plt.show()
		
h = HashMap()
sequence = []
counter = 0
with open("dist.all.last.txt") as file:
	for line in file:
		sequence.append(line.split(None, 1)[0]) #take the word only
		counter += 1
halfSize = (counter-1)*0.5 #Total number of names = 88,799, we only want 50% random unique names.
						   #88,799-1 = 88,798. 50% of that is 44,399

largestBucket = []
largestBucket2 = []
count = 0
for name in random.sample(sequence, int(halfSize)): #return only 50% unique input from sequence
	h.add1(name)
	h.add2(name)
	count += 1
	if (count == halfSize): #stop when we return only 50% of input
		break

h.histogram1()
h.histogram2()