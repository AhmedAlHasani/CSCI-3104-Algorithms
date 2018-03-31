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
