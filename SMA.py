from collections import defaultdict
import queue

class Graph: 
  
   
    def __init__(this): 
  

        #Dictionary To Store Entire Graph
        this.graph = defaultdict(list)

        #Dictionary To Hold if Verticie Has Been Visited
        this.visited = defaultdict(bool) 

         # Create an open,closed and expanded list for SMA
        this.openlist = queue.PriorityQueue()
        this.closedlist = []
        this.expanded = []
        this.readopenlist = []
       
        # Check if we reached goal state
        this.foundgoal = False;
  
    # method to add edge to Node 
    def addEdge(this,u,v,g,h): 
        this.graph[u].append((v,g+h))
        this.visited[u] = False 

    # Print if we reached a goal state
    def foundState(this, s):
        print(s, " Has been reached and is a Goal State")
           
    # method to run Best First Search 
    def AStar(this, s): 
  
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
  
            # Get Node with lowest Heurisitc and Path combined
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
            print("\nContents Of Expanded List: ", this.expanded)
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
g.addEdge('S','A', 10,3)
g.addEdge('S','F', 10,2)
g.addEdge('S','B', 10,7)
g.addEdge('A','C', 5,1)
g.addEdge('A','D', 5,7)
g.addEdge('F','D', 9,4)
g.addEdge('B','E', 8,1)
g.addEdge('B','G2', 8,9)
g.addEdge('C','D', 3,4)
g.addEdge('C','S', 3,2 )
g.addEdge('D','B', 2,3)
g.addEdge('D','G1', 2,6)
g.addEdge('E','H', 4,1)
g.addEdge('E','G2', 4,5)
g.addEdge('G2','B', 0,8)
g.addEdge('G1','C', 0,2)
g.addEdge('H','G2', 2,1)

g.AStar('S')