"""
틱텍토 게임 만들기
2명의 플레이어가 번갈아 가면서 3x3크기의 판에 O 와 X를 표시하면서 연속되게 만들면 승리하는 게임이다.

1.메인 게임을 시작한다.
2.첫번째 플레이어가 O,X 중 하나를 고른다.

3.3x3 화면을 출력한다.
4.입력을 받는다.
5.승리조건인지 확인한다.

6.승리조건이 아니라면 3,4,5를 반복한다.
7.승리조건이라면 승리메시지와 다시 플레이 할지를 물어본다.

"""
def make_board():
    return [[" " for i in range(3)] for x in range(3) ]

def make_visted_board():
    return [[False for i in range(3)] for x in range(3) ]

def display_board(pans):
    for row in pans:
        print(row)
    
def choice_o_x():
    player1 = ""
    player2 = ""
    choice = ""
    
    while choice not in ["O", "X"]:
        choice = input("Choice your mark!!! O or X : ")
        choice = choice.upper()
        if choice not in ["O", "X"]:
            print("Invalid Input please choice O or X!")

    if choice == "O":
        player1 = "O"
        player2 = "X"
    else:
        player1 = "X"
        player2 = "O"
    return player1, player2


def choice_number(pans, player, visited):
    row = ""
    col = ""
    
    while row not in ["0", "1", "2"] or col not in ["0", "1", "2"]:
        row, col = input("please choice number!! (row, col)>>>").split()
        
        if row not in ["0", "1","2"] or col not in ["0", "1", "2"]:
            print("please check input!!!!")
        
        elif row in ["0","1","2"] and col in ["0", "1", "2"]:           
            row = int(row)
            col = int(col)
            if visited[row][col] == True:
                print("Already checked please check another Choice")
            else:
                break

    row = int(row)
    col = int(col)        
    pans[row][col] = player
    visited[row][col] = True
    return pans, player, visited


def check_victory(board):
    # 가로
    for row in board:
        if row[0] == row[1] == row[2] and " " not in row:
            return True
    
    # 세로
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " " :
            return True

    # 대각선
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    return False

from random import randint

def temp_player(player1, player2):
    number = randint(0,1)
    if number == 0:
        return player1, player2
    else:
        return player2, player1


def check_full(visited_board):
    if False not in visited_board[0] and False not in visited_board[1] and False not in visited_board[2]:
        return True

def replay_game():
    choice = ""
    
    while not (choice == "Yes" or choice == "No"):
        choice = input("Do you want replay game? Yes or No >>> ")

    if choice== "Yes":
        return True
    else:
        return False





print("----- Welcome Tic Tac Toc Game ------")
print()
while True:
    board = make_board()
    visited_board = make_visted_board()
    player1, player2 = choice_o_x()
    first_player, second_player = temp_player(player1, player2)
        
    game_on = True
    turn_over = True

    while game_on:
        display_board(board)
        if turn_over:
            board, first_player, visited_board = choice_number(board, first_player, visited_board)
            turn_over = False
            check = check_victory(board)
        
            if check:    
                display_board(board)
                print(f"winner is {first_player}")
                game_on = False
                    
        else:
            board, second_player, visited_board = choice_number(board, second_player, visited_board)
            turn_over = True

            check = check_victory(board)
        
            if check:    
                display_board(board)        
                print(f"winner is {second_player}")
                game_on = False

        full = check_full(visited_board)  
        if check == False and full == True:
            print("무승부 입니다.")
            display_board(board)
            game_on = False

    if replay_game():
        continue
    else:
        break


