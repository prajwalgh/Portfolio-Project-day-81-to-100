bord = [[7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]


# solve the bord
def solve(bor):
    find = find_empyt(bor)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bor, i, (row, col)):
            bor[row][col] = i

            if solve(bor):
                return True

            bor[row][col] = 0
    print("solve is running")
    return False

# validate id given input is proper or not
def valid(bor, num, pos):
    # check for row
    for i in range(len(bor[0])):
        if bor[pos[0]][i] == num and pos[1] != i:
            return False
    # check for column
    for i in range(len(bor)):
        if bor[i][pos[1]] == num and pos[0] != i:
            return False
    # check for 3 X 3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bor[i][j] == num and (i, j) != pos:
                return False
    return True


# print grid start
def print_grid(bor):
    for i in range(len(bor)):
        if i % 3 == 0 and i != 0:
            print("-------------------------------- ")
        for j in range(len(bor[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(bor[i][j])
            else:
                print(str(bor[i][j]) + "  ", end=" ")


# print grid end


# find first empty slot
def find_empyt(bor):
    for i in range(len(bor)):
        for j in range(len(bor[0])):
            if bor[i][j] == 0:
                return (i, j)  # empyt slot
    return None



# https://www.youtube.com/watch?v=lK4N8E6uNr4&ab_channel=TechWithTim

#print_grid(bord)
#print("________________________________________________________")
#solve(bord)
#print("________________________________________________________")
#print_grid(bord)


