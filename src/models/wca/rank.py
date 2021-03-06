from google.appengine.ext import ndb

from src.models.user import User
from src.models.wca.base import BaseModel
from src.models.wca.event import Event
from src.models.wca.person import Person

class RankBase(BaseModel):
  person = ndb.KeyProperty(kind=Person)
  event = ndb.KeyProperty(kind=Event)
  best = ndb.IntegerProperty()
  state = ndb.ComputedProperty(lambda self: self.GetState())

  worldRank = ndb.IntegerProperty()
  continentRank = ndb.IntegerProperty()
  countryRank = ndb.IntegerProperty()

  def GetState(self):
    if not self.person or not self.person.get():
      return None
    return self.person.get().state

  @staticmethod
  def GetId(row):
    return '%s_%s' % (row['personId'], row['eventId'])

  def ParseFromDict(self, row):
    self.person = ndb.Key(Person, row['personId'])
    self.event = ndb.Key(Event, row['eventId'])
    self.best = int(row['best'])

    self.worldRank = int(row['worldRank'])
    self.continentRank = int(row['continentRank'])
    self.countryRank = int(row['countryRank'])

  @staticmethod
  def ColumnsUsed():
    return ['personId', 'eventId', 'best', 'worldRank', 'continentRank', 'countryRank']

  def ObjectsToGet(self):
    return [self.person]


class RankAverage(RankBase):
  pass

class RankSingle(RankBase):
  pass
