class Event:
    def __init__(self):
        self.name = "Generic event"


class GameStartedEvent(Event):
    def __init__(self, game):
        self.name = "GameStartedEvent"
        self.game = game


class QuitEvent(Event):
    def __init__(self):
        self.name = "Quit Event"


class TickEvent(Event):
    def __init__(self, delta_time):
        self.name = "Tick"
        self.delta_time = delta_time


class CharactorMoveRequest(Event):
    def __init__(self, direction):
        self.name = "CharactorMoveRequest"
        self.direction = direction


class CharactorStopMovingRequest(Event):
    def __init__(self):
        self.name = "CharactorStopMovingRequest"


class CharactorPlaceRequest(Event):
    def __init__(self, x, y):
        self.name = "CharactorPlaceRequest"
        self.x = x
        self.y = y


class EntityMoveEvent(Event):
    def __init__(self, entity):
        self.name = "EntityMoveEvent"
        self.entity = entity


class CharactorAddEvent(Event):
    def __init__(self, charactor):
        self.name = "CharactorAddEvent"
        self.charactor = charactor


class EntityCreatedEvent(Event):
    def __init__(self, entity):
        self.entity = entity
