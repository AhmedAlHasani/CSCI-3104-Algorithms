#First Problem

import random

def merge(A, B):
    final_sorted = [] #new list that will be sorted in the end
    length_A = len(A)
    length_B = len(B)
    i = 0
    j = 0
    while i < length_A and j < length_B: #do until we reach the end of either list A and B
        if A[i] <= B[j]: #if element B is less than element A
            final_sorted.append(A[i]) #then just add it to the final list
            i += 1 #to keep count where we are at in list A

        else: #otherwise, if A is greater than B
            global final_count
            final_count = final_count + (len(A) - i) # len(A) - i = how many reverse pairs at each iteration
            final_sorted.append(B[j])
            j += 1 #to keep count where we are at in list B

    if i == length_A: # No more elements to look at in A
        final_sorted.extend(B[j:]) #therefore, add elements in B to final_sorted since we already added A
    
    else: #if there are remaining elements in A
        final_sorted.extend(A[i:]) #then add them to the final list since we already added B
    return final_sorted 

def mergeSort(A):
    length = len(A)
    half_length = int(length/2)
    if length > 1:
        first_half = mergeSort(A[:half_length]) #keeps dividing the problem until one element remains
        second_half = mergeSort(A[half_length:]) #keeps dividing the other half of the problem until one element remains
        return merge(first_half,second_half) #recursively merge the individual elements
    else:
        return A

final_count = 0
random_list = []
i = 0
for i in range(100):
    random_list.append(random.randrange(0,250)) #genreate random numbers between 0 and 10,000
print(random_list)
mergeSort(random_list)
print("\n")
print("Reverse Pairs Count: ", final_count)

#Second Problem
import random
import networkx as nx

#to allow ford_fulkerson(), we need to decrease capacity by the flow from g_prime
def g_hat(G, people, issues):
	start = "source"
	for people_data in people:
		person = people_data[0]
		capacity1 = people_data[2]
		flow1 = people_data[1]

		#new capacity is c(e) - l(e)
		G[start][person]['capacity'] = capacity1 - flow1 
		
		#get rid of l(e), and set it to 0
		G[start][person]['flow'] = 0

		#keep a global counter
		global count1
		count1 = count1 + G[start][person]['capacity']

	for people_data in people:
		person = people_data[0]
		#print edge data 
		print("Source to People: ", G.get_edge_data(start, person))

	end = "sink"
	for issue_data in issues:
		issue = issue_data[0]
		capacity1 = issue_data[2]
		flow1 = issue_data[1]

		#new capacity is c(e) - l(e)
		G[issue][end]['capacity'] = capacity1 - flow1 
		
		#get rid of l(e), and set it to 0
		G[issue][end]['flow'] = 0

		#keep a global counter
		global count2
		count2 = count2 + G[issue][end]['capacity']

	for issue_data in issues:
		issue = issue_data[0]
		#print edge data 
		print("Issues to Sink: ", G.get_edge_data(issue, end))
	
	return G

def g_prime(G, people, issues):
	not_here = [] #if there was a person without any opinions
	
	#check for those individuals then
	for person in people:
		person = person[0]
		if person not in G: #
			not_here.append(person)

	 #if a person does not have an opinion he/she is not added
	print("\n")
	print("People Not Included in Graph: ", not_here)

	start = "source"
	for person_data in people:
		#edge between source and a person
		person = person_data[0]
		G.add_edge(start, person, capacity = person_data[2])

		#each edge's flow equal to minimum for that person
		G[start][person]['flow'] = person_data[1]

		#set demand for each node P to flow
		person_data[3] = person_data[1]

	end = "sink"
	for issue_data in issues:
		#edge between issue and sink
		issue = issue_data[0]
		G.add_edge(issue, end, capacity = issue_data[2])

		##each edge's flow equal to minimum for that issue
		G[issue][end]['flow'] = issue_data[1]

		#set demand for each node I to flow
		issue_data[3] = issue_data[1]

	return G

#Create G graph
def create_graph():
	G = nx.DiGraph()

	#create 1000 ppl, from 1 to 1000
	people_initially = list(range(1, 1001))
	
	 #create 10 issues, from 1 to 10
	global issues
	issues = list(range(1, 11))
	
	#create a list of issues with stored information
	i = 0
	for issue in issues:
		issue_1 = "issue" + str(issue)
		#minimum issues random number between 299 and 401 (exclusive)
		issue_2 = random.randint(299, 401)
		#maximum issues random number between 299 and 401 (exclusive)
		issue_3 = random.randint(499, 701)

		#store issue, lower limit, max. limit, and demand of 0
		issues[i] = [issue_1, issue_2, issue_3, 0]
		i += 1

	#connect people to issues in a graph G
	for person in people_initially:
		h_p = 0
		for issue in issues:
			if random.randint(1, 10) in (1, 2, 3, 4, 5): #if 50%

				#add edge between person and issue 
				G.add_edge(person, issue[0], capacity = 1.0) 
				
				 #count how many issues for each person
				h_p += 1
		
		#minimum issues
		b_p = (int)(h_p/2)
		
		#maximum issues
		t_p = h_p

		#store the person, max. issues and min, and 0 for demand initially
		person_parameter = [person, b_p, t_p, 0]
		
		#then add them to the whole list
		global people
		people.append(person_parameter)
	return G

