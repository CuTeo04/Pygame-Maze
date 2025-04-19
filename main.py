import turtle
import time
import game_easy
import game_constants  # Thay vì import *

# Cập nhật hàm main() trong file constants
def main():
    screen = turtle.Screen()
    screen.tracer(0)

    # Đường dẫn đầy đủ đến các hình ảnh trong thư mục assets
    easy = "assets/easy.gif"
    medium = "assets/medium.gif"
    hard = "assets/hard.gif"
    introduction = "assets/introduction.png"

    # Đăng ký các hình ảnh
    screen.addshape(easy)
    screen.addshape(medium)
    screen.addshape(hard)

    # create level
    class Level(turtle.Turtle):

        level = ""

        def __init__(self, level, position_y):
            turtle.Turtle.__init__(self)
            self.shape(level)
            self.penup()
            self.goto(0, position_y)
            self.level = level
            self.onclick(self.play_game)

        def play_game(self, x, y):
            if self.level == easy:
                turtle.clearscreen()
                game_easy.init_game("easy", game_constants.map_easy)
            elif self.level == medium:
                turtle.clearscreen()
                game_easy.init_game("medium", game_constants.map_medium)
            elif self.level == hard:
                turtle.clearscreen()
                game_easy.init_game("hard", game_constants.map_hard)

    # add level
    level_easy = Level(easy, -120)
    level_medium = Level(medium, -170)
    level_hard = Level(hard, -220)

    # Cài đặt hình nền và các thuộc tính màn hình
    screen.bgpic(introduction)
    screen.title("Maze Game")
    screen.setup(1000, 740)
    screen.update()
    screen.mainloop()

# Cập nhật hàm show_main_menu trong file constants
game_constants.show_main_menu = main

if __name__ == "__main__":
    main()