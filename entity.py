from events import *
from game_locals import *


class Entity(object):
    def __init__(self, world, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.x = 0
        self.y = 0

        self.mass = 10

        self.Reset()

        ev = EntityCreatedEvent(self)
        self.evManager.Post(ev)

    def UpdatePosition(self, delta_time):
        self.y += PX_IN_METRE * self.y_vel * delta_time

        ev = EntityMoveEvent(self)
        self.evManager.Post(ev)

    def Reset(self):
        self.x_vel = 0
        self.y_vel = 0

    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.UpdatePosition(event.delta_time)