people = [] #empty list for people
issues = [] #empty list for issues
count1 = 0
count2 = 0
G = create_graph() #test case, as required part(e)
G = g_prime(G, people, issues)
G = g_hat(G, people, issues)
print("Total Demand on People Nodes: ", count1)
print("Total Demand on Issues Nodes: ",count2)
R = nx.ford_fulkerson(G, 'source', 'sink')
print("Max Flow: ", R[0])
print("\n")
if count1 != count2:
	print("The Two Demands are not Equal")
	print("Hence, may not be feasible survey")



#Fourth Problem

import networkx as nx

def createGraph(G):
	#adding an edge also adds the node
	G.add_edge('Spider', 'A', weight=1.0)
	G.add_edge('Spider', 'H', weight=1.0)
	G.add_edge('Spider', 'J', weight=1.0)

	G.add_edge('H', 'G', weight=1.0)
	G.add_edge('H', 'K', weight=1.0)

	G.add_edge('G', 'L', weight=1.0)
	G.add_edge('G', 'F', weight=1.0)

	G.add_edge('F', 'E', weight=1.0)

	G.add_edge('E', 'Fly', weight=1.0)

	G.add_edge('J', 'S', weight=1.0)
	G.add_edge('J', 'K', weight=1.0)

	G.add_edge('K', 'L', weight=1.0)
	G.add_edge('L', 'M', weight=1.0)
	G.add_edge('M', 'N', weight=1.0)
	G.add_edge('M', 'F', weight=1.0)

	G.add_edge('N', 'O', weight=1.0)
	G.add_edge('N', 'E', weight=1.0)

	G.add_edge('O', 'Fly', weight=1.0)

	G.add_edge('A', 'S', weight=1.0)
	G.add_edge('A', 'B', weight=1.0)

	G.add_edge('B', 'R', weight=1.0)
	G.add_edge('B', 'C', weight=1.0)

	G.add_edge('S', 'R', weight=1.0)
	G.add_edge('R', 'Q', weight=1.0)

	G.add_edge('Q', 'C', weight=1.0)
	G.add_edge('Q', 'P', weight=1.0)

	G.add_edge('C', 'D', weight=1.0)
	G.add_edge('D', 'Fly', weight=1.0)
	G.add_edge('P', 'D', weight=1.0)
	G.add_edge('P', 'O', weight=1.0)
	G.add_edge('O', 'Fly', weight=1.0)

	G.add_edge('T', 'Q', weight=1.0)
	G.add_edge('T', 'P', weight=1.0)
	G.add_edge('T', 'O', weight=1.0)
	G.add_edge('T', 'N', weight=1.0)
	G.add_edge('T', 'M', weight=1.0)

	G.add_edge('R', 'T', weight=1.0)
	G.add_edge('S', 'T', weight=1.0)
	G.add_edge('J', 'T', weight=1.0)
	G.add_edge('K', 'T', weight=1.0)
	G.add_edge('L', 'T', weight=1.0)

	return G

def main(): 
	G = createGraph(nx.DiGraph())

	paths = ["Spider"]
	for elements in paths:
		if len(paths) == 1: #if there is exactly one path, it must be the case that paths = ['Spider']
			node = "Spider" #hence, node = Spider
		else: #if there are more than one path
			node = elements[-1] #then node will equal to the last node. For instance if element = ['Spider', 'A'] then node = 'A'
		for neighbor in G.adj[node]: #iterates through each neighbor of a node
			newPath= [elements] #stores the original paths. For instance newPath = 'Spider', 'A'
			newPath.append(neighbor) #Adds the new neighbor to the path . newPath = 'Spider', 'A', 'some neighbor'
			paths.append(newPath) #adds the new path to the list of paths

	i = 0
	for elements in paths:
		if "Fly" in elements: #only count the paths that has 'Fly' in it. Hence, paths that start with 'Spider' and end with 'Fly'
			#print(elements) #print all the paths
			i += 1 #count the number of paths
	print(i)

main()



#Fifth Problem

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