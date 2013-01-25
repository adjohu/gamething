from event import *
from charactor import Charactor


class Player:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.charactors = [Charactor(evManager)]

    def Notify(self, event):
        if isinstance(event, CharactorMoveRequest):
            print "charctor move request", event.direction
