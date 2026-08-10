import pygame
pygame.init()

import time

class all_plants():
    class sunflower(pygame.sprite.Sprite):
        x: int
        y: int
        hp: int
        image: pygame.Surface
        rect: pygame
        live: bool

        def __init__(self, x: int, y: int):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.hp = 500
            self.last_sun_time = time.time()
            self.sun_interval = 5.0
            self.ready_to_give = False
            self.live = True
            self.image = pygame.image.load("plants_vs_zombies//images//sunflower.png").convert_alpha()
            self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*130))

        def sun_check(self):
            current_time = time.time()
            if current_time - self.last_sun_time >= self.sun_interval:
                self.ready_to_give = True
                self.sun_interval = 10.0
                self.last_sun_time = current_time
            else:
                self.ready_to_give = False

        def hit(self, damage: int):
            self.hp -= damage
            if self.hp <= 0:
                self.live = False

    class wallnut(pygame.sprite.Sprite):
        x: int
        y: int
        hp: int
        image: pygame.Surface
        rect: pygame
        live: bool

        def __init__(self, x: int, y: int):
            pygame.sprite.Sprite.__init__(self)
            self.x = x
            self.y = y
            self.hp = 4000
            self.live = True
            self.image = pygame.image.load("plants_vs_zombies//images//wallnut.png").convert_alpha()
            self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*130))

        def hit(self, damage: int):
            self.hp -= damage
            if self.hp <= 0:
                self.live = False

class sun(pygame.sprite.Sprite):
    x: int
    y: int
    alpha: int
    full_vanish: bool
    image: pygame.Surface
    rect: pygame

    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.alpha = 255
        self.start_time = time.time()
        self.full_vanish = False
        self.image = pygame.image.load("plants_vs_zombies//images//sun.png").convert_alpha()
        self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*130))
        self.image.set_alpha(self.alpha)

    def update(self):
        current_time = time.time()
        if 255 - (current_time - self.start_time)*255 > 0:
            self.alpha = 255 - (current_time - self.start_time)*255
        else:
            self.full_vanish = True