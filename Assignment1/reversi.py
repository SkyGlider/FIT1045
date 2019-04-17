#ANDREW PANG YONG CHEN 30506271
#FIT 1045
#STARTED : 18 MAR 2019
#COMPLETED : 20 MAR 2019
#SUBMITTED : 4 APR 2019
#ASSIGNMENT 1 TASK 2



#new board creates a fresh board
def new_board() :
    
    zeros = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    zeros4 = [ 0, 0, 0, 2, 1, 0, 0, 0 ]
    zeros5 = [ 0, 0, 0, 1, 2, 0, 0, 0 ]
    #concatannates all the boards into alist
    board = [ zeros[:], zeros[:], zeros[:], zeros4,
              zeros5, zeros[:], zeros[:], zeros[:] ]
    
    return board




def print_board(board) :
    
    #prints header line
    print('  a b c d e f g h')
    
    #prints every board line
    for i in range(len(board)) :
        no_line = str(board[i])
        no_line = no_line.replace('[','')
        no_line = no_line.replace(']','')
        no_line = no_line.replace(',','')
        no_line = no_line.replace('1','B')
        no_line = no_line.replace('2','W')
        no_line = no_line.replace('0','.')
        print(str(i+1) + " " + no_line)
        
    #prints seperator line
    print('-----------------')




#gets score
def score(board) :
    
    bl = 0
    wh = 0

    #runs through each element in each list in board
    #counts the w and b tokens
    for i in board:
        for j in i:
            if j == 1:
                bl +=1
            elif j == 2:
                wh += 1

    return (bl,wh)




#enclosing fucntion checks for move validity
def enclosing(board, player, pos, direct) :

    move_validity = False
    
    if player == 1 :
        opponent = 2
    else:
        opponent = 1

    #tries to checks the stone ajacent to the chosen position
    #try except is to prevent out of range exception
    try:
        stone_next = board[pos[0]+direct[0]][pos[1]+direct[1]]
    except:
        return False


    if stone_next == opponent:

        y_dr = direct[0]
        x_dr = direct[1]

        #boundaries for while loop to prevent out of range error
        while (pos[0]+y_dr) < 8 and (pos[0]+y_dr) > -1 and (pos[1]+x_dr) < 8 and (pos[1]+x_dr) > -1  :

            #checks every succesive stone in specified direction
            stone_adj = board[pos[0]+y_dr][pos[1]+x_dr]
           
            if stone_adj == player:
                move_validity = True
                break
            
            elif stone_adj == 0:            
                break

            y_dr += direct[0]
            x_dr += direct[1]
            
    #if a stone of current player is found, then move is valid
    #if while loop overflows/any other conditions, move is invalid
    return move_validity




def valid_moves(board, player):
    
    #this fucntion checks every single empty grid
    #it also checks all 8 directions through the enclosig function
    #returns a list of valid positions
    valid_list = []
    for row in range(8):
        for col in range(8):
                for v_dr in range(-1,2):
                    for h_dr in range(-1,2): 
                        if board[row][col] == 0:
                                if enclosing(board, player, (row,col), (v_dr,h_dr)) == True :
                                    valid_list.append((row,col))
                            
    return valid_list




def next_state(board, player, pos) :
    
     if player == 1:
          next_player = 2
     else :
          next_player = 1

     #gets valid moves for both players
     valid_pos = valid_moves(board,player)
     valid_pos2 = valid_moves(board,next_player)

     #checks if player entered a valid position
     if pos in valid_pos:
        
        board[pos[0]][pos[1]] = player
        
        #calls the switch function (additional function)
        #flips the stones between each position
        next_board = switch(board,player,pos)
          
     elif valid_pos == []:

        #if both players have no moves, it returns 0
        if valid_pos2 == []:
            next_player = 0
        else:
            print('No more moves')

        next_board = board
               
     else:
         print('Invalid Move!')
         next_board = board
         next_player = player

     return (next_board, next_player)
               



