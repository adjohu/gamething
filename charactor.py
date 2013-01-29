from events import *
from entity import Entity
from game_locals import *
from sprites import CharactorSprite


class Charactor(Entity):
    def __init__(self, evManager):
        super(Charactor, self).__init__(self, evManager)

        self.sprite = CharactorSprite()

        self.moveAmount = 10

    def Move(self, direction):
        if direction == DIRECTION_LEFT:
            self.x_vel -= self.moveAmount
        elif direction == DIRECTION_RIGHT:
            self.x_vel += self.moveAmount

        ev = EntityMoveEvent(self)
        self.evManager.Post(ev)

    def Place(self, x, y):
        self.x = x
        self.y = y

        self.Reset()

        ev = EntityMoveEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        super(Charactor, self).Notify(event)

        if isinstance(event, GameStartedEvent):
            self.Place(100, 100)
            ev = CharactorAddEvent(self)
            self.evManager.Post(ev)

        elif isinstance(event, CharactorPlaceRequest):
            self.Place(event.x, event.y)

        elif isinstance(event, CharactorMoveRequest):
            self.Move(event.direction)
