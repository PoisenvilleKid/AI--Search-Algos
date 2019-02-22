from collections import defaultdict
import queue

class Graph: 
  
   
    def __init__(this): 
  

        #Dictionary To Store Entire Graph
        this.graph = defaultdict(list)

        #Dictionary To Hold if Verticie Has Been Visited
        this.visited = defaultdict(bool) 

         # Create an open,closed and expanded list for Best First Search 
        this.openlist = queue.PriorityQueue()
        this.closedlist = []
        this.expanded = []
        this.readopenlist = []
       
        # Check if we reached goal state
        this.foundgoal = False;
  
    # method to add edge to Node 
    def addEdge(this,u,v,h): 
        this.graph[u].append((v,h))
        this.visited[u] = False 

    # Print if we reached a goal state
    def foundState(this, s):
        print(s, " Has been reached and is a Goal State")
           
    # method to run Best First Search 
    def BFS(this, s): 
  
        print("****Best First Search****")
        print("****Adding Root Node****\n") 

        #Put Root Node in que and mark as visited
        this.openlist.put((0,s))
        this.readopenlist.append(s)
        print(s, " Has been added to the end of the open list") 

        this.visited[s] = True
        print(s , " Has Been Visited\n")
        print("****Beginning Loop****")


        # Loop to find other nodes
        while this.openlist: 
  
            # Get Node with lowest Heurisitc
            s = this.openlist.get()[1]
            this.readopenlist.remove(s)
            
            # If Node is a goal state end program
            if s == 'G1' or s == 'G2':
                this.foundState(s)
                foundgoal = True
                this.expanded.append(s)
                break

            # Add current Node to closed and expanded lists
            this.closedlist.append(s) 
            this.expanded.append(s)
            print (s, "Has been removed from the open list and added to the closed list\n") 
  
            
            # Find neighbor edges to Node and mark as visited
            for i in this.graph[s]: 
                v = i[0]
                if this.visited[v] == False: 
                    this.openlist.put((i[1],v))
                    this.readopenlist.append(v)
                    this.visited[v] = True
                    print(v, " Has been added to the end of the open list and marked as Visited")
            print("Contents Of Expanded List: ", this.expanded)
            print("Contents Of Open List: ", this.readopenlist)
            print("Contents of Closed List", this.closedlist)        
            print("\n---------------------------------------------------------------------------\n")
                          
        if (not foundgoal):
            print("Goal State Not Found")
        print("Final Contents Of Expanded List: ", this.expanded)    
        print("Final Contents Of Open List: ", this.readopenlist)
        print("Final Contents of Closed List", this.closedlist)         

# Driver code 
  
g = Graph() 
g.addEdge('S','A', 5)
g.addEdge('S','F', 9)
g.addEdge('S','B', 8)
g.addEdge('A','C', 3)
g.addEdge('A','D', 2)
g.addEdge('F','D', 2)
g.addEdge('B','E', 4)
g.addEdge('B','G2', 0)
g.addEdge('C','D', 2)
g.addEdge('C','S', 10 )
g.addEdge('D','B', 8)
g.addEdge('D','G1', 0)
g.addEdge('E','H', 2)
g.addEdge('E','G2', 0)
g.addEdge('G2','B', 8)
g.addEdge('G1','C', 3)
g.addEdge('H','G2', 0)

g.BFS('S')