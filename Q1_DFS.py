from collections import defaultdict


class Graph: 
  
   
    def __init__(this): 
  
        #Dictionary To Store Entire Graph
        this.graph = defaultdict(list)

        #Dictionary To Hold if Verticie Has Been Visited
        this.visited = defaultdict(bool) 

         # Create an open,closed and expanded list for DFS 
        this.openlist = []
        this.closedlist = []
        this.expanded = []

        # Check if we found goal state
        this.foundgoal = False;
  
    # add edges to nodes
    def addEdge(this,u,v): 
        this.graph[u].append(v)
        this.visited[u] = False 

    # print if we found goal state
    def foundState(this, s):
        print(s, " Has been reached and is a Goal State")
           
    # Method to run DFS
    def DFS(this, s): 
  
        print("****Depth First Search****")
        print("****Adding Root Node****\n") 

        # Add RootNode To Stack and mark as visited
        this.openlist.append(s)
        print(s, " Has been added to the end of the open list") 

        this.visited[s] = True
        print(s , " Has Been Visited\n")
        print("****Beginning Loop****")


        # Find Current Node's Neighbors
        while this.openlist: 
  
            #Remove node from end of stack
            s = this.openlist.pop()

            # If Our current node is a goal state end program
            if s == 'G1' or s == 'G2':
                this.foundState(s)
                foundgoal = True
                this.expanded.append(s)
                break

            # Add Current Node to Closed and Expanded
            this.closedlist.append(s)
            this.expanded.append(s)

            print (s, "Has been removed from the open list and added to the closed list\n")
            
  
            # Get All The Neighbors Of Current Node and Mark As Visited
            for i in this.graph[s]: 
                if this.visited[i] == False: 
                    this.openlist.append(i)
                    this.visited[i] = True
                    print(i, " Has been added to the end of the open list and marked as Visited")
            
            # Print Contents After Every Neighbor reached
            print("\nContents Of Expanded List: ", this.expanded)
            print("Contents Of Open List: ", this.openlist)
            print("Contents of Closed List:", this.closedlist)        
            print("\n---------------------------------------------------------------------------\n")
                          
        if (not foundgoal):
            print("Goal State Not Found")
        print("Final Contents Of Expanded List: ", this.expanded)    
        print("Final Contents Of Open List: ", this.openlist)
        print("Final Contents of Closed List:", this.closedlist)         

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

g.DFS('S')