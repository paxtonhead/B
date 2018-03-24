from collections import defaultdict

class Graph: 

  def __init__(self, ver):
    self.V = ver
    self.graph = defaultdict(set)
    self.counter = 0
    self.connectedComponents = defaultdict(set)
    self.userBase = []

  def addEdge(self, u, v):
    self.graph[u].add(v)

  def setUserBase(self, ub):
    self.userBase = ub

  def getUserBase(self):
    return self.userBase

  def printGraph(self):
    print(self.graph)

  def printuserBase(self):
    print(self.userBase)

  def printConnectedComponents(self):
    print(self.connectedComponents)

  def getConnectedComponents(self): 
    return self.connectedComponents


  def fillGraph(self):
    for i in self.userBase: 
      for user in self.userBase:

      # Continues to avoid comparing user to themselves
        if user is i:
          continue

        for wants in i['WANT']:
          for haves in user['HAVE']:
            if wants == haves:
              self.addEdge(i['ID'], user['ID'])


  def convertIDToUsername(self, D):
    for key, value in D.items():
    
      result = set()

      for users in self.userBase:
        for i in value:
          if users['ID'] == i:
            result.add(users['USERNAME'])

      D[key] = result

    return D

  
  def findWholeMatch(self, initialUser):
    initialUser = self.userBase[0]
    half_match = []
    full_match = {}

    # Initial search finds a half match
    for user in self.userBase:

      # Continues to avoid comparing user to themselves
      if user == initialUser:
        continue

      for wants in initialUser['WANT']:
        for haves in user['HAVE']:
          if wants == haves:
            half_match.append(user)
            full_match['RECEIVE'] = wants


    # Next searches the half matches the determine if there if a full match
    for user in half_match:
      
      for haves in initialUser['HAVE']:
        for wants in user['WANT']:
          if wants == haves:
            full_match['SEND'] = wants
            full_match['NAME OF USER'] = user['USERNAME']

    return full_match


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
    return self.connectedComponents


  # The main function that finds and prints all strongly
  # connected components
  def calcSCCs(self):
    
    
    # Function that returns reverse (or transpose) of this graph
    def getTranspose():
      g = Graph(self.V)

      # Recur for all the vertices adjacent to this vertex
      for i in self.graph:
          for j in self.graph[i]:
              g.addEdge(j,i)
      return g

    
    def fillOrder(v,visited, stack):
      # Mark the current node as visited 
      visited[v]= True
      #Recur for all the vertices adjacent to this vertex
      for i in self.graph[v]:
          if visited[i]==False:
              fillOrder(i, visited, stack)
      stack = stack.append(v)
    
    
    # A function used by DFS
    def DFSUtil(v,visited):
      # Mark the current node as visited and print it
      visited[v]= True
      self.connectedComponents[self.counter].add(v)
      #Recur for all the vertices adjacent to this vertex
      for i in self.graph[v]:
        if visited[i]==False:
          DFSUtil(i,visited) 

      self.counter += 1
      return self.connectedComponents
    
    
    
    
    stack = []
    # Mark all the vertices as not visited (For first DFS)
    visited = [False]*(self.V)
    # Fill vertices in stack according to their finishing
    # times
    for i in range(self.V):
        if visited[i]==False:
            fillOrder(i, visited, stack)

    # Create a reversed graph
    gr = getTranspose() 
      
    # Mark all the vertices as not visited (For second DFS)
    visited =[False]*(self.V)

    # Now process all vertices in order defined by Stack
    while stack:
        i = stack.pop()
        if visited[i]==False:
            self.connectedComponents = gr.DFSUtil(i, visited)

    return self.connectedComponents


