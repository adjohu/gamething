import pygame
from events import *
from sprites import *


class View:
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        pygame.init()

        pygame.display.set_caption("Game")

        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.background = pygame.display.get_surface()

        self.frontSprites = pygame.sprite.RenderUpdates()

    def AddCharactor(self, charactor):
        charactor.sprite.add(self.frontSprites)

    def MoveEntity(self, entity):
        rounded = (round(entity.x), round(entity.y))
        entity.sprite.moveTo = rounded

    def Draw(self):
        self.background.fill((0, 0, 0))

        self.frontSprites.clear(self.window, self.background)

        # Group.update -> calls update() on each sprite in group
        self.frontSprites.update()

        dirty = self.frontSprites.draw(self.window)

        # Update the area of the display changed in the above draw call
        pygame.display.update(dirty)

    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.Draw()

        elif isinstance(event, CharactorAddEvent):
            self.AddCharactor(event.charactor)

        elif isinstance(event, EntityMoveEvent):
            self.MoveEntity(event.entity)
