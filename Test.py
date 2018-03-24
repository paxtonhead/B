from Graph import Graph
from Place import Place
from User import User

user_base1 = None
user_base2 = None

API_KEY = 'AIzaSyBoE7AXEdbfic8WGVoSTyXRayhVQX1WXHg'


####################TESTING#################################          
#########################################################################################################
# A = {'USERNAME': 'A', 'LOCATION': 'Earl Gregg Swem Library Williamsburg, VA', 'ID': 0, 'WANT': [1], 'HAVE': [3]}
# B = {'USERNAME': 'B', 'LOCATION': 'Kaplan Arena Williamsburg, VA', 'ID': 1, 'WANT': [3], 'HAVE': [1]}
# C = {'USERNAME': 'C', 'LOCATION': 'Sadler Center Williamsburg, VA', 'ID': 2, 'WANT': [6], 'HAVE': [7]}
# D = {'USERNAME': 'D', 'ID': 3, 'WANT': [], 'HAVE': []}
# E = {'USERNAME': 'E', 'ID': 4, 'WANT': [], 'HAVE': []}

A = User('A', 1, [1], [3], 'Earl Gregg Swem Library Williamsburg, VA')
B = User('C', 2, [3], [1], 'Kaplan Arena Williamsburg, VA')
C = User('B', 3, [6], [10], 'Sadler Center Williamsburg, VA')
A = A.mergeAndReturn()
B = B.mergeAndReturn()
C = C.mergeAndReturn()


userBase = User.createUserBase(A, B, C)
print(userBase)

G1 = Graph(len(userBase))
G1.setUserBase(userBase)
G1.fillGraphs()
G1.printGraph(True)
G1.printGraph(False)
strong = G1.calcSCCs()
strong = G1.convertIDToUsername(strong)
print(strong)
print(G1.findWholeMatch(1))



#########################################################################################################

#########################################################################################################
user1 = {'USERNAME': 'Scott', 'WANT': ['Modern Warfare 2', 'Hunger Games', 'Monopoly'], 
        'HAVE': ['Fortnite', 'Super Smash Bros', 'Star Wars: A New Hope']}
user2 = {'USERNAME': 'Conner', 'WANT': ['Star Wars: A New Hope', 'Hunger Games 2'], 
        'HAVE': ['Monopoly', 'Sorry', 'Clue']}

user_base2 = [user1, user2]

#print(findWholeMatch(user1))
#########################################################################################################

