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


def findHalfMatch(initial_user):
  half_match = []

  for user in user_base1:

    # Continues to avoid comparing user to themselves
    if user == initial_user:
      continue

    for wants in initial_user['WANT']:
      for haves in user['HAVE']:
        if wants == haves:
          half_match.append(user['USERNAME'])

  return half_match
          
#########################################################################################################
A = {'USERNAME': 'A', 'WANT': [1, 5], 'HAVE': [2, 6]}
B = {'USERNAME': 'B', 'WANT': [3, 5], 'HAVE': [1, 2]}
C = {'USERNAME': 'C', 'WANT': [2, 3], 'HAVE': [1, 7]}
D = {'USERNAME': 'D', 'WANT': [4, 6], 'HAVE': [3, 5]}
E = {'USERNAME': 'E', 'WANT': [1, 7], 'HAVE': [3, 6]}

user_base1 = [A, B, C, D, E]

findHalfMatch(A)

G = {}

for node in user_base1:
  G[node['USERNAME']] = findHalfMatch(node)

print(G)
#########################################################################################################

#########################################################################################################
user1 = {'USERNAME': 'Scott', 'WANT': ['Modern Warfare 2', 'Hunger Games', 'Monopoly'], 
        'HAVE': ['Fortnite', 'Super Smash Bros', 'Star Wars: A New Hope']}
user2 = {'USERNAME': 'Conner', 'WANT': ['Star Wars: A New Hope', 'Hunger Games 2'], 
        'HAVE': ['Monopoly', 'Sorry', 'Clue']}

user_base2 = [user1, user2]

print(findWholeMatch(user1))
#########################################################################################################

