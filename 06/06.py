
def calculate_methods(tu):
    # tu is short for tuple
    time = tu[0]
    result = []
    for i in range(time + 1):
        # hold the button for i ms
        t = time - i
        # i is your speed, GO FAST!!!! s = vt
        completion = i * t
        result.append((i, completion))
    return result

def find_wins(arr, record):
    # arr is an array of the tuples in (seconds held, distance went) format
    # record is the current WORLD RECORD FOR THE RACE lol
    result = []
    for item in arr:
        if item[1] > record:
            result.append(item[0])
    return result
    

def calc(races):
    # i am NOT racist
    sumber = 1
    for item in races:
        wins = find_wins(calculate_methods(item), item[1])
        sumber *= len(wins)
    print(f"The number of wins multiplied is {sumber}")
        
    


def main():
    # since the file is so simplistic im going to just make a 2d array lol
    # who needs file reading when I CAN READ
    races1 = [(50, 242), (74, 1017), (86, 1691), (85, 1252)]
    calc(races1)
    races2 = [(50748685, 242101716911252)]
    calc(races2)
    
if __name__ == "__main__":
    main()
    