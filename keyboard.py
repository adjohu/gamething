import pygame
from pygame.locals import *
from event import *
from game_locals import *


class KeyboardController:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            # handle input events
            for event in pygame.event.get():
                ev = None
                if event.type == QUIT:
                    ev = QuitEvent()
                if event.type == KEYDOWN:
                    key = event.key
                    if key == K_ESCAPE:
                        ev = QuitEvent()
                    elif key == K_UP:
                        direction = DIRECTION_UP
                        ev = CharactorMoveRequest(direction)

                if ev:
                    self.evManager.Post(ev)
