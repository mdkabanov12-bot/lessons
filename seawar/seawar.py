import pygame
pygame.init()

sc = pygame.display.set_mode((800, 500))
pygame.display.set_caption("морской бой")

global font
font = pygame.font.SysFont("Arial", 32)

# DECODER = {
#     0 : "empty",
#     1 : "ship",
#     2 : "kiled",
#     3 : "no_shoot",
# }

boards = [
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],

    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]

def res_boards():
    global boards
    boards = [
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ],

    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    ]

MENU_MAIN = (55, 55, 55)
MENU_SCREEN = GAME_MAIN = (255, 255, 255)
GAME_LINES = GAME_SHIPS = (0, 0, 0)
RED_TEAM = (255, 0, 0)
BLUE_TEAM = (0, 0, 255)
COUNT_SHIPS = 15

def drow_screen(end=0):
    drow_menu()
    drow_game_board(end)

def drow_menu():
    global current_team
    pygame.draw.rect(sc, MENU_MAIN, (0, 0, 800, 100))
    pygame.draw.rect(sc, MENU_SCREEN, (10, 10, 50, 50))
    pygame.draw.rect(sc, RED_TEAM if current_team == "red" else BLUE_TEAM, (11, 11, 48, 48))
    pygame.draw.rect(sc, MENU_SCREEN, (605, 5, 190, 40))
    exit_text = font.render("EXIT", True, MENU_MAIN)
    sc.blit(exit_text, (675, 10))

def drow_bord_player(number, end = 0):
    global game_start
    pygame.draw.line(sc, GAME_LINES, (400*number+40, 140), (400*number+40, 460), 2)
    pygame.draw.line(sc, GAME_LINES, (400*number+40, 140), (400*number+360, 140), 2)
    pygame.draw.line(sc, GAME_LINES, (400*number+360, 140), (400*number+360, 460), 2)
    pygame.draw.line(sc, GAME_LINES, (400*number+40, 460), (400*number+360, 460), 2)

    for i in range(10):
        pygame.draw.line(sc, GAME_LINES, (400*number+40 + 32*i, 140), (400*number+40 + 32*i, 460))

    for i in range(10):
        pygame.draw.line(sc, GAME_LINES, (400*number+40, 140 + 32*i), (400*number+360, 140 + 32*i))

    for i in range(10):
        for j in range(10):
            kub = boards[number][i][j]
            team = "red" if number == 0 else "blue"
            if kub == 0:
                pass
            elif (kub == 1 and team == current_team and not game_start) or (kub == 1 and end == 1):
                full_kub(24+(j+1)*32, 124+(i+1)*32, "1", number)
            elif kub == 2:
                full_kub(24+(j+1)*32, 124+(i+1)*32, "2", number)
            elif kub == 3:
                full_kub(24+(j+1)*32, 124+(i+1)*32, "3", number)

def drow_game_board(end = 0):
    global winner
    pygame.draw.rect(sc, GAME_MAIN, (0, 100, 800, 400))
    pygame.draw.line(sc, GAME_LINES, (400, 100), (400, 500), 2)
    drow_bord_player(0, end)
    drow_bord_player(1, end)
    pygame.draw.rect(sc, RED_TEAM, (365, 105, 30, 30))
    pygame.draw.rect(sc, BLUE_TEAM, (405, 105, 30, 30))

def drow_win(winner):
    drow_screen(1)
    repeat_text = font.render("REPEAT", True, MENU_MAIN)
    pygame.draw.rect(sc, MENU_SCREEN, (300, 20, 200, 60))
    sc.blit(repeat_text, (345, 30))
    winner_text = font.render("WINNER", True, GAME_LINES)
    sc.blit(winner_text, (250 if winner == "red" else 450, 100))

def full_kub(x, y, type, number):
    if type == "1":
        pygame.draw.rect(sc, GAME_SHIPS, (x-16+400*number, y-16, 32, 32))
    elif type == "2":
        pygame.draw.line(sc, GAME_LINES, (x-15+400*number, y-16), (x+14+400*number, y+16), 6)
        pygame.draw.line(sc, GAME_LINES, (x+14+400*number, y-16), (x-15+400*number, y+16), 6)
    elif type == "3":
        pygame.draw.circle(sc, GAME_LINES, (x+400*number, y), 4)

