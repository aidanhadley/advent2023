def convert_lines(lines):
    # should have two delimiters
    result = []
    for line in lines:
        # convert into 2 lines
        almost = line.split(':')
        soClose = almost[1].split('|')
        soClose[1] = soClose[1].rstrip()
        # convert each into a list
        toAdd = []
        closer1 = soClose[0].split()
        closer2 = soClose[1].split()
        # print(closer1, closer1)
        toAdd.append(closer1)
        toAdd.append(closer2)
        result.append(toAdd)
    return result


def part1(lines):
    array = convert_lines(lines)
    sumber = 0
    for line in array:
        totals = 0
        isFirst = True
        for winner in line[0]:
            for lucky in line[1]:
                if winner == lucky:
                    if isFirst:
                        totals += 1
                        isFirst = False
                    else:
                        totals *= 2
        sumber += totals
    print(f"The total number of winning points is {sumber}")

def part2(lines):
    array = convert_lines(lines)
    sumber = 0
    # make a new array for each ticket (to keep track)
    tickets = []
    for ticket in array:
        tickets.append([ticket])
    for ticket in tickets:
        print(ticket)
    
# debug
def print_converted(converted):
    for line in converted:
        print(line)

def main():
    file = open('input/day4e.txt', 'r', encoding="utf8")
    lines = file.readlines()
    # converted = convert_lines(lines)
    # print_converted(converted)
    part2(lines)
    
if __name__ == "__main__":
    main()