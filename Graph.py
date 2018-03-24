from collections import defaultdict
from Stack import Stack

class Graph:

    def __init__(self, ver):
        self.V = ver
        self.IDGraph = defaultdict(set)
        self.UsernameGraph = defaultdict(set)
        self.counter = 0
        self.connectedComponents = defaultdict(set)
        self.userBase = []
        self.longestCycle = 0
        self.bestCycle = []

    def addEdge(self, u, v):
        if isinstance(u, int):
            self.IDGraph[u].add(v)
        elif isinstance(u, str):
            self.UsernameGraph[u].add(v)

    def setUserBase(self, ub):
        self.userBase = ub

    def getUserBase(self):
        return self.userBase

    def getGraph(self, check):
        if check:
            return self.UsernameGraph
        else:
            return self.IDGraph

    def printGraph(self, check):
        if check:
            print(self.UsernameGraph)
        else:
            print(self.IDGraph)

    def printuserBase(self):
        print(self.userBase)

    def printConnectedComponents(self):
        print(self.connectedComponents)

    def getConnectedComponents(self):
        return self.connectedComponents

    def fillGraphs(self):
        for i in self.userBase:
            for user in self.userBase:

                # Continues to avoid comparing user to themselves
                if user is i:
                    continue

                for wants in i['WANT']:
                    for haves in user['HAVE']:
                        if wants == haves:
                            self.addEdge(i['ID'], user['ID'])

        for i in self.userBase:
            for user in self.userBase:

                # Continues to avoid comparing user to themselves
                if user is i:
                    continue

                for wants in i['WANT']:
                    for haves in user['HAVE']:
                        if wants == haves:
                            self.addEdge(i['USERNAME'], user['USERNAME'])

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

    ######################################Start of SCC algo###################################################
    ##########################################################################################################
    # The main function that finds and prints all strongly
    # connected components
    def calcSCCs(self):

        # Function that returns reverse (or transpose) of this graph
        def getTranspose():
            g = Graph(self.V)

            # Recur for all the vertices adjacent to this vertex
            for i in self.IDGraph:
                for j in self.IDGraph[i]:
                    g.addEdge(j, i)
            return g

        def fillOrder(v, visited, stack):
            # Mark the current node as visited
            visited[v] = True
            # Recur for all the vertices adjacent to this vertex
            for i in self.IDGraph[v]:
                if visited[i] == False:
                    fillOrder(i, visited, stack)
            stack = stack.append(v)

        # A function used by DFS
        def DFSUtil(v, visited):
            # Mark the current node as visited and print it
            visited[v] = True
            self.connectedComponents[self.counter].add(v)
            # Recur for all the vertices adjacent to this vertex
            for i in self.IDGraph[v]:
                if visited[i] == False:
                    DFSUtil(i, visited)

            self.counter += 1
            return self.connectedComponents

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                self.connectedComponents = DFSUtil(i, visited)

        return self.connectedComponents

    def getBiggestCycle(self, user_base):
        stack = Stack()
        blockedSet = []
        blockedMap = []
        hasBeenInCycle = []
        startVertex = user_base[0]['USERNAME']
        self.longestCycle = 0

        stack.push(startVertex)
        blockedSet.append(startVertex)

        def johnsonRecur(currentNode):
            returnedNode = None
            #print(currentNode)
            #print(self.UsernameGraph)
            neighbors = self.UsernameGraph[currentNode]
            #print(neighbors)
            for k in neighbors:
                if k == startVertex:
                    addCycle()
                    continue
                if k in blockedSet:
                    # print(str(k) + " is in blocked set")
                    continue
                stack.push(k)
                blockedSet.append(k)
                returnedNode = johnsonRecur(k)
            if currentNode in hasBeenInCycle:
                stack.pop()
                unblock(currentNode)
            else:
                blockedMap.append([returnedNode, currentNode])

        def unblock(current):
            noid = current
            blockedSet.remove(current)
            for i in blockedMap:
                if i[0] == noid:
                    temp = i[1]
                    blockedMap.__delitem__(i)
                    noid = temp
                    blockedSet.remove(noid)

        def addCycle():
            temp = Stack()
            bowel = False
            if len(stack) > self.longestCycle:
                self.longestCycle = len(stack)
                self.bestCycle.clear()
                bowel = True

            while (len(stack) > 0):
                hasBeenInCycle.append(stack.peek())
                temp.push(stack.pop())
            while (len(temp) > 0):
                if bowel:
                    self.bestCycle.append(temp.peek())
                stack.push(temp.pop())
            self.bestCycle.append(startVertex)

        johnsonRecur(startVertex)
        final = ''
        half = int(len(self.bestCycle) / 2)
        self.bestCycle = self.bestCycle[0:half]
        for k in self.bestCycle:
            final = final + k

    def printBestCycle(self):
        print(self.bestCycle)

    ##########################################################################################################
