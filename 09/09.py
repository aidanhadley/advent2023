# ldas

# i think this will introduce recursion
def find_diffs(nums):
    # nums is an array
    result = []
    for i in range(1, len(nums)):
        result.append(int(nums[i]) - int(nums[i - 1]))
    return result

def find_h(nums):
    # nums is an array, output the next number
    history = []
    # array or arrays lol
    clist = nums
    
    while not all(x == 0 for x in clist):
        history.append(clist)
        clist = find_diffs(clist)
    # reverse the history
    rhistory = history[::-1]
    return rhistory
    
def find_next(nums):
    rhistory = find_h(nums)
    sumber = 0
    for arr in rhistory:
        sumber += int(arr[len(arr) - 1])
    return sumber

def part1(lines):
    result = 0
    for line in lines:
        nums = line.split()
        result += find_next(nums)
    return result

def find_prev(nums):
    rhistory = find_h(nums)
    sumber = rhistory[0][0]
    for x in range(1, len(rhistory)):
        sumber = int(rhistory[x][0]) - sumber
    return sumber

def part2(lines):
    result = 0
    for line in lines:
        nums = line.split()
        result += find_prev(nums)
    return result
        

def main():
    file = open("09/input.txt", "r", encoding="utf8")
    lines = file.readlines()
    test = [0, 3, 6, 9, 12, 15, 18, 21]
    # test = [1, 3, 6, 10, 15, 21]
    # test = [10, 13, 16, 21, 30, 45]
    # p_int = find_prev(test)
    # print(p_int)
    answer1 = part1(lines)
    print(answer1)
    answer2 = part2(lines)
    print(answer2)


if __name__ == "__main__":
    main()