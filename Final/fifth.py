import math
import random

def hit(people, all_distances):
	hit = []
	person_index = 0
	for individual_distances in all_distances:
		one_row = individual_distances # store each row
		minimum_distance = 10000 #some big number larger than our distances
		for distance in one_row:
			if distance < minimum_distance:
				minimum_distance = distance
		index = one_row.index(minimum_distance)
		person_hit_who = [people[person_index], people[index]]
		hit.append(person_hit_who)
		person_index += 1
	return hit

def create_distances(people):
	n_squared = len(people)*len(people)
	#generate random unique distances according to how many ppl are there in the list above
	unique_distances = random.sample(range(1, n_squared+1), n_squared)
	i = 0
	x = 0

	#generate 2d list of distances, grab no. from the unique_distances
	complete_distances = [[ 0 for x in range(len(people))] for y in range(len(people))]
	while i < len(unique_distances):  
		while x < len(people):
			y = 0
			while y < len(people):
				complete_distances[x][y] = unique_distances[i] 
				i += 1
				y += 1
			x = x + 1

	# people cant have distances with themselves
	i = 0
	while i < len(people):
		complete_distances[i][i] = math.inf
		i+=1

	#match distances
	x = 0
	while x < len(people):
		y = 0
		while y < len(people):
			complete_distances[x][y] = complete_distances[y][x] 
			y += 1
		x = x + 1

	return complete_distances

def true_or_false(results, people):
	boolean_list = []
	for pair in results:
		boolean_list.append(pair[-1])#grab the 2nd person in the pair

	boolean = "False"
	for person in people:
		if person not in boolean_list:
			print("Not Hit: ", person)
			boolean = "True"
	return boolean

people = ['a', 'b', 'c', 'd', 'e'] #5 people
complete_distances = create_distances(people)
print(complete_distances)
results = hit(people, complete_distances)
print(results)
final_result = true_or_false(results, people)
print(final_result)