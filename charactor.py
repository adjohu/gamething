from event import *
from entity import Entity
from game_locals import *
from sprites import CharactorSprite


class Charactor(Entity):
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.sprite = CharactorSprite()

        self.moveAmount = 10

    def Move(self, direction):
        if direction == DIRECTION_LEFT:
            self.x -= self.moveAmount
        elif direction == DIRECTION_RIGHT:
            self.x += self.moveAmount

    def Place(self, x, y):
        self.sprite.moveTo = (x, y)

        ev = CharactorPlaceEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, GameStartedEvent):
            self.Place(100, 100)
            ev = CharactorAddEvent(self)
            self.evManager.Post(ev)

        elif isinstance(event, CharactorPlaceRequest):
            self.Place(event.x, event.y)

        elif isinstance(event, CharactorMoveRequest):
            self.Move(event.direction)
