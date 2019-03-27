import copy

def new_board() :
    
    zeros = [ 0, 0, 0, 0, 0, 0, 0, 0 ]
    zeros4 = [ 0, 0, 0, 2, 1, 0, 0, 0 ]
    zeros5 = [ 0, 0, 0, 1, 2, 0, 0, 0 ]
    board = [ copy.copy(zeros), copy.copy(zeros), copy.copy(zeros), zeros4, zeros5,
              copy.copy(zeros), copy.copy(zeros), copy.copy(zeros)]
    
         
    return board

def print_board(board) :
    print('0 [a, b, c, d, e, f, g, h]')
    for i in range(len(board)) :
        print(str(i+1) + " " + str(board[i]))
    print('##########################')
def score(board) :
    bl = 0
    wh = 0
    
    for i in range(len(board)) :
        for j in range(len(board[i])) :
            if board[i][j] == 1 :
                bl += 1
            elif board[i][j] == 2 :
                wh += 1

    return (bl,wh)

def enclosing(board, player, pos, direct) :

    move_validity = False
    
    if player == 1 :
        opponent = 2
    else:
        opponent = 1
    
    stone_next = board[pos[0]+direct[0]][pos[1]+direct[1]]
    
    if stone_next == opponent:
        
        y_dr = direct[0]
        x_dr = direct[1]

        while (pos[0]+y_dr) < 8 and (pos[0]+y_dr) > -1 and (pos[1]+x_dr) < 8 and (pos[1]+x_dr) > -1  :
        
            stone_adj = board[pos[0]+y_dr][pos[1]+x_dr]
            
            if stone_adj == player:
                move_validity = True
                break
            
            elif stone_adj == 0:            
                break

            y_dr += direct[0]
            x_dr += direct[1]

    return move_validity

def valid_moves(board, player):
    
    valid_list = []

    
    for row in range(8):
        for col in range(8):
            
                for v_dr in range(-1,2):
                    for h_dr in range(-1,2): 
                        if board[row][col] == 0:
                            try:
                                if enclosing(board, player, (row,col), (v_dr,h_dr)) == True :
                                    valid_list.append((row,col))
                            except:
                                continue
    return valid_list


def next_state(board, player, pos) :

     if player == 1:
          next_player = 2
     else :
          next_player = 1
          
     valid_pos = valid_moves(board,player)
     valid_pos2 = valid_moves(board,next_player)
    
     if pos in valid_pos:
        
        board[pos[0]][pos[1]] = player
       
        next_board = switch(board,player,pos)
          

     elif valid_pos == []:

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
               

def switch(board, player, pos) :

    if player == 1:
        opponent = 2
    else :
        opponent = 1
      
    for row in range (-1,2):    
        for col in range (-1,2):
            
            y_dr = row
            x_dr = col
            chg_list= []
            
            while (pos[0]+y_dr) < 8 and (pos[0]+y_dr) > -1 and (pos[1]+x_dr) < 8 and (pos[1]+x_dr) > -1  :
                
                stone_adj = board[pos[0]+y_dr][pos[1]+x_dr]
                if stone_adj == player:

                    for i in range(len(chg_list)):
                        board [chg_list[i][0]] [chg_list[i][1]] = player
                    break
            
                elif stone_adj == opponent:            
                    chg_list.append([(pos[0]+y_dr),(pos[1]+x_dr)])

                else :
                    break
                
                y_dr += row
                x_dr += col
    
    
    switched_board = board
    return switched_board

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

def get_pos(board):
    valid_pos = valid_moves(board,2)
    if valid_pos == []:
        return (0,0)
    max_pts = 0
    best_pos = None
    
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
        if player == 0:
            print("GAME OVER!!")
            print(score(gameboard))
            break
                
        ply_in = input("Player " + str(player) + "'s Choice : ")
        if len(ply_in) == 2 :
            
            ply_pos = position(ply_in)
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
                ply_pos = position(ply_in)
                [gameboard, next_player]  = next_state(gameboard, player, ply_pos)
                player = next_player
                
            elif ply_in.lower() == 'q' :
                print('Game Session End')
                break
            
            else :
                print("Invalid Move!")
            
        elif player == 2 :
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




