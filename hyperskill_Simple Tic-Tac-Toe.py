grid = '         '
list_grid = list(grid)
X_win = 0  #X winning variable
O_win = 0  #O winning variable
pos_test = 0 #possibility test
competitor = 1
main_loop = 1
def winning_test(x):
    global X_win, O_win, pos_test
    list_grid = list(x)
    #winning conditions X
    for i in range(0, 7, 3):
        if (list_grid[i]  == 'X' and list_grid[i + 1] == 'X' and list_grid[i + 2] == 'X'):
            X_win = 1
    for i in range(0, 3, 1):
        if (list_grid[i] == 'X' and list_grid[i + 3] == 'X' and list_grid[i + 6] == 'X'):
            X_win = 1
    for i in range(0, 3, 2):
        if (list_grid[0 + i] == 'X' and list_grid[4] == 'X' and list_grid[8 - i] == 'X'):
            X_win = 1
    #winning conditions O
    for i in range(0, 7, 3):
        if (list_grid[i] == 'O' and list_grid[i + 1] == 'O' and list_grid[i + 2] == 'O'):
            O_win = 1
    for i in range(0, 3, 1):
        if (list_grid[i] == 'O' and list_grid[i + 3] == 'O' and list_grid[i + 6] == 'O'):
            O_win = 1
    for i in range(0, 3, 2):
        if (list_grid[0 + i] == 'O' and list_grid[4] == 'O' and list_grid[8 - i] == 'O'):
            O_win = 1
    #possibility test
    if (X_win == 1 and O_win == 1) or (abs(list_grid.count("X") - list_grid.count("O")) >= 2):
        pos_test = 1
def board_print(list_grid):
    #board
    print('---------')
    print('| {} {} {} |'.format(list_grid[0], list_grid[1], list_grid[2], ))
    print('| {} {} {} |'.format(list_grid[3], list_grid[4], list_grid[5], ))
    print('| {} {} {} |'.format(list_grid[6], list_grid[7], list_grid[8], ))
    print('---------')
def results_interpretation(pos_test, X_win, O_win, list_grid):
    global main_loop
    if pos_test == 1:
        print('Impossible')
    elif (X_win == 0 and O_win == 0) and all(x != ' ' for x in list_grid):
        print('Draw')
        main_loop = 0
    elif X_win == 1:
        print('X wins')
        main_loop = 0
    elif O_win == 1:
        print('O wins')
        main_loop = 0
def user_inp_processing(x):
    global input_loop_ctrl, list_grid, competitor
    inp_list = x.split(' ')
    if competitor == 1:
        sign = 'X'
    elif competitor == -1:
        sign = 'O'
    if (inp_list[0].isnumeric() and inp_list[1].isnumeric()):
        if (int(inp_list[0]) > 3 or int(inp_list[1]) > 3):
            print('Coordinates should be from 1 to 3!')
            input_loop_ctrl = 0
        elif list_grid[((int(inp_list[0]) - 1) * 3 + int(inp_list[1]) - 1)] != ' ':
            print('This cell is occupied! Choose another one!')
            input_loop_ctrl = 0
        else:
            list_grid[((int(inp_list[0]) - 1) * 3 + int(inp_list[1]) - 1)] = sign
            competitor = -1 * competitor
            input_loop_ctrl = 0
    else:
        print('You should enter numbers!')

board_print(list_grid)

while main_loop == 1:
    user_inp = input()
    input_loop_ctrl = 1
    while input_loop_ctrl == 1:
        user_inp_processing(user_inp)
    #board output
    board_print(list_grid)
    winning_test(list_grid)
    #results
    results_interpretation(pos_test, X_win, O_win, list_grid)

