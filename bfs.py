from collections import deque

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Tọa độ (x, y)
        self.parent = parent      # Node cha
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)

def bfs(maze, start, end, walls):
    """
    Thuật toán BFS để tìm đường đi
    :param maze: Ma trận mê cung
    :param start: Tọa độ điểm bắt đầu (x, y)
    :param end: Tọa độ điểm kết thúc (x, y)
    :param walls: Danh sách các tọa độ tường
    :return: Danh sách các tọa độ đường đi hoặc None nếu không tìm thấy
    """
    # Kiểm tra điểm bắt đầu và kết thúc có phải tường không
    if start in walls or end in walls:
        return None

    # Khởi tạo node bắt đầu 
    start_node = Node(start)
    
    # Hàng đợi BFS
    queue = deque([start_node])
    
    # Danh sách các điểm đã đi qua
    visited = set([start])
    
    # Các bước di chuyển có thể (lên, xuống, trái, phải)
    moves = [(0, 24), (0, -24), (-24, 0), (24, 0)]
    
    # Lặp cho đến khi hàng đợi trống
    while queue:
        # Lấy node đầu tiên từ hàng đợi
        current_node = queue.popleft()
        
        # Nếu đã đến đích, xây dựng đường đi và trả về
        if current_node.position == end:
            path = []
            current = current_node
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]  # Đảo ngược để có đường đi từ điểm bắt đầu
        
        # Kiểm tra các node kề
        for move in moves:
            # Tính tọa độ node mới
            new_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            # Kiểm tra xem node mới có hợp lệ không
            if new_position in walls:  # Node là tường
                continue
                
            if new_position in visited:  # Node đã được xử lý
                continue
            
            # Đánh dấu node mới đã thăm
            visited.add(new_position)
            
            # Tạo node mới và thêm vào hàng đợi
            new_node = Node(new_position, current_node)
            queue.append(new_node)
    
    # Không tìm thấy đường đi
    return None

def preload_paths(maze, walls, treasures_positions, princess_position):
    """
    Tải trước tất cả đường đi từ mỗi kho báu và công chúa đến tất cả các vị trí có thể đi được
    :param maze: Ma trận mê cung
    :param walls: Danh sách các tọa độ tường
    :param treasures_positions: Danh sách vị trí của các kho báu
    :param princess_position: Vị trí của công chúa
    :return: Dictionary chứa đường đi từ mỗi nguồn đến tất cả các điểm
    """
    all_paths = {}
    # Tạo danh sách các điểm nguồn (kho báu và công chúa)
    source_points = treasures_positions.copy()
    if princess_position:
        source_points.append(princess_position)
    
    # Tạo một tập hợp các điểm đích (tất cả các điểm không phải là tường)
    # Đầu tiên, xác định kích thước của bản đồ
    min_x, max_x, min_y, max_y = float('inf'), float('-inf'), float('inf'), float('-inf')
    for x, y in walls:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # Tạo danh sách các điểm có thể đi được
    walkable_points = []
    step_size = 24  # Kích thước bước di chuyển
    for x in range(int(min_x), int(max_x) + step_size, step_size):
        for y in range(int(min_y), int(max_y) + step_size, step_size):
            if (x, y) not in walls:
                walkable_points.append((x, y))
    
    # Tính toán đường đi từ mỗi điểm nguồn đến tất cả các điểm có thể đi được
    for source in source_points:
        all_paths[source] = {}
        for target in walkable_points:
            if source != target:  # Không tính đường đi đến chính nó
                path = bfs(maze, source, target, walls)
                if path:  # Nếu có đường đi
                    all_paths[source][target] = path
    
    return all_paths