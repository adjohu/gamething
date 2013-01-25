import pygame
from event import *


class View:
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        pygame.init()

        self.window = pygame.display.set_mode((600, 300))
        self.background = pygame.display.get_surface()
        pygame.display.set_caption("Game")
        self.background.fill((0, 0, 0))

        self.frontSprites = pygame.sprite.RenderUpdates()

    def ShowCharactor(self, charactor):
        charactorSprite = CharactorSprite(self.frontSprites)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            pygame.display.update()
