import turtle
import game_easy
import game_constants 


# Cập nhật hàm main() trong file main.py
def main():
    screen = turtle.Screen()
    screen.tracer(0)

    # Đường dẫn đầy đủ đến các hình ảnh trong thư mục assets
    easy = "assets/easy.gif"
    medium = "assets/medium.gif"
    hard = "assets/hard.gif"
    introduction = "assets/introduction.png"
    random_map_button = "assets/random_map.gif"  # Thêm hình ảnh cho nút bản đồ ngẫu nhiên

    # Đăng ký các hình ảnh
    screen.addshape(easy)
    screen.addshape(medium)
    screen.addshape(hard)
    screen.addshape(random_map_button)  # Đăng ký hình ảnh mới

    # Tạo tiêu đề "Maze Game" ở trên cùng
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.goto(0, 300)
    title_turtle.color("white")
    title_turtle.write("Maze Game", align="center", font=("Arial", 24, "bold"))

    # Tạo nút bản đồ ngẫu nhiên
    class RandomMapToggle(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(random_map_button)
            self.penup()
            self.goto(0, -250)  # Đặt cao hơn một chút (từ -270 lên -250)
            self.onclick(self.toggle_random_map)

        def toggle_random_map(self, x, y):
            # Đảo ngược trạng thái hiện tại
            game_constants.use_random_maps = not game_constants.use_random_maps
            status = "BẬT" if game_constants.use_random_maps else "TẮT"
            
            # Hiển thị trạng thái hiện tại
            status_turtle.clear()
            status_turtle.write(f"Bản đồ ngẫu nhiên: {status}", align="center", font=("Arial", 14, "bold"))

    # Create status turtle for displaying random map status
    status_turtle = turtle.Turtle()
    status_turtle.hideturtle()
    status_turtle.penup()
    status_turtle.goto(0, -320)
    status_turtle.color("white")
    status_turtle.write(f"Bản đồ ngẫu nhiên: BẬT", align="center", font=("Arial", 14, "bold"))

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
                if game_constants.use_random_maps:
                    random_map = game_constants.get_random_map("easy")
                    game_easy.init_game("easy", random_map)
                else:
                    game_easy.init_game("easy", game_constants.map_easy)
            elif self.level == medium:
                turtle.clearscreen()
                if game_constants.use_random_maps:
                    random_map = game_constants.get_random_map("medium")
                    game_easy.init_game("medium", random_map)
                else:
                    game_easy.init_game("medium", game_constants.map_medium)
            elif self.level == hard:
                turtle.clearscreen()
                if game_constants.use_random_maps:
                    random_map = game_constants.get_random_map("hard")
                    game_easy.init_game("hard", random_map)
                else:
                    game_easy.init_game("hard", game_constants.map_hard)

    # add level
    level_easy = Level(easy, 100)  # Căn chỉnh vị trí nút easy
    level_medium = Level(medium, 50)  # Căn chỉnh vị trí nút medium
    level_hard = Level(hard, 0)  # Căn chỉnh vị trí nút hard
    random_map_toggle = RandomMapToggle()  # Thêm nút bản đồ ngẫu nhiên

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