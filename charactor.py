from event import *
from entity import Entity
from game_locals import *


class Charactor(Entity):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.moveAmount = 10

    def Move(self, direction):
        if direction == DIRECTION_LEFT:
            self.x -= self.moveAmount
        elif direction == DIRECTION_RIGHT:
            self.x += self.moveAmount
            print self.x

    def Place(self, x, y):
        self.x = x
        self.y = y

        ev = CharactorPlaceEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, GameStartedEvent):
            self.Place(100, 100)

        elif isinstance(event, CharactorMoveRequest):
            self.Move(event.direction)