def click(x, y, number):
    global count_1, count_2, current_team
    if game_start == False:
        if number == 0:
            x_cor = (x - 40) // 32
            y_cor = (y - 140) // 32
            if boards[0][y_cor][x_cor] != 1:
                a, b, c, d, e, f, g, h = boards[0][y_cor-1 if y_cor != 0 else 0][x_cor-1 if x_cor != 0 else 0], boards[0][y_cor - 1 if y_cor != 0 else 0][x_cor], boards[0][y_cor - 1 if y_cor != 0 else 0][x_cor+1 if x_cor != 9 else 9], boards[0][y_cor][x_cor - 1 if x_cor != 0 else 0], boards[0][y_cor][x_cor+1 if x_cor != 9 else 9], boards[0][y_cor+1 if y_cor != 9 else 9][x_cor-1 if x_cor != 0 else 0], boards[0][y_cor+1 if y_cor != 9 else 9][x_cor], boards[0][y_cor+1 if y_cor!=9 else 9][x_cor+1 if x_cor!= 9 else 9]
                if a != 1 and b != 1 and c != 1 and d != 1 and e != 1 and f != 1 and g != 1 and h != 1:
                    boards[0][y_cor][x_cor] = 1
                    count_1 += 1
        else:
            x_cor = (x - 440) // 32
            y_cor = (y - 140) // 32
            if boards[1][y_cor][x_cor] != 1:
                a, b, c, d, e, f, g, h = boards[1][y_cor-1 if y_cor != 0 else 0][x_cor-1 if x_cor != 0 else 0], boards[1][y_cor - 1 if y_cor != 0 else 0][x_cor], boards[1][y_cor - 1 if y_cor != 0 else 0][x_cor+1 if x_cor != 9 else 9], boards[1][y_cor][x_cor - 1 if x_cor != 0 else 0], boards[1][y_cor][x_cor+1 if x_cor != 9 else 9], boards[1][y_cor+1 if y_cor != 9 else 9][x_cor-1 if x_cor != 0 else 0], boards[1][y_cor+1 if y_cor != 9 else 9][x_cor], boards[1][y_cor+1 if y_cor!=9 else 9][x_cor+1 if x_cor!= 9 else 9]
                if a != 1 and b != 1 and c != 1 and d != 1 and e != 1 and f != 1 and g != 1 and h != 1:
                    boards[1][y_cor][x_cor] = 1
                    count_2+=1
    else:
        if number == 0:
            x_cor = (x - 440) // 32
            y_cor = (y - 140) // 32
            if boards[1][y_cor][x_cor] == 1:
                boards[1][y_cor][x_cor] = 2
                count_2-=1
            elif boards[1][y_cor][x_cor] == 2 or boards[1][y_cor][x_cor] == 3:
                pass
            else:
                boards[1][y_cor][x_cor] = 3
                current_team = "blue"
        else:
            x_cor = (x - 40) // 32
            y_cor = (y - 140) // 32
            if boards[0][y_cor][x_cor] == 1:
                boards[0][y_cor][x_cor] = 2
                count_1-=1
            elif boards[0][y_cor][x_cor] == 2 or boards[0][y_cor][x_cor] == 3:
                pass
            else:
                boards[0][y_cor][x_cor] = 3
                current_team = "red"

def win_check()->str|None:
    global count_1, count_2
    if count_1 == 0: return "blue"
    elif count_2 == 0: return "red"

Fps = 30
clock = pygame.time.Clock()

def game_loop():
    global game_start, winner, count_1, count_2, win, current_team, win, ready
    winner = ""
    win = False
    current_team = "red"
    game_start = False
    count_1 = 0
    count_2 = 0
    ready = False

    while not ready:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 605 < x < 795 and 5 < y < 45:
                    exit()
                if 40 < x < 360 and 140 < y < 460 and current_team == "red":
                    click(x, y, 0)
                elif 440 < x < 760 and 140 < y < 460 and current_team == "blue":
                    click(x, y, 1)
                    if count_2 == COUNT_SHIPS:
                        ready = True
                        current_team = "red"
                        game_start = True
        if count_1 == COUNT_SHIPS:
            current_team = "blue"
            count_1+=1
        drow_screen()
        pygame.display.flip()
        clock.tick(Fps)
    count_1-=1
    while not win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 605 < x < 795 and 5 < y < 45:
                    exit()
                if 40 < x < 360 and 140 < y < 460 and current_team == "blue":
                    click(x, y, 1)
                    winner = win_check()
                    if winner == None:
                        pass
                    else:
                        win = True
                        drow_win(winner)
                elif 440 < x < 760 and 140 < y < 460 and current_team == "red":
                    click(x, y, 0)
                    winner = win_check()
                    if winner == None:
                        pass
                    else:
                        win = True
                        drow_win(winner)

        drow_screen()
        pygame.display.flip()
        clock.tick(Fps)

game_loop()
while win:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            if 605 < x < 795 and 5 < y < 45:
                exit()
            elif 300 < x < 500 and 20<y<80:
                res_boards()
                game_loop()
    drow_win(winner)
    pygame.display.flip()
    clock.tick(Fps)