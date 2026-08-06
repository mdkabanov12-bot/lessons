import pygame
pygame.init()

sc = pygame.display.set_mode((400, 500))
pygame.display.set_caption("крестики нолики")

font = pygame.font.SysFont("Arial", 32)

MENU = (55, 55, 55)
BOARD = (235, 235, 235)
LINES = (0, 0, 0)
CROSS = (255, 0, 0)
CIRCLE = (0, 0, 255)

board = [
    ['','',''],
    ['','',''],
    ['','','']
]

def drow_cross(x, y):
    pygame.draw.line(sc, CROSS, (x - 30, y - 30), (x + 30, y + 30), 10)
    pygame.draw.line(sc, CROSS, (x - 30, y + 30), (x + 30, y - 30), 10)

def drow_circle(x, y):
    pygame.draw.circle(sc, CIRCLE, (x, y), 40, 7)

def drow_figure(x, y, figure):
    x_cor = 100 + 100 * x
    y_cor = 200 + 100 * y
    if figure == "cross":
        drow_cross(x_cor, y_cor)
    else:
        drow_circle(x_cor, y_cor)

def drow_all_figures():
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "":
                drow_figure(j, i, board[i][j])

def drow_game_board():
    pygame.draw.rect(sc, BOARD, (0, 100, 400, 400))
    pygame.draw.line(sc, LINES, (50, 250), (350, 250), 10)
    pygame.draw.line(sc, LINES, (50, 350), (350, 350), 10)
    pygame.draw.line(sc, LINES, (150, 150), (150, 450), 10)
    pygame.draw.line(sc, LINES, (250, 150), (250, 450), 10)
    drow_menu()
    drow_all_figures()

def drow_menu():
    pygame.draw.rect(sc, MENU, (0, 0, 400, 100))
    pygame.draw.rect(sc, BOARD, (5, 5, 90, 90))
    pygame.draw.rect(sc, BOARD, (300, 5, 95, 40))
    global current_player
    if current_player == "cross":
        drow_cross(50, 50)
    else:
        drow_circle(50, 50)
    text_surface = font.render(current_player, True, BOARD)
    text_exit = font.render("EXIT", True, LINES)
    sc.blit(text_exit, (315, 5))
    sc.blit(text_surface, (100, 20))

def win_check() -> str|None:
    (a, b, c, d, e, f, g, h, i) = (board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])
    if a == e == i != "":
        return a
    elif a == d == g != "":
        return a
    elif a == b == c != "":
        return a
    elif e == b == h != "":
        return e
    elif e == c == g != "":
        return e
    elif e == d == f != "":
        return e
    elif i == h == g != "":
        return i
    elif i == f == c != "":
        return i
    elif a != "" and b != "" and c != "" and d != "" and e != "" and f != "" and g != "" and h != "" and i != "":
        return "drow"

def click(x_cl, y_cl):
    if 50 < x_cl < 350 and 150 < y_cl < 450:
        x = (x_cl - 50)//100
        y = (y_cl - 150)//100
        if board[y][x] == "":
            global current_player
            board[y][x] = current_player
            current_player = "cross" if current_player == "circle" else "circle"
    elif 300 < x_cl < 395 and 5 < y_cl < 45:
        exit()

def drow_win(winner):
    global win
    win = True
    drow_game_board()
    text_surface = font.render(f"winner: {winner}", True, BOARD)
    repeat_text = font.render("repeat", True, LINES)
    pygame.draw.rect(sc, MENU, (100, 200, 200, 100))
    sc.blit(text_surface, (115, 210))
    pygame.draw.rect(sc, BOARD, (150, 250, 90, 40))
    sc.blit(repeat_text, (160, 250))

FPS = 60
clock = pygame.time.Clock()

def game_loop():
    global winner, current_player
    win = False
    current_player = "cross"

    while not win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                click(x, y)
                winner = win_check()
                if winner != None:
                    win = True
                
    
        clock.tick(FPS)
        drow_game_board()
        pygame.display.flip()

game_loop()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            if 150 < x < 240 and 250 < y < 290:
                board = [
                    ['','',''],
                    ['','',''],
                    ['','','']
                ]
                game_loop()
            elif 300 < x < 395 and 5 < y < 45:
                exit()

    drow_win(winner)
    pygame.display.flip()
    clock.tick(FPS)