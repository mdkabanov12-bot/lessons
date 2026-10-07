import pygame
import engine
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

font = pygame.font.SysFont("Arial", 32)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Clean Engine Demo")

cam = engine.Camera(x=0, y=7, z=-15)

cube_verts = [
    (-2, -2, -2), (2, -2, -2), (2, 2, -2), (-2, 2, -2),
    (-2, -2, 2), (2, -2, 2), (2, 2, 2), (-2, 2, 2)
]
cube_faces_indices = [
    [0, 1, 2], [0, 2, 3], [4, 5, 6], [4, 6, 7],
    [3, 2, 6], [3, 6, 7], [0, 1, 5], [0, 5, 4],
    [0, 3, 7], [0, 7, 4], [1, 2, 6], [1, 6, 5]
]
colors = [(255,0,0), (255,0,0), (0,255,0), (0,255,0), (0,0,255), (0,0,255), (255,165,0), (255,165,0), (138,43,226), (138,43,226), (255,255,0), (255,255,0)]

wall_verts = [
    (-5, -2, -10), (5, -2, -10), (-5, 4, -10), (5, 4, -10)
]
wall_faces_indices = [
    [0, 2, 3], [0, 1, 3], [1, 2, 3], [1, 2, 0]
]
wall_color = [(155, 155, 155)]

flor_verts = [[-10, -2, 10], [10, -2, 10], [10, -2, -10], [-10, -2, -10]]

flor_faces_indices = [
    [0, 1, 2], [0, 2, 3]
]

cub_data = engine.prepare_mesh_faces(cube_verts, cube_faces_indices, colors)
wall_data = engine.prepare_mesh_faces(wall_verts, wall_faces_indices, wall_color)
flor_data = engine.prepare_mesh_faces(flor_verts, flor_faces_indices, wall_color)

level_data = cub_data + wall_data

running = True
mouse_down = False
prev_mouse = pygame.mouse.get_pos()
mouse_press_cords = ()
last_time_fps = time.time()- 0.5

while running:
    dt = clock.tick(FPS)
    current_time = time.time()
    if current_time - last_time_fps >= 0.5:
        FPS_text = font.render(str(round(1000/dt, 1)), True, (255, 255, 255))
        last_time_fps = current_time
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                mouse_down = True
                pygame.mouse.set_visible(False)
                pygame.event.set_grab(True)
                prev_mouse = pygame.mouse.get_pos() 
                if mouse_press_cords == (): mouse_press_cords = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                mouse_down = False
                pygame.mouse.set_visible(True)
                pygame.event.set_grab(False)
                mouse_press_cords = ()

    keys = pygame.key.get_pressed()
    
    forward = 0
    if keys[pygame.K_w]: forward = -1
    if keys[pygame.K_s]: forward = 1
    
    right = 0
    if keys[pygame.K_d]: right = -1
    if keys[pygame.K_a]: right = 1
    
    up = 0
    if keys[pygame.K_SPACE]: up = 1
    if keys[pygame.K_LSHIFT]: up = -1

    cam.move(forward, right, up, dt)
    
    curr_mouse = pygame.mouse.get_pos()
    if mouse_down:
        dx = curr_mouse[0] - prev_mouse[0]
        dy = curr_mouse[1] - prev_mouse[1]
        cam.rotate(dx, dy)
        prev_mouse = mouse_press_cords
        pygame.mouse.set_pos(mouse_press_cords)
    else:
        prev_mouse = curr_mouse

    count = engine.render_mesh(screen, level_data, cam, WIDTH, HEIGHT, fov=90)

    screen.blit(FPS_text, (10, 10))
    pygame.display.flip()

pygame.quit()
