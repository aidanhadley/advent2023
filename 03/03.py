# ldas

#introducing... CLASSES!!!
class Number:
    def __init__(self):
        # constructor method
        self.value = ''
        self.coords = []
    
    def add_character(self, character, x, y):
        # self is like this
        # character is a char i think
        # x and y are number coordinates
        self.value += character
        self.coords.append((x, y))
        
    def is_adjacent_to(self, symbol):
        # symbol is like + or *, it has a location
        sx = symbol.x
        sy = symbol.y
        # see if it's within one
        for x, y in self.coords:
            if abs(x - sx) <= 1 and abs(y - sy) <= 1:
                return True
        return False
    
    def __str__(self):
        return f"Num {self.value}, at {self.coords}"

class Symbol:
    # how to pass in items to the constructor
    def __init__(self, character, x, y):
        self.value = character
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Sym {self.value} at {self.x}, {self.y}"

def print_graph(arr):
    for line in arr:
        print("[", end='')
        for item in line:
            print(item, end=", ")
        print("]")
        print()

def builder(lines):
    # make a new array
    schematic = []
    
    for y, line in enumerate(lines):
        schematic_row = []
        
        cnum = Number()
        for x, character in enumerate(line):
            if(character.isdigit()):
                cnum.add_character(character, x, y)
            else:
                if cnum.value:
                    # value is not empty
                    schematic_row.append(cnum)
                    cnum = Number()
                if character != ".":
                    # it's a symbol!
                    schematic_row.append(Symbol(character, x, y))
        # but what if it ENDED on a number??
        if cnum.value:
            schematic_row.append(cnum)
        # add to the whole schematic
        schematic.append(schematic_row)
    return schematic

def part1(lines):
    schematic = builder(lines)
    slen = len(schematic)
    result = 0
    print_graph(schematic)
    for y, row in enumerate(schematic):
        # find min and max (in bounds)
        min_y = max(0, y - 1)
        max_y = min(slen, y + 1)
        # find adjacent rows by SLICING
        arows = schematic[min_y:max_y + 1]
        
        for item in row:
            if isinstance(item, Symbol):
                for adj_row in arows:
                    for other_item in adj_row:
                        if isinstance(other_item, Number) and other_item.is_adjacent_to(item):
                            result += int(other_item.value)
    return result

def main():
    file = open("03/input.txt", "r", encoding="utf8")
    lines = file.readlines()
    print(part1(lines))

if __name__ == "__main__":
    main()