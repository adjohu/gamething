from player import Player
from event import *


class Game:
    STATE_PREPARING = 0
    STATE_RUNNING = 1
    STATE_PAUSED = 2

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.state = Game.STATE_PREPARING

        self.players = [Player(evManager)]

    def Start(self):
        print "game starting"
        self.state = Game.STATE_RUNNING
        ev = GameStartedEvent(self)
        self.evManager.Post(ev)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            if self.state == Game.STATE_PREPARING:
                self.Start()
