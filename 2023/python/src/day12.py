import time
def find_spots(string):
    # takes in a string, returns an array
    # for example:
    # ?????...#?? will produce
    # [5, ., #, 2] and
    # ???.?##.?? will produce
    # [3, ., 1, #, #, ., 2]
    result = []
    for char in string:
        # ? case:
        if char == '?':
            # check to see if there are ?s behind
            if result and str(result[len(result) - 1]).isdigit():
                result[len(result) - 1] += 1
            else:
                # make a new one
                result.append(1)
        # . case
        if char == '.':
            # is there's one already there, don't bother
            if result and result[len(result) - 1] != '.':
                result.append('.')
        # # case
        if char == '#':
            # always add one
            result.append('#')
    return result

def compute(lines):
    # seperate them
    parts = []
    for line in lines:
        almost = line.split()
        nums = almost[1].split(",")
        parts.append((almost[0], nums))
    # let's try it out
    for part in parts:
        code = find_spots(part)


def main():
    file = open("input/day12.txt", "r", encoding="utf8")
    lines = file.readlines()
    start_time = time.time()
    print(f"This program completed in {time.time() - start_time}")


if __name__ == "__main__":
    main()