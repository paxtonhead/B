def johnson():
    stack = Stack()
    blockedSet = []
    blockedMap = []
    hasBeenInCycle = []
    startVertex = user_base1[0]
    stack.push(startVertex)
    blockedSet.append(startVertex)


    def johnsonRecur(currentNode):
        returnedNode = None
        neighbors = G[currentNode['USERNAME']]
        for k in neighbors:
            if k == startVertex:
                addCycle()
                continue
            if k in blockedSet:
                #print(str(k) + " is in blocked set")
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
        print(stack)
        temp = Stack()
        while(len(stack) > 0):
            hasBeenInCycle.append(stack.peek())
            temp.push(stack.pop())
        while(len(temp) > 0):
            stack.push(temp.pop())


    johnsonRecur(startVertex)
