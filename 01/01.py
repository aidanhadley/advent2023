file1 = open("01/input.txt", "r", encoding='utf8')
lines = file1.readlines()

sumber = 0
for line in lines:
    # nums = re.findall(r'\d+', line)
    # GAMEPLAN: split string into sequence of chars, and if it's 0-9,
    # take the first two and add them together
    seq = list(line)
    num1 = num2 = 0
    for thing in seq:
        if (
            thing == "0"
            or thing == "1"
            or thing == "2"
            or thing == "3"
            or thing == "4"
            or thing == "5"
            or thing == "6"
            or thing == "7"
            or thing == "8"
            or thing == "9"
        ):
            if num1 == 0:
                num1 = int(thing)
            num2 = int(thing)
    sumber += (num1 * 10) + num2
    print(sumber)


# part 2 (with the help of chatgpt and oogles from github lol)
# DICTIONARY: hashmap but i python
word_to_num = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# used to find digits with regex is
def find_digit(string, reverse=False):
    start = 0
    stop = len(string) + 1
    step = 1
    # back to front
    if reverse:
        start = -1
        stop *= -1
        step *= -1

    # search character by character
    for i in range(start, stop, step):
        if string[i].isdigit():
            return string[i]

        # increment up (or down) and see if there's a word that matches in the string
        if reverse:
            substr = string[i:]
        else:
            substr = string[: i + step]

        for word, digit in word_to_num.items():
            if word in substr:
                return digit


sumber = 0
for line in lines:
    num1 = find_digit(line)
    # print(num1)
    num2 = find_digit(line, True)
    # print(num2)
    print((int(num1) * 10) + int(num2))
    sumber += (int(num1) * 10) + int(num2)
    print(sumber)
