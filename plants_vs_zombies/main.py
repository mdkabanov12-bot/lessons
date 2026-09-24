import pygame
pygame.init()

from functions import *
from models import *


H, W = 1181, 765
font = pygame.font.SysFont("Arial", 28)

sc = pygame.display.set_mode((H, W))
pygame.display.set_caption("Plants VS Zombies")

bg = pygame.image.load("plants_vs_zombies//images//передний_двор.png").convert()

Fps = 60
clock = pygame.time.Clock()

zombies = []
sunflowers = []
wallnuts = []
peashooters = [all_plants.peashooter(1, i) for i in range(1, 6)]
peas = []
suns = []

draw = [sunflowers, wallnuts, peashooters]
total_suns = 100

find_hp = True

last_vave = time.time()
first_vave = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                find_hp = not find_hp

    for sunf in sunflowers:
        sunf.sun_check()
        if sunf.ready_to_give:
            total_suns += 25
            suns.append(sun(sunf.x, sunf.y))

    sc.blit(bg, (0, 0))
    sun_text = font.render(str(total_suns) if total_suns <= 9990 else "9990+", True, (0, 0, 0))
    sc.blit(sun_text, (330, 8))
    
    draw_plants(sc, draw, find_hp, font)
    draw_suns(sc, suns)
    draw_zombies(sc, zombies, draw, find_hp, font)
    draw_shoot(sc, peas)
    for i in peashooters:
        new_pea = i.shoot(zombies)
        if new_pea != None:
            peas += [new_pea]

    for i in peas:
        i.update(zombies)

    current_time = time.time()
    if first_vave == True and current_time - last_vave >= 1:
        vave(zombies)
        first_vave = False
        last_vave = current_time
    elif (first_vave != True and current_time - last_vave >= 20) or (zombies == [] and first_vave != True):
        vave(zombies)
        last_vave = current_time
    
    pygame.display.update()
    clock.tick(Fps)