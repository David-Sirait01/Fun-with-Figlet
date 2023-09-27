from colorama import Fore, Back, init, Style

# Total semua : 15
sz = 15

class Text:
    back_arr = [
        # Warna Tua
        # "Back.BLACK",
        "Back.RED",
        "Back.GREEN",
        "Back.YELLOW",
        "Back.BLUE",
        "Back.MAGENTA",
        "Back.CYAN",
        "Back.WHITE",
        # "Back.RESET",

        # Warna Muda
        "Back.LIGHTBLACK_EX",
        "Back.LIGHTRED_EX",
        "Back.LIGHTGREEN_EX",
        "Back.LIGHTYELLOW_EX",
        "Back.LIGHTBLUE_EX",
        "Back.LIGHTMAGENTA_EX",
        "Back.LIGHTCYAN_EX",
        "Back.LIGHTWHITE_EX"
    ]

    fore_arr = [
        # Warna Tua
        # "Fore.BLACK",
        "Fore.RED",
        "Fore.GREEN",
        "Fore.YELLOW",
        "Fore.BLUE",
        "Fore.MAGENTA",
        "Fore.CYAN",
        "Fore.WHITE",
        # "Fore.RESET",

        # Warna Muda
        "Fore.LIGHTBLACK_EX",
        "Fore.LIGHTRED_EX",
        "Fore.LIGHTGREEN_EX",
        "Fore.LIGHTYELLOW_EX",
        "Fore.LIGHTBLUE_EX",
        "Fore.LIGHTMAGENTA_EX",
        "Fore.LIGHTCYAN_EX",
        "Fore.LIGHTWHITE_EX"
    ]


class Colour:
    back_arr = [
        # Warna Tua
        # Back.BLACK,
        Back.RED,
        Back.GREEN,
        Back.YELLOW,
        Back.BLUE,
        Back.MAGENTA,
        Back.CYAN,
        Back.WHITE,
        # Back.RESET,

        # Warna Muda
        Back.LIGHTBLACK_EX,
        Back.LIGHTRED_EX,
        Back.LIGHTGREEN_EX,
        Back.LIGHTYELLOW_EX,
        Back.LIGHTBLUE_EX,
        Back.LIGHTMAGENTA_EX,
        Back.LIGHTCYAN_EX,
        Back.LIGHTWHITE_EX
    ]

    fore_arr = [
        # Warna Tua
        # Fore.BLACK,
        Fore.RED,
        Fore.GREEN,
        Fore.YELLOW,
        Fore.BLUE,
        Fore.MAGENTA,
        Fore.CYAN,
        Fore.WHITE,
        # Fore.RESET,

        # Warna Muda
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTRED_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTYELLOW_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTWHITE_EX
    ]

color = Colour()
string = Text()

import io
def clr(file):
    with io.open(file, "w") as fl:
        fl.truncate(0)