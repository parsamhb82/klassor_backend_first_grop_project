from colorama import Fore, Back, Style
import random
import time
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
    if x > 8 or y > 8 or x < 0 or y < 0  :
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

def print_main_soduku(main_soduku : list, initials_list : list) :
    for i in range(9):
        for j in range(9):
            if j % 3 != 2:
                list_tekrari = check(main_soduku, main_soduku[i][j], i, j)
                if len(list_tekrari) >= 2 :
                    print(f"{Fore.RED}{main_soduku[i][j]}{Style.RESET_ALL}|",end='')
                elif [i, j] in initials_list :
                    print(f"{main_soduku[i][j]}|", end ='')
                elif main_soduku[i][j] != 0:
                    print(f"{Fore.YELLOW}{main_soduku[i][j]}{Style.RESET_ALL}|",end = '')
                else :
                    print(f"{main_soduku[i][j]}|", end = '')
            elif j % 3 == 2:
                list_tekrari = check(main_soduku, main_soduku[i][j], i, j)
                if len(list_tekrari) >= 2 :
                    print(f"{Fore.RED}{main_soduku[i][j]}{Style.RESET_ALL} |*| ",end='')
                elif [i, j] in initials_list :
                    print(f"{main_soduku[i][j]} |*| ", end ='')
                elif main_soduku[i][j] != 0:
                    print(f"{Fore.YELLOW}{main_soduku[i][j]}{Style.RESET_ALL} |*| ",end = '')
                else :
                    print(f"{main_soduku[i][j]} |*| ", end = '')
            if j == 8 :
                print()
        if i % 3 == 2 :
            print('=' * 29)
            
                    


    


n = random.randint(0,1)
easy_board1 = [
    [2, 0, 1, 8, 0, 0, 0, 0, 4],
    [8, 9, 0, 3, 0, 0, 2, 6, 1],
    [0, 6, 7, 1, 0, 9, 0, 0, 5],
    [0, 0, 8, 0, 0, 6, 0, 0, 0],
    [0, 0, 3, 5, 0, 0, 6, 0, 0],
    [0, 0, 2, 7, 4, 3, 0, 9, 8],
    [0, 0, 0, 0, 0, 0, 0, 1, 9],
    [5, 0, 9, 0, 3, 2, 0, 0, 6],
    [0, 0, 0, 0, 1, 7, 4, 5, 2]
]
easy_board2 = [
    [0, 0, 0, 1, 0, 0, 0, 0, 3],
    [2, 1, 8, 0, 0, 6, 7, 0, 4],
    [7, 5, 0, 0, 0, 4, 0, 6, 0],
    [0, 4, 9, 8, 3, 1, 2, 0, 0],
    [5, 3, 1, 0, 0, 0, 0, 4, 8],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 6, 2, 0, 0, 0, 0, 0, 0],
    [0, 8, 5, 7, 6, 3, 4, 9, 0],
    [0, 0, 4, 9, 2, 0, 5, 1, 0]
]
mid_board1 = [
    [4, 0, 2, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 8, 0],
    [6, 0, 0, 0, 9, 0, 0, 5, 0],
    [2, 0, 0, 3, 0, 0, 0, 9, 0],
    [0, 0, 4, 1, 5, 0, 0, 0, 0],
    [0, 1, 7, 0, 2, 0, 0, 4, 3],
    [0, 0, 3, 5, 8, 0, 9, 7, 0],
    [5, 0, 9, 4, 0, 7, 2, 6, 1],
    [7, 4, 6, 9, 1, 0, 8, 0, 5]
]
mid_board2 = [
    [0, 0, 0, 0, 8, 0, 0, 0, 3],
    [0, 7, 3, 0, 0, 0, 1, 0, 5],
    [4, 6, 0, 1, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 5, 0, 0, 7, 6],
    [0, 3, 2, 8, 6, 1, 0, 4, 9],
    [6, 9, 5, 7, 0, 3, 0, 2, 1],
    [0, 0, 4, 0, 0, 0, 6, 0, 0],
    [0, 0, 0, 3, 0, 4, 0, 0, 2],
    [3, 5, 0, 0, 2, 8, 0, 0, 0]
]
hard_board1 = [
    [5, 9, 0, 8, 2, 7, 0, 0, 0],
    [0, 1, 0, 6, 0, 9, 0, 5, 0],
    [6, 2, 0, 5, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 6, 0, 0, 0, 0, 7, 0, 0],
    [2, 4, 8, 0, 5, 0, 1, 0, 0],
    [0, 0, 1, 9, 0, 0, 3, 0, 8],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 5, 6, 1]
]

hard_board2 = [
    [4, 7, 0, 0, 0, 0, 6, 0, 8],
    [0, 6, 2, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 4, 2, 0, 1],
    [8, 9, 0, 5, 0, 6, 0, 3, 7],
    [0, 0, 6, 0, 0, 0, 8, 0, 5],
    [0, 0, 0, 0, 0, 1, 0, 0, 2],
    [9, 0, 0, 0, 0, 0, 5, 8, 0],
    [6, 8, 7, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 6, 3, 0, 0, 0]
]


easy_boards = [easy_board1, easy_board2]
mid_boards = [mid_board1, mid_board2]
hard_boards = [hard_board1, hard_board2]
level = input("inset your difficulity Easy | Medium | Hard: ")
if level == "Easy":
    main_soduku = easy_boards[n]
elif level == "Medium":
    main_soduku = mid_boards[n]
elif level == "Hard":
    main_soduku = hard_boards[n]
else:
    print("Invalid level")
    exit()






print('please give your input indices from 0 to 8')
initials_list = initails_list_maker(main_soduku)
print_main_soduku(main_soduku, initials_list)
start = time.time()
while not win_check(main_soduku):
    approach = input("what do you want to do? clear | insert :" )
    if approach == 'insert' :
        print('now tell me which indices you want to insert and what value? x | y | value')
        x, y, main_soduku = inp(main_soduku, initials_list)
        if x != -1 :
            for i in range(9):
                list_tekrari = []
                for j in range(9):
                    list_tekrari = check(main_soduku,main_soduku[i][j],i, j)
                    if len(list_tekrari) >= 2 :
                        print(f'conflicts in{list_tekrari[1:]}')
        print_main_soduku(main_soduku, initials_list)

            
    elif approach == 'clear' :
        print('which indices you want to delete? i | j')
        clear_board(main_soduku, initials_list)
        for i in range(9):
                list_tekrari = []
                for j in range(9):
                    list_tekrari = check(main_soduku,main_soduku[i][j],i, j)
                    if len(list_tekrari) >= 2 :
                        print(f'conflicts in{list_tekrari[1:]}')
        print_main_soduku(main_soduku, initials_list)

    else :
        print_main_soduku(main_soduku, initials_list)

        print("wrong approach")
end = time.time()

print("You Won")
print(f'elapsed time{end - start}')
