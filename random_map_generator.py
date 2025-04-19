import random

def generate_random_maze_dfs(width, height, difficulty):
    """
    Tạo mê cung ngẫu nhiên sử dụng thuật toán DFS
    :param width: Chiều rộng mê cung (số ô)
    :param height: Chiều cao mê cung (số ô)
    :param difficulty: Độ khó ("easy", "medium", "hard")
    :return: Mê cung dưới dạng mảng chuỗi
    """
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    maze = [['X' for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y):
        maze[y][x] = ' '
        directions = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 'X':
                maze[y + dy // 2][x + dx // 2] = ' '
                carve_passages(nx, ny)

    start_x = random.randrange(1, width - 1, 2)
    start_y = random.randrange(1, height - 1, 2)
    carve_passages(start_x, start_y)

    empty_cells = [(x, y) for y in range(height) for x in range(width) if maze[y][x] == ' ']

    # Đặt người chơi (P)
    for y in range(1, height):
        for x in range(1, width):
            if (x, y) in empty_cells:
                maze[y][x] = 'P'
                empty_cells.remove((x, y))
                break
        if 'P' in ''.join([''.join(row) for row in maze]):
            break

    # Đặt công chúa (H)
    for y in range(height - 1, 0, -1):
        for x in range(width - 1, 0, -1):
            if (x, y) in empty_cells:
                maze[y][x] = 'H'
                empty_cells.remove((x, y))
                break
        if 'H' in ''.join([''.join(row) for row in maze]):
            break

    # Xác định số lượng quái vật và kho báu theo độ khó
    if difficulty == "easy":
        num_monsters = max(3, width * height // 100)
        num_treasures = max(3, width * height // 100)
    elif difficulty == "medium":
        num_monsters = max(5, width * height // 90)
        num_treasures = max(5, width * height // 90)
    else:  # hard
        num_monsters = max(7, width * height // 90)
        num_treasures = max(7, width * height // 90)

    # Hàm kiểm tra vị trí có đủ khoảng trống xung quanh cho quái vật
    def is_safe_for_monster(x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == ' ':
                count += 1
        return count >= 2

    # Đặt quái vật
    monster_count = 0
    safe_cells = [pos for pos in empty_cells if is_safe_for_monster(*pos)]
    while monster_count < num_monsters and safe_cells:
        pos = random.choice(safe_cells)
        x, y = pos
        maze[y][x] = 'E'
        empty_cells.remove(pos)
        safe_cells.remove(pos)
        monster_count += 1

    # Đặt kho báu
    treasure_count = 0
    while treasure_count < num_treasures and empty_cells:
        pos = random.choice(empty_cells)
        x, y = pos
        maze[y][x] = 'T'
        empty_cells.remove(pos)
        treasure_count += 1
        
         # Đục thêm lỗ gần quái vật để dễ né
    def dig_near_monsters(extra_digs=3):
        for y in range(height):
            for x in range(width):
                if maze[y][x] == 'E':
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    random.shuffle(directions)
                    dug = 0
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 'X':
                            maze[ny][nx] = ' '
                            dug += 1
                        if dug >= extra_digs:
                            break

    # Đục thêm lỗ tùy theo độ khó
    if difficulty == "easy":
        dig_near_monsters(extra_digs=5)
    elif difficulty == "medium":
        dig_near_monsters(extra_digs=4)
    else:  # hard
        dig_near_monsters(extra_digs=4)

    

    # Trả về danh sách chuỗi
    maze_strings = [''.join(row) for row in maze]
    return maze_strings

def generate_map(level_type):
    """
    Tạo bản đồ ngẫu nhiên dựa vào cấp độ
    :param level_type: Loại cấp độ ("easy", "medium", "hard")
    :return: Mê cung dưới dạng mảng chuỗi
    """
    if level_type == "easy":
        width = 15
        height = 20
    elif level_type == "medium":
        width = 20
        height = 25
    else:  # hard
        width = 25
        height = 30

    return generate_random_maze_dfs(width, height, level_type)
