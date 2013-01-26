import pygame
from event import *
from sprites import *


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

    def AddCharactor(self, charactor):
        charactor.sprite.add(self.frontSprites)

    def Draw(self):
        self.frontSprites.clear(self.window, self.background)

        # Group.update -> calls update() on each sprite in group
        self.frontSprites.update()

        dirty = self.frontSprites.draw(self.window)

        # Update the area of the display changed in the above draw call
        pygame.display.flip()

    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.Draw()

        elif isinstance(event, CharactorAddEvent):
            id(event.charactor)
            self.AddCharactor(event.charactor)
