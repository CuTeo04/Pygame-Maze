import heapq
import math

class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Tọa độ (x, y)
        self.parent = parent      # Node cha
        
        self.g = 0  # Chi phí từ điểm bắt đầu đến node hiện tại
        self.h = 0  # Chi phí ước tính từ node hiện tại đến đích (heuristic)
        self.f = 0  # Tổng chi phí (g + h)
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.position)

def astar(maze, start, end, walls):
    """
    Thuật toán A* để tìm đường đi ngắn nhất
    :param maze: Ma trận mê cung
    :param start: Tọa độ điểm bắt đầu (x, y)
    :param end: Tọa độ điểm kết thúc (x, y)
    :param walls: Danh sách các tọa độ tường
    :return: Danh sách các tọa độ đường đi hoặc None nếu không tìm thấy
    """
    # Khởi tạo node bắt đầu và node kết thúc
    start_node = Node(start)
    end_node = Node(end)
    
    # Danh sách mở và danh sách đóng
    open_list = []
    closed_list = set()
    
    # Thêm node bắt đầu vào danh sách mở
    heapq.heappush(open_list, start_node)
    
    # Các bước di chuyển có thể (lên, xuống, trái, phải)
    moves = [(0, 24), (0, -24), (-24, 0), (24, 0)]
    
    # Lặp cho đến khi danh sách mở trống
    while open_list:
        # Lấy node có f nhỏ nhất từ danh sách mở
        current_node = heapq.heappop(open_list)
        
        # Thêm vào danh sách đóng
        closed_list.add(current_node.position)
        
        # Nếu đã đến đích, xây dựng đường đi và trả về
        if current_node.position == end_node.position:
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
                
            if new_position in closed_list:  # Node đã được xử lý
                continue
            
            # Tạo node mới
            new_node = Node(new_position, current_node)
            
            # Tính toán g, h, f
            new_node.g = current_node.g + 1
            # Sử dụng khoảng cách Manhattan làm heuristic
            new_node.h = abs(new_node.position[0] - end_node.position[0]) + abs(new_node.position[1] - end_node.position[1])
            new_node.f = new_node.g + new_node.h
            
            # Kiểm tra xem node có trong danh sách mở không
            for open_node in open_list:
                if new_node == open_node and new_node.g > open_node.g:
                    continue
            
            # Thêm node mới vào danh sách mở
            heapq.heappush(open_list, new_node)
    
    # Không tìm thấy đường đi
    return None
