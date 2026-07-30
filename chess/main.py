from models import Figure, all_figures
from functions import *
import pygame
pygame.init()

sc = pygame.display.set_mode((600, 700))
pygame.display.set_caption("шахматы")

board: list[list[Figure|None]] = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

def res_main_bord(board: list[list[Figure|None]]|list):
    board: list[list[Figure|None]] = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]
    return board

figures = [
    Figure(("a", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("b", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("c", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("d", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("e", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("f", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("g", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("h", 2), all_figures.pawn, all_figures.white, "⌚", get_new_id()),
    Figure(("a", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("b", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("c", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("d", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("e", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("f", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("g", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("h", 7), all_figures.pawn, all_figures.black, "⌚", get_new_id()),
    Figure(("a", 1), all_figures.rook, all_figures.white, "⌚", get_new_id()),
    Figure(("h", 1), all_figures.rook, all_figures.white, "⌚", get_new_id()),
    Figure(("a", 8), all_figures.rook, all_figures.black, "⌚", get_new_id()),
    Figure(("h", 8), all_figures.rook, all_figures.black, "⌚", get_new_id()),
    Figure(("c", 1), all_figures.bishop, all_figures.white, "⌚", get_new_id()),
    Figure(("f", 1), all_figures.bishop, all_figures.white, "⌚", get_new_id()),
    Figure(("c", 8), all_figures.bishop, all_figures.black, "⌚", get_new_id()),
    Figure(("f", 8), all_figures.bishop, all_figures.black, "⌚", get_new_id()),
    Figure(("e", 1), all_figures.king, all_figures.white, "⌚", get_new_id()),
    Figure(("e", 8), all_figures.king, all_figures.black, "⌚", get_new_id()),
    Figure(("d", 1), all_figures.queen, all_figures.white, "⌚", get_new_id()),
    Figure(("d", 8), all_figures.queen, all_figures.black, "⌚", get_new_id()),
    Figure(("b", 1), all_figures.knight, all_figures.white, "⌚", get_new_id()),
    Figure(("g", 1), all_figures.knight, all_figures.white, "⌚", get_new_id()),
    Figure(("b", 8), all_figures.knight, all_figures.black, "⌚", get_new_id()),
    Figure(("g", 8), all_figures.knight, all_figures.black, "⌚", get_new_id()),
]

win = False
Fps = 30
clock = pygame.time.Clock()

def game_loop():
    global board
    board = res_main_bord(board)
    res_bord()
    current_click: Figure | None = None
    current_fig: Figure | None = None
    sost = 0 # 0 - фигурура не выбрана, 1 - фигура выбрана

    add_figurs(board, figures)

    current_player: all_figures = all_figures.white
    win: bool|str = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = event.pos
                if 100 < x < 500 and 200 < y < 600:
                    x, y = (x - 100)//50, (y-200)//50
                    current_click = detect_figure_by_kords(board, (x, 7-y))
                    if sost == 0:
                        if current_click == None:
                            pass
                        elif current_player == current_click.color:
                            detect_xod(board, current_click)
                            current_fig = current_click
                            sost = 1
                    elif sost == 1:
                        if current_click == None:
                            current_player = detect_xod_2(board, (x, 7-y), current_fig, current_player)
                            sost = 0
                            current_fig = None
                            win = win_check(board)
                        elif current_click.color != current_fig.color:
                            current_player = detect_xod_2(board, (x, 7-y), current_fig, current_player)
                            sost = 0
                            current_fig = None
                            win = win_check(board)
                        else:
                            detect_xod(board, current_click)
                            current_fig = current_click
                elif 490 < x < 590 and 5 < y < 35:
                    exit()

        drow_game(sc, board)
        pygame.display.flip()
        if win != False:
            break
        clock.tick(Fps)

game_loop()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = event.pos
            if 490 < x < 590 and 5 < y < 35:
                exit()
            elif 220 < x < 380 and 450 < y < 495:
                game_loop()
    
    drow_win(sc, board)
    pygame.display.flip()
    clock.tick(Fps)