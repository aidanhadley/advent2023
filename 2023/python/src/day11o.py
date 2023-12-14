import time


def make_graph(lines):
    graph = []
    for line in lines:
        row = []
        for item in line:
            if item != "\n":
                row.append(item)
        graph.append(row)
    return graph

def find_empties(graph):
    # taking this method from nia lol
    # horizontal first el oh el
    ys = []
    for y, line in enumerate(graph):
        if len(set(line)) == 1:
            ys.append(y)
    # vertical next
    xs = []
    for x in range(len(graph[0])):
        check = []
        for line in graph:
            check.append(line[x])
        # we made a vertical line! check it
        if len(set(check)) == 1:
            xs.append(x)
    return [xs, ys]

def find_coords(graph):
    # just like the other
    result = []
    for y, line in enumerate(graph):
        for x, item in enumerate(line):
            if  item == '#':
                # it's a galaxy
                result.append((x, y))
    return result

def expand(point, exs, n=1):
    # point is a single point
    # exs is the empty lines to expand
    # n is expansion factor
    x, y = point
    nx = x
    ny = y
    xs = exs[0]
    ys = exs[1]
    # appy the x expansion factor
    for i in xs:
        if x > i: # meaning the point is beyond the empty space
            nx += n
    for i in ys:
        if y > i:
            ny += n
    return (nx, ny)

def compute(lines, n=1):
    # n is the expansion factor(1 for pt 1, 999,999 for part 2 lol)
    graph = make_graph(lines)
    empties = find_empties(graph)
    coords = find_coords(graph)
    sumber = 0
    nps = []
    for point in coords:
        nps.append(expand(point, empties, n))
    # time to actually calculate
    for i in range(len(nps)):
        for j in range(i + 1, len(nps)):
            d = abs(nps[j][0] - nps[i][0]) + abs(nps[j][1] - nps[i][1])
            sumber += d
    print(f"The sum of all of the shortest distances is {sumber}")


def main():
    file = open("11/input.txt", "r", encoding="utf8")
    lines = file.readlines()
    start_time = time.time()
    # p1
    compute(lines, 1)
    # p2
    compute(lines, 1000000 - 1)
    print(f"This program completed in {time.time() - start_time}")


if __name__ == "__main__":
    main()