#ADDITIONAL FUNCTION
#flips the opponent's coin in between player's stone
def switch(board, player, pos) :

    if player == 1:
        opponent = 2
    else :
        opponent = 1

    #runs through all direction of selected grid
    for row in range (-1,2):    
        for col in range (-1,2):
            
            y_dr = row
            x_dr = col
            #temp list contains the positions where flips have to be made
            chg_list= []

            #while loop runs through every successive stone in one direction
            while (pos[0]+y_dr) < 8 and (pos[0]+y_dr) > -1 and (pos[1]+x_dr) < 8 and (pos[1]+x_dr) > -1  :
                
                stone_adj = board[pos[0]+y_dr][pos[1]+x_dr]
                
                if stone_adj == player:

                    for i in range(len(chg_list)):
                        #flips the stones
                        board [chg_list[i][0]] [chg_list[i][1]] = player
                    #exits the while loop once flips are made
                    break
            
                elif stone_adj == opponent:            
                    chg_list.append([(pos[0]+y_dr),(pos[1]+x_dr)])

                else :
                    #no flips done if succesive stone is empty
                    break
                
                y_dr += row
                x_dr += col
    
    switched_board = board
    
    return switched_board



#converts input to computer readable coordinates
def position(string):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    slist = list(string)
    row = slist[1]
    col = slist[0]
    pos = 0
    
    if len(slist) == 2 and (col in alpha) and (row in nums) :
        row_pos = nums.index(row)
        col_pos = alpha.index(col)
        pos = (row_pos,col_pos)

    return pos



#ADDITIONAL FUNCTION
#calcualtes the position that has maximum score
#used for run_singe_player
def get_pos(board):
    
    valid_pos = valid_moves(board,2)
    
    if valid_pos == []:
        return (0,0)
    
    max_pts = 0
    best_pos = None

    #checks every position available in valid_pos for highest score
    for i in valid_pos :
        
        total_pts = 0
        
        for row in range (-1,2):    
            for col in range (-1,2):
                
                y_dr = row
                x_dr = col
                score = 0
                
                while (i[0]+y_dr) < 8 and (i[0]+y_dr) > -1 and (i[1]+x_dr) < 8 and (i[1]+x_dr) > -1  :
                
                    stone_adj = board[i[0]+y_dr][i[1]+x_dr]
                    
                    if stone_adj == 2:
                        total_pts += score
                        break
            
                    elif stone_adj == 1:            
                        score += 1

                    else :
                        break
                
                    y_dr += row
                    x_dr += col

        #updates the position with the higher score
        if total_pts > max_pts :
            max_pts = total_pts
            best_pos = i
            
    return best_pos
        
    
    


def run_two_players() :
    gameboard = new_board()
    player = 1
    next_player = 2
    while True:
        
        print_board(gameboard)
        
        #announces if game is over
        if player == 0:
            print("GAME OVER!!")
            print(score(gameboard))
            break

        #promts user for input and check if it is valid
        ply_in = input("Player " + str(player) + "'s Choice : ")
        if len(ply_in) == 2 :
            
            ply_pos = position(ply_in.lower())
            [gameboard, next_player]  = next_state(gameboard, player, ply_pos)
            player = next_player
      
        elif ply_in.lower() == 'q' :
            print('Game Session End')
            break
        
        else :
            print("Invalid Move!")


def run_one_player():
    
    gameboard = new_board()
    player = 1
    
    while True:
        print_board(gameboard)
        
        if player == 1 :
            ply_in = input("Player " + str(player) + "'s Choice : ")
            
            if len(ply_in) == 2 :
                ply_pos = position(ply_in.lower())
                [gameboard, next_player]  = next_state(gameboard, player, ply_pos)
                player = next_player
                
            elif ply_in.lower() == 'q' :
                print('Game Session End')
                break
            
            else :
                print("Invalid Move!")
            
        elif player == 2 :
            #calls the get_pos function to get best score
            ply_pos = get_pos(gameboard)
            [gameboard, next_player]  = next_state(gameboard, player, ply_pos)
            player = next_player

        else :

            print("GAME OVER!!")
            print(score(gameboard))
            break

print("Welcome to reversi!")
usr_choice = int(input("Press 1 for Single Player, Press 2 For PvP : "))
if usr_choice == 1 : run_one_player()
else: run_two_players()




