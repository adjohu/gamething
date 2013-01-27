from events import *


class Entity(object):
    def __init__(self, world, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.x = 0
        self.y = 0
        self.x_vel = 0
        self.y_vel = 0

        self.mass = 10

        ev = EntityCreatedEvent(self)
        self.evManager.Post(ev)

    def UpdatePosition(self):
        self.y += self.y_vel

        ev = EntityMoveEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.UpdatePosition()
