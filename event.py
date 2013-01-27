class EventManager:
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def RegisterListener(self, listener):
        print "registered listener", listener
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def Post(self, event):
        for listener in self.listeners.keys():
            listener.Notify(event)


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
    def __init__(self):
        self.name = "Tick"


class CharactorMoveRequest(Event):
    def __init__(self, direction):
        self.name = "CharactorMoveRequest"
        self.direction = direction


class CharactorPlaceRequest(Event):
    def __init__(self, x, y):
        self.name = "CharactorPlaceRequest"
        self.x = x
        self.y = y


class CharactorMoveEvent(Event):
    def __init__(self, charactor):
        self.name = "CharactorPlaceEvent"
        self.charactor = charactor


class CharactorAddEvent(Event):
    def __init__(self, charactor):
        self.name = "CharactorAddEvent"
        self.charactor = charactor
