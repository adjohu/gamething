import pygame
from events import *


class TickController:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        self.clock = pygame.time.Clock()
        self.keep_running = 1

    def Run(self):
        while self.keep_running:
            delta_time = self.clock.tick(60) / 1000.0
            event = TickEvent(delta_time)
            self.evManager.Post(event)

    def Notify(self, event):
        if isinstance(event, QuitEvent):
            self.keep_running = 0
