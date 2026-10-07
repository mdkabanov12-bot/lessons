import math
import pygame
import time

pygame.init()

font = pygame.font.SysFont("Arial", 32)

level = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#", "#", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
]

FPS = 30
WEIGHT, HEIGHT = 900, 600
clock = pygame.time.Clock()

sc = pygame.display.set_mode((WEIGHT, HEIGHT))
pygame.display.set_caption("re-caption")

def convert_to_radians(degres):
    return degres * math.pi / 180

class player(pygame.sprite.Sprite):

    speed = 4
    cords: tuple[float, float]|list[float, float]
    rotate: int

    def __init__(self, cords: tuple[float, float]|list[float, float], rotate: float):
        pygame.sprite.Sprite.__init__(self)
        self.cords = cords
        self.rotate = rotate
        self.rect = (*cords, 10)

    def update(self, up: int, right: int, dt: float):
        self.rotate = self.rotate % 360 if self.rotate >= 0 else self.rotate % -360
        self.cords = (self.cords[0] + right * dt, self.cords[1] + up * dt)
        self.rect = (*self.cords, 10)

class wall(pygame.sprite.Sprite):
    cords: tuple[float, float]|list[float, float]

    def __init__(self, cords: tuple[float, float]|list[float, float]):
        pygame.sprite.Sprite.__init__(self)
        self.cords = cords
        self.rect = (*cords, 60, 60)

class light(pygame.sprite.Sprite):
    cords: tuple[float, float]|list[float, float]
    rotate: float
    wall_distant: float
    rect: pygame.Rect

    def __init__(self, cords: tuple[float, float]|list[float, float], rotate: float):
        pygame.sprite.Sprite.__init__(self)
        self.cords = cords
        self.rotate = rotate
        self.wall_distant = 0
        self.rect = (*cords, 5)
        rad = convert_to_radians(self.rotate)
        self.delx = 5 * math.sin(rad)
        self.dely = 5 * math.cos(rad)

    def go_to_wall(self):
        self.cords = (self.cords[0]+10*self.delx, self.cords[1]-10*self.dely)
        self.wall_distant += 10

    def go_back(self):
        self.cords = (self.cords[0]-2*self.delx, self.cords[1]+2*self.dely)
        self.wall_distant -= 2

walls = []

cam = player((WEIGHT/2, HEIGHT/2), 0)
last_time_fps = time.time()
FPS_text = font.render("60", True, (255, 255, 255))
while True:
    dots = []
    dt = clock.tick(FPS)
    current_time = time.time()
    if current_time - last_time_fps >= 0.5:
        FPS_text = font.render(str(round(1000/dt, 1)), True, (255, 255, 255))
        last_time_fps = current_time
    sc.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    for i in range(len(level)):
        line = level[i]
        for j in range(len(line)):
            pixel = line[j]
            if pixel == "#":
                cords = (j*60, i*60)
                pix = wall(cords)
                walls.append(pix.rect)
                # pygame.draw.rect(sc, (255, 255, 0), (pix.rect))

    keys = pygame.key.get_pressed()
    rd = convert_to_radians(cam.rotate)
    x = cam.speed*(round(rd, 2))
    y = cam.speed*(round(rd, 2))
    up = 0
    right = 0
    if keys[pygame.K_w]:
        up -= y
        right += x
    if keys[pygame.K_s]:
        up += y
        right -= x
    if keys[pygame.K_a]:
        cam.rotate -= 5
    if keys[pygame.K_d]: 
        cam.rotate += 5

    cam.update(up, right, dt/100)
    rd = convert_to_radians(cam.rotate)
    rx = 10*(round(math.sin(rd), 2))
    ry = 10*(round(math.cos(rd), 2))

    # pygame.draw.circle(sc, (255, 0, 0), cam.rect[:2], cam.rect[2])
    # pygame.draw.circle(sc, (0, 255, 0), (cam.cords[0]+rx, cam.cords[1]-ry), 3)
    i = 0
    for deldeg in range(-60, 61, 8):
        l = light((cam.cords[0]+rx, cam.cords[1]-ry), cam.rotate + deldeg)
        is_colide = False
        while is_colide == False and l.wall_distant <= 200:
            li_x = l.cords[0]
            li_y = l.cords[1]
            for w in walls:
                if w[0] <= li_x <= w[0] + w[2] and w[1] <= li_y <= w[1] + w[3]:
                    is_colide = True
            l.go_to_wall()
        if l.wall_distant <= 200:
            while is_colide == True:
                li_x = l.cords[0]
                li_y = l.cords[1]
                for w in walls:
                    if w[0] <= li_x <= w[0] + w[2] and w[1] <= li_y <= w[1] + w[3]:
                        is_colide = False
                l.go_back()
            dots.append((l.cords, l.wall_distant, i))
        else:
            dots.append((None, i))
        i += 1
        l.kill()
    # for dot in dots:
    #     if dot[0]:
    #         pygame.draw.circle(sc, (255, 255, 255), (dot[0]), 3)

    for dot in dots:
        if dot[0]:
           pygame.draw.rect(sc, (0, 0, 255), (dot[2]*60, dot[1]*5, 60, HEIGHT-dot[1]*10))
        else:
            pygame.draw.rect(sc, (0, 0, 200), (dot[1]*60, 280, 60, 40))

    sc.blit(FPS_text, (10, 10))
    pygame.display.flip()