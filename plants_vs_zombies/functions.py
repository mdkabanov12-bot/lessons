import pygame
pygame.init()

from models import *
import random

cost_vaves = [1, 2, 2, 4]

zombies_tipe = [("normal", 0, 1), ("normal_kon", 200, 2), ("normal_can", 450, 4)]

def go_test(zom: all_zombies, draw: list[list[all_plants]]) -> all_plants|None:
    if round(zom.x, 1) - 0.7 >= int(zom.x) and round(zom.x, 1) - 0.8 <= int(zom.x):
        for plants in draw:
            for plant in plants:
                if plant.x == int(zom.x) and zom.y == plant.y:
                    return plant
        zom.may_go = True
        return None
    else:
        zom.may_go = True
        return None

def gen_rand_speed_normal():
    rand = random.randint(1, 5)
    speeds = {1 : 0.6, 2 : 0.8, 3 : 1, 4 : 1.2, 5 : 1.4}
    return speeds[rand]

def gen_rand_line() -> int:
    return random.randint(1, 5)

def gen_rand_zombie(max_cost) -> tuple[tuple, int]:
    pod_zom = []
    for i in zombies_tipe:
        if i[2] <= max_cost:
            pod_zom.append((i[0], i[1], i[2]))
    ind = random.randint(0, len(pod_zom)-1)
    max_cost -= pod_zom[ind][2]
    return (pod_zom[ind], max_cost)

def create_zombie(max_cost):
    zom, ret_cost = gen_rand_zombie(max_cost)
    if zom[0] == "normal" or zom[0] == "normal_kon" or zom[0] == "normal_can":
        return (all_zombies.normal(11, gen_rand_line(), zom[0], zom[1], gen_rand_speed_normal()), ret_cost)

def vave(zombies: list):
    global cost_vaves
    if cost_vaves != []:
        max_cost_vave = cost_vaves[0]
        while max_cost_vave != 0:
            zombie, max_cost_vave = create_zombie(max_cost_vave)
            zombies.append(zombie)
        cost_vaves = cost_vaves[1:]

def draw_plants(sc: pygame.Surface, draw: list[list[all_plants]], find_hp: bool, font):
    for plants in draw:
        for plant in plants:
            if plant.hp <= 0:
                plants.remove(plant)
                continue
            sc.blit(plant.image, plant.rect)
            if find_hp == False:
                hp_text = font.render(str(plant.hp), True, (255, 0, 0))
                sc.blit(hp_text, (plant.rect.x+20, plant.rect.y-30))

def draw_zombies(sc: pygame.Surface, zombies: list[list[all_zombies]], draw: list[list[all_plants]], find_hp: bool, font):
    for zom in zombies:
        sc.blit(zom.image, zom.rect)
        plant: all_plants|None = go_test(zom, draw)
        if zom.hp <= 0:
            zombies.remove(zom)
            continue
        
        if plant == None:
            zom.go()
        else:
            zom.hit(plant)

        if find_hp == False:
            hp_text = font.render(str(zom.hp), True, (255, 0, 0))
            arm_text = font.render(str(zom.arm_hp), True, (0, 0, 255))
            sc.blit(hp_text, (zom.rect.x-10, zom.rect.y-30))
            sc.blit(arm_text, (zom.rect.x+40, zom.rect.y-30))

def draw_suns(sc: pygame.Surface, suns: list[sun]):
    for sn in suns:
            sn.update()
            if sn.full_vanish == False:
                sc.blit(sn.image, sn.rect)
            else:
                suns.remove(sn)

def draw_shoot(sc: pygame.Surface, weapoon: list):
    for w in weapoon:
        if w.vanish == False:
            sc.blit(w.image, w.rect)
        else:
            weapoon.remove(w)