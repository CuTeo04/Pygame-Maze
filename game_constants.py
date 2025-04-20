# game_constants.py
import random_map_dfs as rand_map

# Các bản đồ mặc định
map_easy = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X       XX  XXXXXX  XXXX     XX    XXXX",
    "X      XX  XXX        XX  XX XX     XXX",
    "XXXXXX  XX  XXX                 XXX  XX",
    "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   X",
    "XXXXXX  XX    XXXX  XXXXX        XX  XX",
    "X  XXX        XXXX  XXXXXXXXXX   XXXXXX",
    "X  XXX  XXXXXXXXX          XXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XE               XXXXXXXX  XXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX  X    XXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXX",
    "XXX  XXXXXXXXXX         XXX  XXXX    XX",
    "XXX                     XXXXXXX    XXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XX   XXXXX              XXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX  XXXXX",
    "XX    XXXXXXXXXXXX  X      XXXXX    XXX",
    "XX     E   XXXX        XX     XXXX  XXX",
    "XXXX               TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX        XXXX        HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_medium = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP  XXXXXXXE         XXXXXX      XXXXXX",
    "X  XXXXXXX  XXXXXX  XXXXXXX  XX  XXXXXX",
    "X      TXX  XXXXXX  XXXX     XX   TXXXX",
    "X E    XX  XXX       EXX  XX XX     XXX",
    "XXXXXX  XX  XXX              E  XXX  XX",
    "XXXXXX  XX  XXXXXX  XXXXX     XXXXX   X",
    "XXXXXX  XX    XXXX  XXXXX        XX  XX",
    "X  XXX        XXXX  XXXXXXXXXX   XXXXXX",
    "X  XXX  XXXXXXXXX   E      XXXX  XXXXXX",
    "X         XXXXXXXXXXXXXXX  XXXX  XXXXXX",
    "XE               XXXXXXXX  XXXX    XXXX",
    "XXXXXXXXXXXX     XXXXX TX    XXXX  XXXX",
    "XXXXXXXXXXXXXXX  XXXXX  XXX  XXXX  XXXX",
    "XXX TXXXXXXXXXX         XXX  XXXX   TXX",
    "XXXE                    XXXXXXX   EXXXX",
    "XXX        TXXXXXXXXXXXXXXXXXXX  XXXXXX",
    "XXXXXXXXXX  XXXXXXXXXXXXXXX      XXXXXX",
    "XXXXXXXXXXE             XXXXX     XXXXX",
    "XXE  XXXXX             EXXXXXXXX  XXXXX",
    "XX   XXXXXXXXXXXXX  XXXXXXXXXXXX EXXXXX",
    "XX    XXXXXXXXXXXX  X      XXXXX    XXX",
    "XX     E   XXXX        XX     XXXX  XXX",
    "XXXXT              TXXXXXXXX  XXXX  XXX",
    "XXXXXXXXXXXXXXXX       TXXXX    E   HXX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

map_hard = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP     XT   X     X X  XT       XT    X",
    "X X XX     EX X X X XX         EX XXXXX",
    "X X XXXXXXX X XXX X  X XXXXXXXX X    EX",
    "X XXXE    X X   X XX X X        XXXXX X",
    "X X   X X X XXX X    X XXXXXXXX X     X",
    "X X XXXXX X     XXXXXX  X       X XXXXX",
    "X X XE TX XXXXXXX       X XXXXXXX X   X",
    "X X X X X       X X X XXX       X X X X",
    "X X X X XXXXXXX X X X XXXXXXXXX X X X X",
    "X X X X X   X X X X X X         X X X X",
    "X X X X       X   X   X XXXXX XXX   X X",
    "X X X XXXXXXXXXXXXX XXX X X XXX XXXXX X",
    "XT  X    X             EX             X",
    "XXXXXXXX X XXXXXXXXXT   X X X XXXXX XXX",
    "X        X         XXXXXXXX XXXT  XXX X",
    "XXXXXXXX X XXXXXXX X     EXE          X",
    "X        X       X X X XX XXXXXXXXXXX X",
    "X X XXX XXXXXXXX X X X X          X X X",
    "X X XTX X      X X X X X X  TXXXX X X X",
    "X X    EX X XX X X X XXXXXXXXX    X X X",
    "X XXXXXXX X X  X XXX X       X XXXX X X",
    "X X     X XXXX X     X X X X X        X",
    "X X X X X XT   XXXXXXX X T X XXXXXXXX X",
    "X   X X   XXXX        EXXXXX         HX",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
]

# Hàm lấy bản đồ ngẫu nhiên
def get_random_map(level_type):
    return rand_map.generate_map(level_type)

# Biến kiểm soát: True để sử dụng bản đồ ngẫu nhiên, False để sử dụng bản đồ cố định
use_random_maps = True

def show_main_menu():
    # Được định nghĩa trong main.py
    pass