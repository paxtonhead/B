class User:

  def __init__(self, name, w, h, loc, iden=0):
    self.username = name
    self.ID = iden
    self.wants = w
    self.haves = h
    self.location = loc


  def updateWants(self, w):
    self.wants = w

  def updateHaves(self, h):
    self.haves = h

  def updateLocation(self, loc):
    self.location = loc

  def mergeAndReturn(self):
    self.D = {'USERNAME': self.username, 'ID': self.ID, 'LOCATION': self.location, 'WANT': self.wants, 'HAVE': self.haves}
    return self.D

  @staticmethod
  def createUserBase(*users):
    base = []
    for i in users:
      base.append(i)
    return base
  
  @staticmethod
  def setIDs(base):
    for count, user in enumerate(base):
      user['ID'] = count
