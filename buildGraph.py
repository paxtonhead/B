from Graph import Graph

def findWholeMatch(initial_user):
  half_match = []
  full_match = {}

  # Initial search finds a half match
  for user in user_base2:

    # Continues to avoid comparing user to themselves
    if user == initial_user:
      continue

    for wants in initial_user['WANT']:
      for haves in user['HAVE']:
        if wants == haves:
          half_match.append(user)
          full_match['RECEIVE'] = wants


  # Next searches the half matches the determine if there if a full match
  for user in half_match:
    
    for haves in initial_user['HAVE']:
      for wants in user['WANT']:
        if wants == haves:
          full_match['SEND'] = wants
          full_match['NAME OF USER'] = user['USERNAME']

  return full_match


def fillGraph(G, initial_user):

  for user in user_base1:

    # Continues to avoid comparing user to themselves
    if user == initial_user:
      continue

    for wants in initial_user['WANT']:
      for haves in user['HAVE']:
        if wants == haves:
          G.addEdge(initial_user['ID'], user['ID'])

  return G


def convertIDToUsername(IDs):
  result = set()

  for users in user_base1:
    for i in IDs:
      if users['ID'] == i:
        result.add(users['USERNAME'])

  return result






if __name__ == '__main__':          
  #########################################################################################################
  A = {'USERNAME': 'A', 'ID': 0, 'WANT': [1], 'HAVE': [2]}
  B = {'USERNAME': 'B', 'ID': 1, 'WANT': [3], 'HAVE': [1]}
  C = {'USERNAME': 'C', 'ID': 2, 'WANT': [2], 'HAVE': [3]}
  D = {'USERNAME': 'D', 'ID': 3, 'WANT': [], 'HAVE': []}
  E = {'USERNAME': 'E', 'ID': 4, 'WANT': [], 'HAVE': []}

  user_base1 = [A, B, C, D, E]

  G = Graph(len(user_base1))

  for i in user_base1:
    fillGraph(G, i)

  G.printGraph()

  strong = G.calcSCCs()
  print(strong)

  for key, value in strong.items():
      # do something with value
      strong[key] = convertIDToUsername(value)

  print(strong)

  #########################################################################################################

  #########################################################################################################
  user1 = {'USERNAME': 'Scott', 'WANT': ['Modern Warfare 2', 'Hunger Games', 'Monopoly'], 
          'HAVE': ['Fortnite', 'Super Smash Bros', 'Star Wars: A New Hope']}
  user2 = {'USERNAME': 'Conner', 'WANT': ['Star Wars: A New Hope', 'Hunger Games 2'], 
          'HAVE': ['Monopoly', 'Sorry', 'Clue']}

  user_base2 = [user1, user2]

  #print(findWholeMatch(user1))
  #########################################################################################################

