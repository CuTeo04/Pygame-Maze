import turtle
import math
import random
from game_constants import *
import astar

def init_game(name_level, map_level):
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("A Maze Game")
    screen.setup(1000, 750)
    screen.tracer(0)

    # Đường dẫn đến thư mục assets
    wall_easy = "assets/wall_easy.gif"
    wall_medium = "assets/wall_medium.gif"
    wall_hard = "assets/wall_hard.gif"
    image_princess = "assets/princess.gif"
    image_logo_teky = "assets/logo_teky.gif"
    left = "assets/left.gif"
    right = "assets/right.gif"
    top = "assets/top.gif"
    bottom = "assets/bottom.gif"
    find_path_button = "assets/find_path.gif"
    image_monsters = ["assets/monster_0.gif", "assets/monster_1.gif", "assets/monster_2.gif", "assets/monster_3.gif", "assets/monster_4.gif"]
    image_treasures = ["assets/treasure_0.gif", "assets/treasure_1.gif", "assets/treasure_2.gif", "assets/treasure_3.gif", "assets/treasure_4.gif"]

    # Đăng ký các hình ảnh
    screen.addshape(wall_easy)
    screen.addshape(wall_medium)
    screen.addshape(wall_hard)
    screen.addshape(image_princess)
    screen.addshape(image_logo_teky)
    screen.addshape(left)
    screen.addshape(right)
    screen.addshape(top)
    screen.addshape(bottom)
    screen.addshape(find_path_button)
    for monster in image_monsters:
        screen.addshape(monster)
    for treasure in image_treasures:
        screen.addshape(treasure)
    
    # create list
    walls = []
    treasures = []
    monsters = []
    path_dots = []  # Danh sách các điểm đánh dấu đường đi
    princess_position = None  # Vị trí của công chúa

    #show hp
    def show_hp(hp):
        turtle.clear()
        turtle.color('white')
        turtle.penup()
        turtle.goto(380, 305)
        style = ('Courier', 20, 'bold')
        turtle.write("HP: {0}".format(hp), font=style, align='center')
        turtle.hideturtle()

    #create logo teky
    class LogoTeky(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(image_logo_teky)
            self.penup()
            self.goto(-420, 330)
            self.onclick(self.main)

        def main(self, x, y):
            turtle.clearscreen()
            from game_constants import show_main_menu
            show_main_menu()
            turtle.done()

    # Thêm lớp nút tìm đường
    class FindPathButton(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(find_path_button)
            self.penup()
            self.goto(-330, 330)
            self.onclick(self.find_path)
        
        def find_path(self, x, y):
            # Xóa đường đi cũ nếu có
            clear_path()
            
            # Lấy vị trí hiện tại của người chơi
            start_pos = (player.xcor(), player.ycor())
            
            # Kiểm tra xem còn kho báu không
            if treasures:
                # Nếu còn kho báu, tìm kho báu gần nhất
                nearest_treasure = None
                min_distance = float('inf')
                
                for treasure in treasures:
                    end_pos = (treasure.xcor(), treasure.ycor())
                    # Tính khoảng cách Manhattan
                    distance = abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
                    if distance < min_distance:
                        min_distance = distance
                        nearest_treasure = treasure
                
                if nearest_treasure:
                    end_pos = (nearest_treasure.xcor(), nearest_treasure.ycor())
                    path = astar.astar(map_level, start_pos, end_pos, walls)
                    if path:
                        # Hiển thị đường đi đến kho báu gần nhất
                        show_path(path)
                        return
            
            # Nếu không còn kho báu hoặc không tìm được đường đến kho báu nào,
            # tìm đường đến công chúa
            if princess_position:
                path = astar.astar(map_level, start_pos, princess_position, walls)
                if path:
                    # Hiển thị đường đi đến công chúa
                    show_path(path)
                    return

    # Hàm để hiển thị đường đi
    def show_path(path):
        for pos in path[1:]:  # Bỏ qua vị trí đầu tiên (vị trí hiện tại của người chơi)
            dot = turtle.Turtle()
            dot.shape("circle")
            dot.color("yellow")
            dot.shapesize(0.3)
            dot.penup()
            dot.goto(pos)
            path_dots.append(dot)

    # Hàm để xóa đường đi
    def clear_path():
        for dot in path_dots:
            dot.hideturtle()
            dot.clear()
        path_dots.clear()

    #create pen
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            if name_level == "easy":
                self.shape(wall_easy)
            elif name_level == "medium":
                self.shape(wall_medium)
            else:
                self.shape(wall_hard)
            self.penup()
            self.speed(0)

    #create player
    class Player(turtle.Turtle):
        
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(bottom)
            self.penup()
            self.speed(0)
            self.hp = 500
            show_hp(self.hp)

        def up(self):
            self.shape(top)
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 24
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
                # Xóa đường đi khi người chơi di chuyển
                clear_path()

        def down(self):
            self.shape(bottom)
            move_to_x = self.xcor()
            move_to_y = self.ycor() - 24
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
                # Xóa đường đi khi người chơi di chuyển
                clear_path()

        def left(self):
            self.shape(left)
            move_to_x = self.xcor() - 24
            move_to_y = self.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
                # Xóa đường đi khi người chơi di chuyển
                clear_path()

        def right(self):
            self.shape(right)
            move_to_x = self.xcor() + 24
            move_to_y = self.ycor()
            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
                # Xóa đường đi khi người chơi di chuyển
                clear_path()

        def is_collision(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))
            if distance < 5:
                return True
            else:
                return False

        # Thêm hàm tự động di chuyển theo đường đi
        def follow_path(self, path):
            if not path or len(path) <= 1:
                return
            
            # Xóa đường đi hiện tại
            clear_path()
            
            # Hiển thị đường đi mới
            show_path(path)
            
            # Di chuyển người chơi theo đường đi
            next_pos = path[1]  # Vị trí tiếp theo trong đường đi
            current_pos = (self.xcor(), self.ycor())
            
            # Xác định hướng di chuyển
            if next_pos[0] > current_pos[0]:
                self.right()
            elif next_pos[0] < current_pos[0]:
                self.left()
            elif next_pos[1] > current_pos[1]:
                self.up()
            elif next_pos[1] < current_pos[1]:
                self.down()
            
            # Lập lịch cho bước di chuyển tiếp theo
            if len(path) > 2:
                turtle.ontimer(lambda: self.follow_path(path[1:]), 300)

    #create treasure
    class Treasure(turtle.Turtle):
        
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            if name_level == "easy":
                self.number_random = random.randint(0, 1)
            elif name_level == "medium":
                self.number_random = random.randint(0, 2)
            else:
                self.number_random = random.randint(3, 4)
            self.shape(image_treasures[self.number_random])
            self.hp = (self.number_random + 1) * 100
            self.penup()
            self.speed(0)
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    #create princess
    class Princess(turtle.Turtle):
        
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape(image_princess)
            self.penup()
            self.speed(0)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    #class monster
    class Monster(turtle.Turtle):
        
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            if name_level == "easy":
                self.number_random = random.randint(0, 1)
            elif name_level == "medium":
                self.number_random = random.randint(0, 2)
            else:
                self.number_random = random.randint(3, 4)
            self.shape(image_monsters[self.number_random])
            self.hp = -(self.number_random + 1) * 100
            self.penup()
            self.speed(0)
            self.gold = -25
            self.goto(x, y)
            self.direction = random.choice(["up", "down", "left", "right"])

        def move(self):
            if self.direction == "up":
                x = 0
                y = 24
            elif self.direction == "down":
                x = 0
                y = -24
            elif self.direction == "left":
                x = -24
                y = 0
            elif self.direction == "right":
                x = 24
                y = 0
            move_to_x = self.xcor() + x
            move_to_y = self.ycor() + y

            if (move_to_x, move_to_y) not in walls:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(["up", "down", "left", "right"])
            turtle.ontimer(self.move, t = random.randint(100, 300))

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    #setup level
    def setup_maze(level):
        nonlocal princess_position
        for y in range(len(level)):
            for x in range(len(level[y])):
                character = level[y][x]
                position_x = -456 + (x * 24)
                position_y = 288 - (y * 24)
                if character == "X":
                    pen.goto(position_x, position_y)
                    pen.stamp()
                    walls.append((position_x, position_y))
                elif character == "P":
                    player.goto(position_x, position_y)
                elif character == "T":
                    treasures.append(Treasure(position_x, position_y))
                elif character == "E":
                    monsters.append(Monster(position_x, position_y))
                elif character == "H":
                    princess.goto(position_x, position_y)
                    princess_position = (position_x, position_y)
                    princess.stamp()

    #create instance
    pen = Pen()
    player = Player()
    princess = Princess()
    logo_teky = LogoTeky()
    find_path_button = FindPathButton()  # Thêm nút tìm đường

    #keyboard bindding
    turtle.listen()
    turtle.onkey(player.up, "Up")
    turtle.onkey(player.down, "Down")
    turtle.onkey(player.right, "Right")
    turtle.onkey(player.left, "Left")
    # Thêm phím tắt để tự động tìm đường
    turtle.onkey(lambda: find_path_button.find_path(0, 0), "f")
    # Thêm phím tắt để tự động di chuyển theo đường đi
    turtle.onkey(lambda: player.follow_path(astar.astar(map_level, (player.xcor(), player.ycor()), princess_position, walls)), "a")

    #set up level
    setup_maze(map_level)

    #run monster
    for monster in monsters:
        turtle.ontimer(monster.move, 250)

    while True:
        for treasure in treasures:
            if player.is_collision(treasure):
                player.hp += treasure.hp
                show_hp(player.hp)
                treasure.destroy()
                treasures.remove(treasure)
        for monster in monsters:
            if player.is_collision(monster):
                player.hp += monster.hp
                show_hp(player.hp)
                monster.destroy()
                monsters.remove(monster)
                if player.hp <= 0:
                    turtle.clearscreen()
                    turtle.color('red')
                    turtle.penup()
                    turtle.goto(0, -45)
                    style = ('Courier', 24, 'italic')
                    turtle.write('You died! Play again', font=style, align='center')
                    turtle.hideturtle()
                    from game_constants import show_main_menu
                    show_main_menu()
                    turtle.done()
                    break
        if player.is_collision(princess) and len(treasures) == 0:
            turtle.clearscreen()
            turtle.color('blue')
            turtle.penup()
            turtle.goto(0, -45)
            style = ('Courier', 24, 'italic')
            turtle.write('You are winner!', font=style, align='center')
            turtle.hideturtle()
            from game_constants import show_main_menu
            show_main_menu()
            turtle.done()
            break
        screen.update()