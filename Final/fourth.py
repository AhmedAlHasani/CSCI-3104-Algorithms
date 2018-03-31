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