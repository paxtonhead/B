from collections import defaultdict

class Graph:

  connectedComponents = defaultdict(set)

  def __init__(self, ver):
    self.V = ver
    self.graph = defaultdict(set)
    self.counter = 0

  def addEdge(self, u, v):
    self.graph[u].add(v)


  def printGraph(self):
    print(self.graph)

  def printConnected(self):
    print(self.connectedComponents)

  def getConnectedComponents(self):
    return self.connectedComponents

  
  # A function used by DFS
  def DFSUtil(self,v,visited):
    # Mark the current node as visited and print it
    visited[v]= True
    self.connectedComponents[self.counter].add(v)
    #Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
      if visited[i]==False:
        self.DFSUtil(i,visited) 

    self.counter += 1


  def fillOrder(self,v,visited, stack):
    # Mark the current node as visited 
    visited[v]= True
    #Recur for all the vertices adjacent to this vertex
    for i in self.graph[v]:
        if visited[i]==False:
            self.fillOrder(i, visited, stack)
    stack = stack.append(v)
     
 
    # Function that returns reverse (or transpose) of this graph
  def getTranspose(self):
    g = Graph(self.V)

    # Recur for all the vertices adjacent to this vertex
    for i in self.graph:
        for j in self.graph[i]:
            g.addEdge(j,i)
    return g


  # The main function that finds and prints all strongly
  # connected components
  def calcSCCs(self):

      stack = []
      # Mark all the vertices as not visited (For first DFS)
      visited = [False]*(self.V)
      # Fill vertices in stack according to their finishing
      # times
      for i in range(self.V):
          if visited[i]==False:
              self.fillOrder(i, visited, stack)

      # Create a reversed graph
      gr = self.getTranspose()
        
      # Mark all the vertices as not visited (For second DFS)
      visited =[False]*(self.V)

      # Now process all vertices in order defined by Stack
      while stack:
          i = stack.pop()
          if visited[i]==False:
              gr.DFSUtil(i, visited)

      return self.connectedComponents
