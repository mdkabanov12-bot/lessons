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
            self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*125))

        def hit(self, damage: int):
            self.hp -= damage
            if self.hp <= 0:
                self.live = False

    class peashooter(pygame.sprite.Sprite):
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
            self.hp = 600
            self.live = True
            self.shoot_interval = 1.5
            self.last_shoot = time.time()
            self.image = pygame.image.load("plants_vs_zombies//images//peashooter.png").convert_alpha()
            self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*125))

        def shoot(self, zombies):
            current_time = time.time()
            if current_time - self.last_shoot >= self.shoot_interval:
                for i in zombies:
                    if i.y == self.y and i.x <= 10:
                        self.last_shoot = current_time
                        return pea(self.x+0.5, self.y)

        def hit(self, damage: int):
            self.hp -= damage
            if self.hp <= 0:
                self.live = False

class all_zombies():
    class normal(pygame.sprite.Sprite):
        may_go: bool
        x: float
        y: int
        damage: int
        hp: int
        arm_hp: int
        image: pygame.Surface
        rect: pygame
        speed: float

        def __init__(self, x: float, y: int, type: str = "normal", armor: int = 0, speed: float = 1.0):
            pygame.sprite.Sprite.__init__(self)
            self.start_time = time.time()
            self.x = x
            self.y = y
            self.speed = speed
            self.type = type
            self.damage = 50
            self.hp = 190
            self.arm_hp = armor
            self.live = True
            self.may_go = True
            self.last_damage = time.time()
            self.image = pygame.image.load(f"plants_vs_zombies//images//zombie//{self.type}.png").convert_alpha()
            self.rect = self.image.get_rect(center=(290+(self.x-0.5)*95, 95+(self.y-0.5)*130))

        def go(self):
            if self.may_go == True:
                current_time = time.time()
                if current_time - self.start_time >= 0.1:
                    self.x -= 0.019*self.speed
                    self.rect = self.image.get_rect(center=(290+(self.x-0.5)*95, 95+(self.y-0.5)*130))
                    self.start_time = current_time
                    round(self.x, 1)
        def end_armor(self):
            self.image = pygame.image.load(f"plants_vs_zombies//images//zombie//normal.png").convert_alpha()
            self.rect = self.image.get_rect(center=(290+(self.x-0.5)*95, 95+(self.y-0.5)*130))

        def hit(self, plant: all_plants):
            current_time = time.time()
            if current_time - self.last_damage >= 0.25/self.speed:
                plant.hit(self.damage)
                self.last_damage = current_time


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

class pea(pygame.sprite.Sprite):
    x: float
    y: int
    def __init__(self, x: float, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vanish = False
        self.image = pygame.image.load("plants_vs_zombies//images//pea.png").convert_alpha()
        self.rect = self.image.get_rect(center=(290+(x-0.5)*95, 95+(y-0.5)*130))

    def update(self, zombies: list):
        self.x += 0.1
        self.rect = self.image.get_rect(center=(290+(self.x-0.5)*95, 95+(self.y-0.5)*130))
        self.vanish = False
        for i in zombies:
            if self.rect.colliderect(i.rect) and self.y == i.y:
                if i.arm_hp > 0:
                    i.arm_hp -= 20
                    if i.arm_hp <= 0:
                        i.hp += i.arm_hp
                        i.arm_hp = 0
                        if i.type == "normal_kon" or i.type == "normal_can":
                            i.end_armor()
                else:
                    i.hp -= 20
                self.vanish = True
                break