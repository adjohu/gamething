from physics import Physics
from events import *


class World:
    def __init__(self, evManager):
        from weakref import WeakSet

        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.physics = Physics(evManager)

        self.entities = WeakSet()

    def AddEntity(self, entity):
        self.entities.add(entity)

    def ApplyPhysics(self):
        for entity in self.entities:
            self.physics.Apply(entity)

    def Notify(self, event):
        if isinstance(event, EntityCreatedEvent):
            self.AddEntity(event.entity)

        elif isinstance(event, TickEvent):
            self.ApplyPhysics()
