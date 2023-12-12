import sys

sys.setrecursionlimit(100000)


class Pipe:
    # a pipe has these qualities:
    # 1. the location x, y
    # 2. what direction it can lead (left right up down)
    def __init__(self, x, y):
        # part one
        self.coords = [x, y]
        self.x = x
        self.y = y
        # part two
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.visited = False

    def is_connected(self, other):
        ox = other.x
        oy = other.y
        x = self.x
        y = self.y
        # left case :
        if x - ox == 1 and y - oy == 0 and self.left is True and other.right is True:
            return True
        # right case:
        if x - ox == -1 and y - oy == 0 and self.right is True and other.left is True:
            return True
        # up case:
        if x - ox == 0 and y - oy == 1 and self.up is True and other.down is True:
            return True
        # down case
        if x - ox == 0 and y - oy == -1 and self.down is True and other.up is True:
            return True
        # this excludes all other cases
        return False
    
    def is_visited(self):
        return self.visited
    
    def visit(self):
        self.visited = True

    def __str__(self):
        return "."


class vPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.up = True
        self.down = True

    def __str__(self):
        return "|"


class hPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left = True
        self.right = True

    def __str__(self):
        return "-"


class LPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.up = True
        self.right = True

    def __str__(self):
        return "L"


class JPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.up = True
        self.left = True

    def __str__(self):
        return "J"


class SPipe(Pipe):
    # 7pipe
    def __init__(self, x, y):
        super().__init__(x, y)
        self.left = True
        self.down = True

    def __str__(self):
        return "7"


class FPipe(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.right = True
        self.down = True

    def __str__(self):
        return "F"

class startP(Pipe):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.up = True
        self.down = True
        self.right = True
        self.left = True
    
    def __str__(self):
        return "S"
def make_pipes(lines):
    # this returns a 2d array of the graph and
    # an array of the coordianates of the start position (x, y)
    pipe_classes = {
        "|": vPipe,
        "-": hPipe,
        "L": LPipe,
        "J": JPipe,
        "7": SPipe,
        "F": FPipe,
        ".": Pipe,
        "S": startP,
    }
    graph = []
    start = None
    for y, line in enumerate(lines):
        row = []
        for x, char in enumerate(line):
            if char == "\n":
                continue
            item = pipe_classes.get(char)
            row.append(item(x, y))
            if char == "S":
                start = item(x, y)
        graph.append(row)
    return graph, start


def print_pipes(graph):
    for row in graph:
        for item in row:
            print(item, end="")
        print()

def path_find(graph, pipe, distance, direction):
    x, y = pipe.x, pipe.y
    pipe.visit()
    graph[y][x].visit()

    # Establish next move
    dirs = {
        "left": (0, -1),
        "right": (0, 1),
        "up": (-1, 0),
        "down": (1, 0)
    }
    dy, dx = dirs.get(direction)
    new_x, new_y = x + dx, y + dy
    # test = graph[22][91]
    # Check if the move is within bounds
    if 0 <= new_x < len(graph[0]) and 0 <= new_y < len(graph):
        neighbor = graph[new_y][new_x]
        isOpen = not neighbor.is_visited()
        # Check if the neighbor is a valid pipe and hasn't been visited
        if isOpen and pipe.is_connected(neighbor):
            # print(pipe, direction, distance, end=" ")
            # Recursively explore the neighbor with an increased distance
            max_distance = max(
                path_find(graph, neighbor, distance + 1, "left"),
                path_find(graph, neighbor, distance + 1, "right"),
                path_find(graph, neighbor, distance + 1, "up"),
                path_find(graph, neighbor, distance + 1, "down")
            )
        else:
            max_distance = distance
    else:
        max_distance = distance

    # Reset the visited status after exploring neighbors (backtrack)
    # visited[y][x] = False

    return max_distance

def part1(lines):
    graph, start = make_pipes(lines)
    # start_x, start_y = start.x, start.y
    # Make visited array
    # visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
    # Set max_distance to -1 initially
    max_distance = 1
    # Find the farthest point starting from the specified position
    # max_distance = max (
    r = path_find(graph, start, max_distance, "right")
    # print()
    l = path_find(graph, start, max_distance, "left")
    # print()
    u = path_find(graph, start, max_distance, "up")
    # print()
    d = path_find(graph, start, max_distance, "down")
    # print()
    # )
    max_distance = max( r, l, u, d)
    
    print(f"The farthest point from the starting position is at distance {max_distance/2}.")


def main():
    file = open("10/input.txt", "r", encoding="utf8")
    lines = file.readlines()
    # graph , coords = make_pipes(lines)
    # print_pipes(graph)
    # print(coords)
    part1(lines)


if __name__ == "__main__":
    main()
