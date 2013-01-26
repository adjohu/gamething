import pygame


class CharactorSprite(pygame.sprite.Sprite):
    CharactorSpriteGroup = pygame.sprite.RenderUpdates()

    def __init__(self, group=CharactorSpriteGroup):
        pygame.sprite.Sprite.__init__(self, group)

        charactorSurf = pygame.Surface((64, 64))
        pygame.draw.rect(charactorSurf, (0, 255, 128), ((0, 0), (64, 64)))
        pygame.draw.circle(charactorSurf, (255, 0, 0), (32, 32), 32)
        self.image = charactorSurf
        self.rect = charactorSurf.get_rect()

        self.moveTo = None

    def update(self):
        if self.moveTo:
            self.rect.center = self.moveTo
            self.moveTo = None
