def findMatch(initial_user):
  half_match = []
  full_match = {}

  # Initial search finds a half match
  for users in user_base:

    # Continues to avoid comparing user to themselves
    if users == initial_user:
      continue

    for wants in initial_user['WANT']:
      for haves in users['HAVE']:
        if wants == haves:
          half_match.append(users)
          full_match['RECEIVE'] = wants


  # Next searches the half matches the determine if there if a full match
  for users in half_match:
    
    for haves in initial_user['HAVE']:
      for wants in users['WANT']:
        if wants == haves:
          full_match['SEND'] = wants
          full_match['NAME OF USER'] = users['USERNAME']

  return full_match


user1 = {'USERNAME': 'Scott', 'WANT': ['Modern Warfare 2', 'Hunger Games', 'Monopoly'], 
        'HAVE': ['Fortnite', 'Super Smash Bros', 'Star Wars: A New Hope']}
user2 = {'USERNAME': 'Connor', 'WANT': ['Star Wars: A New Hope', 'Hunger Games 2'], 
        'HAVE': ['Monopoly', 'Sorry', 'Clue']}

user_base = [user1, user2]

print(findMatch(user1))

