from models import Figure, kords, colors, all_figures, main_figure
import pygame
pygame.init()

font = pygame.font.SysFont("Arial", 32)
global_id = 0

def res_bord():
    global board_2
    board_2 = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

def get_new_id():
    global global_id
    global_id+=1
    return global_id

def decode_x_pos_1(x: str)->int:
    decoder = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}
    return decoder[x]

def decode_x_pos_2(x: int)->str:
    decoder = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}
    return decoder[x]

def add_figure(board: list[list[Figure|None]], figure: Figure|None = None):
    kor: kords = figure.kords
    kord: tuple = (decode_x_pos_1(kor[0]), kor[1])
    board[kord[1]-1][kord[0]-1] = figure

def add_figurs(board: list[list[Figure|None]], figurs: list[Figure]):
    for fig in figurs:
        add_figure(board, fig)

def detect_figure_by_kords(board: list[list[Figure| None]], kords: tuple) -> tuple | None:
    (x, y) = kords
    fig: Figure|None = board[y][x]
    return fig

class all_detect_xod:
    class pawn:
        def detect_main(board: list[list[Figure|None]], fig_kord: tuple, color: all_figures):
            (x, y) = fig_kord
            all_detect_xod.pawn.detect_near(board, fig_kord, color)
            if (color == all_figures.white and y != 7) or (color == all_figures.black and y != 0):
                if (board[y+1][x] == None and color == all_figures.white) or (board[y-1][x] == None and color == all_figures.black):
                    add_xod((x, (y+1) if color == all_figures.white else (y-1)))
                    if (y == 1 and color == all_figures.white) or (y ==6 and color == all_figures.black):
                        all_detect_xod.pawn.detect_second(board, fig_kord, color)
        def detect_second(board: list[list[Figure|None]], fig_kord: tuple, color: all_figures):
            (x, y) = fig_kord
            if color == all_figures.white:
                if board[y+2][x] == None:
                    add_xod((x, y + 2))
            if color == all_figures.black:
                if board[y-2][x] == None:
                    add_xod((x, y - 2))
        def detect_near(board: list[list[Figure|None]], fig_kord: tuple, color: all_figures):
            (x, y) = fig_kord
            if color == all_figures.white:
                try:
                    if board[y+1][x-1] != None:
                        fig = detect_figure_by_kords(board, (x-1, y+1))
                        if fig.color == all_figures.black:
                            add_xod((x-1, y+1))
                except:
                    pass
                try:
                    if board[y+1][x+1] != None:
                        fig = detect_figure_by_kords(board, (x+1, y+1))
                        if fig.color == all_figures.black:
                            add_xod((x+1, y+1))
                except:
                    pass
            else:
                try:
                    if board[y-1][x-1] != None:
                        fig = detect_figure_by_kords(board, (x-1, y-1))
                        if fig.color == all_figures.white:
                            add_xod((x-1, y-1))
                except:
                    pass
                try:
                    if board[y-1][x+1] != None:
                        fig = detect_figure_by_kords(board, (x+1, y-1))
                        if fig.color == all_figures.white:
                            add_xod((x+1, y-1))
                except:
                    pass
    class knight:
        def detect(board: list[list[Figure|None]], fig_kord: tuple, color: all_figures):
            try:
                (x, y) = fig_kord
                if board[y+2][x+1]==None:
                    add_xod((x+1, y+2))
                else:
                    fig : Figure = board[y+2][x+1]
                    if fig.color  != color:
                        add_xod((x+1, y+2))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y+2][x-1]==None:
                    add_xod((x-1, y+2))
                else:
                    fig : Figure = board[y+2][x-1]
                    if fig.color  != color:
                        add_xod((x-1, y+2))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y-2][x+1]==None:
                    add_xod((x+1, (y-2) if y-2 >= 0 else 50))
                else:
                    fig : Figure = board[y-2][x+1]
                    if fig.color  != color:
                        add_xod((x+1, (y-2) if y-2 >= 0 else 50))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y-2][x-1]==None:
                    add_xod(((x-1) if x >= 1 else 50, (y-2) if y-2 >= 0 else 50))
                else:
                    fig : Figure = board[y-2][x-1]
                    if fig.color  != color:
                        add_xod(((x-1) if x >= 1 else 50, (y-2) if y-2 >= 0 else 50))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y+1][x+2]==None:
                    add_xod((x+2, y+1))
                else:
                    fig : Figure = board[y+1][x+2]
                    if fig.color  != color:
                        add_xod((x+2, y+1))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y+1][x-2]==None:
                    add_xod(((x-2) if x >= 2 else 50, y+1))
                else:
                    fig : Figure = board[y+1][x-2]
                    if fig.color  != color:
                        add_xod(((x-2) if x >= 2 else 50, y+1))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y-1][x+2]==None:
                    add_xod((x+2, (y-1) if y >= 1 else 50))
                else:
                    fig : Figure = board[y-1][x+2]
                    if fig.color  != color:
                        add_xod((x+2, (y-1) if y >= 1 else 50))
            except:
                pass
            try:
                (x, y) = fig_kord
                if board[y-1][x-2]==None:
                    add_xod(((x-2) if x >= 2 else 50, (y-1) if y >= 1 else 50))
                else:
                    fig : Figure = board[y-1][x-2]
                    if fig.color  != color:
                        add_xod(((x-2) if x >= 2 else 50, (y-1) if y >= 1 else 50))
            except:
                pass
    class rook:
        def detect_main(board: list[list[Figure|None]], kords: tuple, color: all_figures):
            all_detect_xod.rook.detect_1(board, kords, color, 0)
            all_detect_xod.rook.detect_2(board, kords, color, 0)
            all_detect_xod.rook.detect_3(board, kords, color, 0)
            all_detect_xod.rook.detect_4(board, kords, color, 0)
        def detect_1(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if board[y+delta+1][x] == None:
                    add_xod((x, y+delta+1))
                    all_detect_xod.rook.detect_1(board, kords, color, delta+1)
                else:
                    fig: Figure = board[y+delta+1][x]
                    if fig.color != color: add_xod((x, y+delta+1))
            except:
                pass
        def detect_2(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if y - delta-1 >= 0:
                    if board[y-delta-1][x] == None:
                        add_xod((x, y-delta-1))
                        all_detect_xod.rook.detect_2(board, kords, color, delta+1)
                    else:
                        fig: Figure = board[y-delta-1][x]
                        if fig.color != color: add_xod((x, y-delta-1))
            except:
                pass
        def detect_3(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if board[y][x+delta+1] == None:
                    add_xod((x+delta+1, y))
                    all_detect_xod.rook.detect_3(board, kords, color, delta+1)
                else:
                    fig: Figure = board[y][x+delta+1]
                    if fig.color != color: add_xod((x+delta+1, y))
            except:
                pass
        def detect_4(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if x - delta-1 >= 0:
                    if board[y][x-delta-1] == None:
                        add_xod((x-delta-1, y))
                        all_detect_xod.rook.detect_4(board, kords, color, delta+1)
                    else:
                        fig: Figure = board[y][x-delta-1]
                        if fig.color != color: add_xod((x-delta-1, y))
            except:
                pass
    class bishop:
        def detect_main(board: list[list[Figure|None]], kords: tuple, color: all_figures):
            all_detect_xod.bishop.detect_1(board, kords, color, 0)
            all_detect_xod.bishop.detect_2(board, kords, color, 0)
            all_detect_xod.bishop.detect_3(board, kords, color, 0)
            all_detect_xod.bishop.detect_4(board, kords, color, 0)
        def detect_1(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if board[y+delta+1][x+delta+1] == None:
                    add_xod((x+delta+1, y + delta + 1))
                    all_detect_xod.bishop.detect_1(board, kords, color, delta+1)
                else:
                    fig: Figure = board[y+delta+1][x+delta+1]
                    if fig.color != color: add_xod((x+delta+1, y+delta+1))
            except:
                pass
        def detect_2(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if y-delta-1>=0:
                    if board[y-delta-1][x+delta+1] == None:
                        add_xod((x+delta+1, y - delta - 1))
                        all_detect_xod.bishop.detect_2(board, kords, color, delta+1)
                    else:
                        fig: Figure = board[y-delta-1][x+delta+1]
                        if fig.color != color: add_xod((x+delta+1, y-delta-1))
            except:
                pass
        def detect_3(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if y-delta-1>=0 and x - delta - 1>=0:
                    if board[y-delta-1][x-delta-1] == None:
                        add_xod((x-delta-1, y - delta - 1))
                        all_detect_xod.bishop.detect_3(board, kords, color, delta+1)
                    else:
                        fig: Figure = board[y-delta-1][x-delta-1]
                        if fig.color != color: add_xod((x-delta-1, y-delta-1))
            except:
                pass
        def detect_4(board: list[list[Figure|None]], kords: tuple, color: all_figures, delta: int):
            (x, y) = kords
            try:
                if x - delta - 1>=0:
                    if board[y+delta+1][x-delta-1] == None:
                        add_xod((x-delta-1, y + delta + 1))
                        all_detect_xod.bishop.detect_4(board, kords, color, delta+1)
                    else:
                        fig: Figure = board[y+delta+1][x-delta-1]
                        if fig.color != color: add_xod((x-delta-1, y+delta+1))
            except:
                pass
    class queen:
        def detect(board: list[list[Figure|None]], kords:tuple, color: all_figures):
            all_detect_xod.bishop.detect_main(board, kords, color)
            all_detect_xod.rook.detect_main(board, kords, color)
    class king:
        def detect(board: list[list[Figure|None]], kords: tuple, color:all_figures):
            (x, y) = kords
            try:
                if board[y+1][x+1]==None:
                    add_xod((x+1, y+1))
                else:
                    fig : Figure = board[y+1][x+1]
                    if fig.color != color: add_xod((x+1, y+1))
            except:
                pass
            try:
                if board[y+1][x]==None:
                    add_xod((x, y+1))
                else:
                    fig : Figure = board[y+1][x]
                    if fig.color != color: add_xod((x, y+1))
            except:
                pass
            try:
                if x-1>= 0:
                    if board[y+1][x-1]==None:
                        add_xod((x-1, y+1))
                    else:
                        fig : Figure = board[y+1][x-1]
                        if fig.color != color: add_xod((x-1, y+1))
            except:
                pass
            try:
                if board[y][x+1]==None:
                    add_xod((x+1, y))
                else:
                    fig : Figure = board[y][x+1]
                    if fig.color != color: add_xod((x+1, y))
            except:
                pass
            try:
                if x-1>= 0:
                    if board[y][x-1]==None:
                        add_xod((x-1, y))
                    else:
                        fig : Figure = board[y][x-1]
                        if fig.color != color: add_xod((x-1, y))
            except:
                pass
            try:
                if y-1>= 0:
                    if board[y-1][x+1]==None:
                        add_xod((x+1, y-1))
                    else:
                        fig : Figure = board[y-1][x+1]
                        if fig.color != color: add_xod((x+1, y-1))
            except:
                pass
            try:
                if y-1>= 0:
                    if board[y-1][x]==None:
                        add_xod((x, y-1))
                    else:
                        fig : Figure = board[y-1][x]
                        if fig.color != color: add_xod((x, y-1))
            except:
                pass
            try:
                if y-1>= 0 and x - 1>=0:
                    if board[y-1][x-1]==None:
                        add_xod((x-1, y-1))
                    else:
                        fig : Figure = board[y-1][x-1]
                        if fig.color != color: add_xod((x-1, y-1))
            except:
                pass

def detect_xod_2(board : list[list[Figure|None]], kord_click: tuple, figure: Figure, current_player: all_figures) -> all_figures:
    (new_x, new_y) = kord_click
    if board_2[new_y][new_x] == "X":
        went_figure(board, figure, (decode_x_pos_2(new_x+1), new_y+1))
        current_player = all_figures.white if current_player == all_figures.black else all_figures.black
        res_bord()
        return current_player
    else:
        res_bord()
        return current_player

def detect_xod(board: list[list[Figure | None]],figure: Figure)->Figure|None:
    global board_2
    res_bord()
    kords_figure = (decode_x_pos_1(figure.kords[0])-1, figure.kords[1]-1)
    if figure.type == all_figures.pawn:
        all_detect_xod.pawn.detect_main(board, kords_figure, figure.color)
    elif figure.type == all_figures.knight:
        all_detect_xod.knight.detect(board, kords_figure, figure.color)
    elif figure.type == all_figures.rook:
        all_detect_xod.rook.detect_main(board, kords_figure, figure.color)
    elif figure.type == all_figures.bishop:
        all_detect_xod.bishop.detect_main(board, kords_figure, figure.color)
    elif figure.type == all_figures.queen:
        all_detect_xod.queen.detect(board, kords_figure, figure.color)
    elif figure.type == all_figures.king:
        all_detect_xod.king.detect(board, kords_figure, figure.color)
        

def add_xod(kords: tuple):
    global board_2
    board_2[kords[1]][kords[0]] = "X"

def drow_xod(sc: pygame.Surface, kords: tuple):
    (x, y) = kords
    x, y = x * 50 + 125, y * 50 + 225
    pygame.draw.circle(sc, colors.red, (x, y), 10)

def drow_all_xod(sc: pygame.Surface):
    global board_2
    for i in range(8):
        for j in range(8):
            if board_2[i][j] == "X":
                drow_xod(sc, (j, 7-i))

def get_figure_by_kords(board: list[list[Figure|None]], kords: kords) -> Figure|None:
    for fig in board:
        if fig.kords == kords:
            return fig

def went_figure(board: list[list[Figure|None]], figur: Figure, new_kords: kords) -> Figure|None:
    old_kord: kords = figur.kords
    old_kords = (decode_x_pos_1(old_kord[0]), old_kord[1])
    board[old_kords[1]-1][old_kords[0]-1] = None
    if figur.type != all_figures.pawn:
        add_figure(board, Figure(new_kords, figur.type, figur.color, figur.icon, figur.id))
        return Figure(new_kords, figur.type, figur.color, figur.icon, figur.id)
    elif new_kords[1] == 1 or new_kords[1] == 8:
        add_figure(board, Figure(new_kords, all_figures.queen, figur.color, figur.icon, figur.id))
        return Figure(new_kords, all_figures.queen, figur.color, figur.icon, figur.id)
    else:
        add_figure(board, Figure(new_kords, figur.type, figur.color, figur.icon, figur.id))
        return Figure(new_kords, figur.type, figur.color, figur.icon, figur.id)

def drow_kletku(sc: pygame.Surface, kord:tuple, color):
    pygame.draw.rect(sc, color, ((kord[0]*50)+100, (kord[1]*50)+200, 50, 50))

def drow_all_kletki(sc: pygame.Surface):
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 1:
                drow_kletku(sc, (j, i), colors.dark_brown)
            else:
                drow_kletku(sc, (j, i), colors.light_brown)

class drow_figure:
    def pawn(sc: pygame.Surface, kord: tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+5, y+35, 40, 10))
        pygame.draw.polygon(sc, color, [(x+10, y+35), (x+20, y+15), (x+30, y+15), (x+40, y+35)])
        pygame.draw.circle(sc, color, (x+25, y+15), 10)
    def rook(sc: pygame.Surface, kord:tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+5, y+35, 40, 10))
        pygame.draw.rect(sc, color, (x+10, y+10, 30, 25))
    def bishop(sc: pygame.Surface, kord: tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+10, y+35, 30, 10))
        pygame.draw.polygon(sc, color, [(x+15, y+35), (x+20, y+5), (x+30, y+5), (x+35, y+35)])
    def queen(sc: pygame.Surface, kord: tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+5, y+35, 40, 10))
        pygame.draw.polygon(sc, color, [(x+10, y+35), (x+5, y+20), (x+10, y+25), (x+17, y+5), (x+25, y+15), (x+33, y+5), (x+40, y+25), (x+45, y+20), (x+40, y+35)])
    def king(sc: pygame.Surface, kord: tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+5, y+35, 40, 10))
        pygame.draw.polygon(sc, color, [(x+10, y+35), (x+10, y+25), (x+20, y+10), (x+30, y+10), (x+40, y+25), (x+40, y+35), (x+35, y+35), (x+35, y+25), (x+30, y+20), (x+20, y+20), (x+15, y+25), (x+15, y+35)])
        pygame.draw.rect(sc, color, (x+22.5, y+20, 7.5, 15))
        # pygame.draw.circle(sc, color, (x+25, y+15), 5)
    def knight(sc: pygame.Surface, kord: tuple, color: tuple):
        (x, y) = kord
        x, y = x*50+100, y*50+200
        pygame.draw.rect(sc, color, (x+7.5, y+35, 35, 10))
        x+=2
        pygame.draw.polygon(sc, color, [(x+15, y+35), (x+18, y+25), (x+15, y+23), (x+14, y+20), (x+14, y+10), (x+18, y+5), (x+23, y+5), (x+30, y+10), (x+32, y+10), (x+32, y+12), (x+27, y+14), (x+32, y+15), (x+32, y+17), (x+35, y+20), (x+33, y+22), (x+30, y+17), (x+28, y+35)])

def drow_all_figurs(sc: pygame.Surface, board:list[list[Figure|None]]):
    for i in range(8):
        for j in range(8):
            kletka: Figure|None = board[i][j]
            if kletka == None:
                pass
            else:
                (ty, col) = get_type_color(kletka)
                if ty == all_figures.pawn and col == all_figures.white:
                    drow_figure.pawn(sc, (j, 7-i), colors.white)
                elif ty == all_figures.pawn and col == all_figures.black:
                    drow_figure.pawn(sc, (j, 7-i), colors.black)
                elif ty == all_figures.rook and col == all_figures.white:
                    drow_figure.rook(sc, (j, 7-i), colors.white)
                elif ty == all_figures.rook and col == all_figures.black:
                    drow_figure.rook(sc, (j, 7-i), colors.black)
                elif ty == all_figures.bishop and col == all_figures.white:
                    drow_figure.bishop(sc, (j, 7-i), colors.white)
                elif ty == all_figures.bishop and col == all_figures.black:
                    drow_figure.bishop(sc, (j, 7-i), colors.black)
                elif ty == all_figures.queen and col == all_figures.white:
                    drow_figure.queen(sc, (j, 7-i), colors.white)
                elif ty == all_figures.queen and col == all_figures.black:
                    drow_figure.queen(sc, (j, 7-i), colors.black)
                elif ty == all_figures.king and col == all_figures.white:
                    drow_figure.king(sc, (j, 7-i), colors.white)
                elif ty == all_figures.king and col == all_figures.black:
                    drow_figure.king(sc, (j, 7-i), colors.black)
                elif ty == all_figures.knight and col == all_figures.white:
                    drow_figure.knight(sc, (j, 7-i), colors.white)
                elif ty == all_figures.knight and col == all_figures.black:
                    drow_figure.knight(sc, (j, 7-i), colors.black)

def get_type_color(figure:Figure)->tuple:
    return (figure.type, figure.color)

def win_check(board: list[list[Figure|None]]) -> str|bool:
    w_d = True
    b_d = True
    for i in board:
        for j in i:
            j: Figure|None = j
            if j == None:
                pass
            elif j.type == all_figures.king and j.color == all_figures.white:
                w_d = False
            elif j.type == all_figures.king and j.color == all_figures.black:
                b_d = False
    if w_d == True:
        return "black"
    elif b_d == True:
        return "white"
    else:
        return False

def drow_board(sc: pygame.Surface, board:list[list[Figure|None]]):
    pygame.draw.rect(sc, (255, 255, 255), (0, 100, 600, 600))
    drow_all_kletki(sc)
    drow_all_figurs(sc, board)
    drow_all_xod(sc)

def drow_menu(sc: pygame.Surface):
    pygame.draw.rect(sc, colors.gray, (0, 0, 600, 100))
    pygame.draw.rect(sc, colors.white, (490, 5, 100, 30))
    exit_text = font.render("EXIT", True, colors.black)
    sc.blit(exit_text, (510, 3))

def drow_game(sc: pygame.Surface, board:list[list[Figure|None]]):
    drow_board(sc, board)
    drow_menu(sc)

def drow_win(sc: pygame.Surface, board: list[list[Figure|None]]):
    drow_game(sc, board)
    pygame.draw.rect(sc, colors.gray, (150, 300, 300, 200))
    pygame.draw.rect(sc, colors.white, (220, 450, 160, 45))
    restart_text = font.render("RESTART", True, colors.black)
    sc.blit(restart_text, (240, 455))