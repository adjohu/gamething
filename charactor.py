from event import *
from entity import Entity


class Charactor(Entity):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Move(self, direction):
        print "move", direction

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
