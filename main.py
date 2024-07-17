import random
def check(main_sudoku, m, x, y):
    list_tekrari = []
    
    # Check the row
    for j in range(9):
        if main_sudoku[x][j] == m and j != y and m != 0:
            list_tekrari.append([x, j])
    
    # Check the column
    for i in range(9):
        if main_sudoku[i][y] == m and i != x and  m != 0  :
            list_tekrari.append([i, y])
    
    # Check the 3x3 block
    start_row = (x // 3) * 3
    start_col = (y // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if main_sudoku[i][j] == m and (i != x or j != y) and m != 0:
                list_tekrari.append([i, j])
    
    # Add the current position
    list_tekrari.append([x, y])
    
    return list_tekrari

def clear_board(main_sudoku: list, initials_list: list):
    x, y = map(int, input().split())
    if x < 0 or x > 8 or y < 0 or y > 8:
        print('index input out of range')
        return
    if [x, y] in initials_list:  # Check if the cell is in the initial list
        print("Can't change this index because it's an initial value.")
    else:
        main_sudoku[x][y] = 0
def win_check(main_soduko : list) -> bool :
    for i in range(9):
        for j in range(9):
            if main_soduko[i][j] == 0:
                return False
    for i in range(9):
        for j in range(9):
            if(len(check(main_soduko, main_soduko[i][j], i, j)) > 1 ):
                return False
    return True
def initails_list_maker(main_soduku: list) -> list:
    initials_list = []
    for i in range(9):
        for j in range(9):
            if main_soduku[i][j] != 0 :
                initials_list.append([i, j])
    return initials_list
def inp(main_soduku : list, initials_list : list) :
    x , y , value = map(int, input().split())
    if x > 8 or y > 8 or x < 0 or y < 0 :
        print('index input out of range')
        return -1, -1 , main_soduku
    if main_soduku[x][y] == 0 :
        main_soduku[x][y] = value
        return x, y, main_soduku
    for i in range (len(initials_list)):
        if initials_list[i][0] == x and initials_list[i][1] == y:
            print("can't insert into initials")
            return -1, -1, main_soduku
    print("can't insert that number cause this cell is not empty please clear it first")
    return -1, -1, main_soduku

def print_main_soduku(main_soduku : list) :
    for i in range(9):
        if i % 3 != 2:
            for j in range(9):
                if j % 3 != 2:
                    print(f"{main_soduku[i][j]}|", end="")
                    if j == 8:
                        print()
                elif j % 3 == 2:
                    print(f"{main_soduku[i][j]} |*| ", end="")
                    if j == 8:
                        print()
        elif i % 3 == 2:
            for j in range(9):
                if j % 3 != 2:
                    print(f"{main_soduku[i][j]}|", end="")
                    if j == 8:
                        print()
                elif j % 3 == 2:
                    print(f"{main_soduku[i][j]} |*| ", end="")
                    if j == 8:
                        print()
            print(29 * "=")
