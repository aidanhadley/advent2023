import re


# part 1: The Elf would first like to know which games would have been possible
# if the bag contained only :
# 12 red cubes, 13 green cubes, and 14 blue cubes?
def find_maxes(line):
    # print("NEWLINE")
    seq = line.split()
    red = green = blue = 0
    for i, j in enumerate(seq):
        # add reds
        if re.search(r"\bred\b", j):
            if int(seq[i - 1]) > red:
                red = int(seq[i - 1])
        # add greens
        if re.search(r"\bgreen\b", j):
            if int(seq[i - 1]) > green:
                green = int(seq[i - 1])
        # add blues
        if re.search(r"\bblue\b", j):
            if int(seq[i - 1]) > blue:
                blue = int(seq[i - 1])
    # now we have the totals
    result = [red, green, blue]
    return result


def part1(lines):
    sumber = 0
    for line in lines:
        seq = line.split()
        nums = find_maxes(line)
        # use 'and' instead of & because that's bitwise lol
        red = nums[0]
        green = nums[1]
        blue = nums[2]
        if red <= 12 and green <= 13 and blue <= 14:
            num = re.search(r"\b(\d+)\b", seq[1])
            sumber += int(num.group(1))
    print(sumber)


# what is the fewest number of cubes of each color that could have been in the
# bag to make the game possible? The power of a set of cubes is equal to the
# numbers of red, green, and blue cubes multiplied together. What is the sum of
# the power of these sets?
def part2(lines):
    sumber = 0
    for line in lines:
        nums = find_maxes(line)
        red = nums[0]
        green = nums[1]
        blue = nums[2]
        power = red * green * blue
        sumber += power
    print(sumber)


def splitter(line):
    # line is a string
    seq = line.split()
    return seq


# main method
def main(file):
    # file = open("02/input.txt", "r", encoding="utf8")
    lines = file.readlines()
    part1(lines)
    part2(lines)


if __name__ == "__main__":
    main(None)
