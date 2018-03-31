import random
import string
from random import randint
import matplotlib.pyplot as plt
import numpy as np

table1 = []
#table2 = []
i = 1
size = []
while i <= 5701:
	if i%2 != 0:
		size.append(i)
	i+=1
class HashMap():
	def __init__(self):
		self.LTable1 = [] #hold 'l' values for h1(x)
		self.LTable2 = [] #hold 'l' values for h2(x)
		self.collisionTable1 = [] #list that will hold collisions per 'l' for h1(x)
		self.collisionTable2 = [] #list that will hold collisions per 'l' for h2(x)

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

	def createMap(self, lengthIndex):
		hashTable = [None] * lengthIndex
		return hashTable

	def findCollisions(self, hashTable , lengthIndex):
		i = 0
		collisions = 0
		while i < lengthIndex:
			if hashTable[i] is not None:
				collisions += len(hashTable[i])
			i+=1
		return (collisions-lengthIndex) #take away the number of elements in index 'i'

	def addPlot_h1(self, sequence , lengthIndex):
		hashTable = self.createMap(lengthIndex)
		for elements in sequence:
			h1Value = self.Hash_Function1(elements)
			index1 = h1Value%lengthIndex
			if hashTable[index1] is None:
				hashTable[index1] = list([h1Value]) #list(), so to create a linkedList in case of collisions
			else:
				hashTable[index1].append(h1Value)
		collisions = self.findCollisions(hashTable, lengthIndex)
		self.LTable1.append(lengthIndex)
		self.collisionTable1.append(collisions)
	
	def addPlot_h2(self, sequence , lengthIndex):
		hashTable = self.createMap(lengthIndex)
		for elements in sequence:
			h1Value = self.Hash_Function2(elements)
			index1 = h1Value%lengthIndex
			if hashTable[index1] is None:
				hashTable[index1] = list([h1Value]) #list(), so to create a linkedList in case of collisions
			else:
				hashTable[index1].append(h1Value)
		collisions = self.findCollisions(hashTable, lengthIndex)
		self.LTable2.append(lengthIndex)
		self.collisionTable2.append(collisions)

	def linePlot1(self):
		plt.plot(self.LTable1, self.collisionTable1)
		plt.title("l vs. collisions h1(x)")
		plt.xlabel("l")
		plt.ylabel("collisions")
		plt.show()

	def linePlot2(self):
		plt.plot(self.LTable2, self.collisionTable2)
		plt.title("l vs. collisions h2(x)")
		plt.xlabel("l")
		plt.ylabel("collisions")
		plt.show()

	def print(self):
		for item in self.map1:
			if item is not None:
				print("PRINTING" + str(item))

h = HashMap()
sequence = []
counter = 0
with open("dist.all.last.txt") as file:
	for line in file:
		sequence.append(line.split(None, 1)[0]) #take the word only

count = 0
lengthIndex = 2
collisions = 0
while lengthIndex <= 5701:
	if lengthIndex%2 != 0 or lengthIndex == 2:
		h.addPlot_h1(sequence, lengthIndex)
		h.addPlot_h2(sequence, lengthIndex)
	lengthIndex+=1
h.linePlot1()
h.linePlot2()