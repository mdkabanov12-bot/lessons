import pygame
pygame.init()

from models import *


H, W = 1181, 765
font = pygame.font.SysFont("Arial", 32)

sc = pygame.display.set_mode((H, W))
pygame.display.set_caption("Plants VS Zombies")

bg = pygame.image.load("plants_vs_zombies//images//передний_двор.png").convert()

Fps = 60
clock = pygame.time.Clock()

s1 = all_plants.sunflower(1, 1)
s2 = all_plants.sunflower(1, 2)
nut1 = all_plants.wallnut(2, 1)

sunflowers = [s2, s1]
wallnuts = [nut1]
suns = []

draw = [sunflowers, wallnuts]
total_suns = 100

find_hp = True

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

    for plants in draw:
        for plant in plants:
            if plant.live == False:
                plants.remove(plant)
                continue
            sc.blit(plant.image, plant.rect)
            if find_hp == False:
                hp_text = font.render(str(plant.hp), True, (255, 0, 0))
                sc.blit(hp_text, (plant.rect.x+20, plant.rect.y-30))
    
    for sn in suns:
        sn.update()
        if sn.full_vanish == False:
            sc.blit(sn.image, sn.rect)
        else:
            suns.remove(sn)
    
    pygame.display.update()
    clock.tick(Fps)