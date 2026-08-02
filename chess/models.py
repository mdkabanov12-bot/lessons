from dataclasses import dataclass

class kords:
    x: str
    y: int

class colors:
    red = (255, 0, 0)
    white = (235, 235, 235)
    gray = (55, 55, 55)
    black = (0, 0, 0)
    light_brown = (205, 133, 63)
    dark_brown = (150, 77, 34)

class all_figures:
    class pawn:
        pass
    class rook:
        pass
    class bishop:
        pass
    class king:
        pass
    class queen:
        pass
    class knight:
        pass
    class black:
        pass
    class white:
        pass

@dataclass(slots=True)
class Figure:
    kords: kords
    type: all_figures
    color: all_figures
    icon: str| None = "⌚"
    id: int| None = None

class main_figure:
    type: all_figures
    color: all_figures