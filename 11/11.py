import time


def make_graph(lines):
    graph = []
    for y, line in enumerate(lines):
        row = []
        for x, item in enumerate(line):
            if item != "\n":
                row.append(item)
        graph.append(row)
    return graph


def expand_graph(graph, n=1):
    # ok attempt 2 at this: vertical first
    # starting from reverse order, as to not fuck anything up
    # check the last one to the first one
    for i in range(len(graph[0]) - 1, -1, -1):
        # the line to check
        l = []
        for line in graph:
            l.append(line[i])
        # now the line to check is filly equipped
        # check with the set method
        if len(set(l)) == 1:
            # debug

            for line in graph:
                # make a list of the proper size
                l = n * ["."]
                # add them at the proper location
                line[i:i] = l
    # horizontal
    # backwards again
    # make an insertable row
    row = []
    row += len(graph[0]) * ["."]
    for i in range(len(graph) - 1, -1, -1):
        if len(set(graph[i])) == 1:
            rows = []
            for j in range(n):
                rows.append(row)
            graph[i:i] = rows
    return graph


def find_coords(graph, n=1):
    coords = []
    # we taking over the for loop bitch !!
    y = 0
    while y < len(graph):
        row = graph[y]

        # if it's empty skip the bitch!!!
        if len(set(row)) == 1:
            y += n + 1
            continue

        for x, item in enumerate(row):
            if item == "#":
                coords.append((x, y))

        y += 1

    return coords


def compute(lines, n=1):
    small = make_graph(lines)
    graph = expand_graph(small, n)
    coords = find_coords(small, n)
    sum = 0
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            d = abs(coords[j][0] - coords[i][0]) + abs(coords[j][1] - coords[i][1])
            sum += d
    print(f"The sum of all of the shortest distances is {sum}")

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
