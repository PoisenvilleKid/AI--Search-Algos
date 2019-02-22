from collections import defaultdict 

class Graph: 
  
    def __init__(this): 
  
        #Dictionary To Store Entire Graph
        this.graph = defaultdict(list)

        #Dictionary To Hold if Verticie Has Been Visited
        this.visited = defaultdict(bool) 

         # Create an open and closed list for BFS 
        this.openlist = []
        this.closedlist = []
        this.expanded = []

        # Variable to keep track if we reached goal state
        this.foundgoal = False;
  
    # function to add an edge to graph 
    def addEdge(this,u,v): 
        this.graph[u].append(v)
        this.visited[u] = False 

    # IF we hit a goal state print out the Goal State
    def foundState(this, s):
        print(s, "Has been removed from the open list and is a Goal State")
           
    # Function to print a BFS of graph 
    def BFS(this, s): 
  
        print("****Breadth First Search****")
        print("****Adding Root Node****\n") 

        # Mark the source node as  
        # visited and enqueue it
        this.openlist.append(s)
        print(s, " Has been added to the end of the open list") 

        this.visited[s] = True
        print(s , " Has Been Visited\n")
        print("****Beginning Loop****")

        # Loop through the rest of the Nodes and their Neighbors
        while this.openlist: 
  
            # Pop the node at the front of the queue
            s = this.openlist.pop(0)

            #Check To See If The Current Node Is A Goal State
            if s == 'G1' or s == 'G2':
                this.foundState(s)
                foundgoal = True
                this.expanded.append(s)
                break

            # Add The Popped Node to Our Closed List... We Are about to go to its neighbors
            this.closedlist.append(s)
            this.expanded.append(s) 
            print (s, "Has been removed from the open list and added to the closed list\n")
            
            # Find All The Neighbors from the current Node and add to the queue for us to open later
            # Mark All the neighbors as visited
            for i in this.graph[s]: 
                if this.visited[i] == False: 
                    this.openlist.append(i)
                    this.visited[i] = True
                    print(i, " Has been added to the end of the open list and marked as Visited")

            print("\nContents of Expanded List: ",this.expanded)
            print("Contents Of Open List: ", this.openlist)
            print("Contents of Closed List:", this.closedlist)        
            print("\n---------------------------------------------------------------------------\n")

        if (not foundgoal):
            print("Goal State Not Found")
        print("Final Contents Of Expanded List:", this.expanded)
        print("Final Contents Of Open List: ", this.openlist)
        print("Final Contents of Closed List", this.closedlist)         

# Driver code 
  
g = Graph() 
g.addEdge('S','A')
g.addEdge('S','F')
g.addEdge('S','B')
g.addEdge('A','C')
g.addEdge('A','D')
g.addEdge('F','D')
g.addEdge('B','E')
g.addEdge('B','G2')
g.addEdge('C','D')
g.addEdge('C','S')
g.addEdge('D','B')
g.addEdge('D','G1')
g.addEdge('E','H')
g.addEdge('E','G2')
g.addEdge('G2','B')
g.addEdge('G1','C')
g.addEdge('H','G2')

g.BFS('S')