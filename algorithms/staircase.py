print "Build a staircase! Type a number and press Enter:"
n = int(raw_input().strip())

def space_maker2(n, staircase):
    space = n - len(staircase)
    space_string = ""
    for i in range(space):
        space_string += " "
    return space_string

staircase = ""
for i in range(n):
    staircase += "#"
    print space_maker2(n, staircase) + staircase
