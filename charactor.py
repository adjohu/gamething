from event import *


class Charactor:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self, event):
        if isinstance(event, CharactorMoveRequest):
            self.Move(event.direction)

    def Move(self, direction):
        print "move", direction

    def Place(self):
