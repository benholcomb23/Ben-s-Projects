toprow = ['0', '1', '2']
midrow = ['3', '4', '5']
botrow = ['6', '7', '8']

playing_field = [toprow, midrow, botrow]

popped_value = None
x_queue = []
o_queue = []

def coordinateChange(user_input):
    column = user_input % 3
    row = user_input // 3
    return (row, column)

def printField():
    for list in playing_field:
        print(list)

def reset_field():
    field_string = -1
    for row in range(0,3):
        for column in range(0,3):
            field_string += 1
            playing_field[row][column] = str(field_string)

def getInput(turn):
    # print("Get input o_queue is " + str(o_queue) + " and x_queue is " + str(x_queue) + "And turn is" + str(turn))
    if turn == True:
        x_input = input("Player one, play an X 0-8...")
        return x_input
    elif turn == False:
        o_input = input("Player two, play an O 0-8")
        return o_input
    else:
        print("getInput not fucking working")

def chooseSymbol(turn):
    if turn == True:
        return "X"
    else:
        return "O"
    
def playTurn(turn):
    # print("1.) debug, o_queue is " + str(o_queue) + " and x_queue is " + str(x_queue))
    symbol = chooseSymbol(turn)
    valid_input = False
    while valid_input == False:
        nrow, ncolumn, nactivate = checknPopped(turn)
        change_field(nrow, ncolumn, "!", nactivate)
        printField()
        input = getInput(turn)
        try:
            input = int(input)
        except ValueError:
            print("ValueError: Enter a valid position")
        if input in range(0, 9):
            (row, column) = coordinateChange(input)
            if playing_field[row][column] != 'X' and playing_field[row][column] != 'O' and playing_field[row][column] != '!':
                valid_input = True
                prow, pcolumn, pvalue, pactive = addToQueue(turn, input)
                change_field(row, column, symbol, True)
                win = checkWinCon(turn)
                change_field(prow, pcolumn, pvalue, pactive)
                return win
                # print("The main change field function row and column is " + str(row) + str(column))
            else:
                print("Sorry, this spot is taken")
        else:
            print("BadInput: Enter a valid position")

def checknPopped(turn):
    activate = False
    if turn == True:
        if len(x_queue) > 2:
            x, y = nextPop(x_queue)
            activate = True
            return x, y, activate
        else:
            return 0, 0, False
    else:
        if len(o_queue) > 2:
            x, y = nextPop(o_queue)
            activate = True
            return x, y, activate
        else:
            return 0, 0, False

def change_field(row, column, print_value, active):
    if active == True:
        playing_field[row][column] = str(print_value)

def addToQueue(turn, input):
    if turn == True:
        x_queue.insert(0, input)
        if len(x_queue) > 3:
            x, y, v = popValue(x_queue)
            return (x, y, v, True)
        else:
            return (0, 0, 0, False)
    else:
        o_queue.insert(0, input)
        if len(o_queue) > 3:
            x, y, v = popValue(o_queue)
            return (x, y, v, True)
        else:
            return (0, 0, 0, False)

# Pop list should be: (Popped Row, Popped Column, UserinputValue, PopBool(y or n), nextpopped row, nextpopped column, Nextpop(y or n))

def nextPop(coord):
    if coord == x_queue:
        next_pop = x_queue[2]
        npoprow, npopcolumn = coordinateChange(next_pop)
    elif coord == o_queue:
        next_pop = o_queue[2]
        npoprow, npopcolumn = coordinateChange(next_pop)
    return npoprow, npopcolumn

def popValue(coord):
    if coord == x_queue:
        popped_value = x_queue[3]
        poprow, popcolumn = coordinateChange(popped_value)
        x_queue.pop(3)
    elif coord == o_queue:
        popped_value = o_queue[3]
        poprow, popcolumn = coordinateChange(popped_value)
        o_queue.pop(3)
    return poprow, popcolumn, popped_value

def listCheck(list, turn):
    list_check = False
    if (turn == True) and (list.count("X") == 3  or (list.count("X") == 2 and list.count("!") == 1)): 
        list_check = True
    elif (turn == False) and (list.count("O") == 3 or (list.count("O") == 2 and list.count("!") == 1)):
        list_check = True
    else:
        list_check = False
    return list_check

    # ! X X

def checkWinCon(turn):
    diag_one = [toprow[0], midrow[1], botrow[2]]
    diag_two = [botrow[0], midrow[1], toprow[2]]
    vert_one = [toprow[0], midrow[0], botrow[0]]
    vert_two = [toprow[1], midrow[1], botrow[1]]
    vert_three = [toprow[2], midrow[2], botrow[2]]
    possible_3_patterns = [toprow, midrow, botrow, diag_one, diag_two, vert_one, vert_two, vert_three]
    for list in possible_3_patterns:
        if listCheck(list, turn) == True:
            return True
        
def playAgain(turn):
    play_again_loop = True
    while play_again_loop == True:
        if turn == True:
            play_again = input("X wins! Play again? y or n")
        else:
            play_again = input("O wins! Play again? y or n")
        if play_again == "y":
            play_again_loop = False
            return True
        elif play_again == "n":
            print("Goodbye!")
            play_again_loop = False
            return False 
        else:
            print("Not a valid answer, king")

# While loop that plays until break
def mainloop():
    #Initializing New Game
    reset_field()
    x_queue.clear()
    o_queue.clear()
    gameplay = True
    player_turn = True
    input("Welcome to infinite tik tac toe!")
    # Mainloop
    while gameplay == True:
        win = playTurn(player_turn)
        if win == True:
            if playAgain(player_turn) == True:
                gameplay = False
                mainloop()
            else:
                gameplay = False
                break
        else:
            player_turn = not player_turn

mainloop()