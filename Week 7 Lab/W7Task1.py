#ANDREW PANG
#WEEK 7 TASK 1
#12/4/19

def is_solution(board,n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for y in range(-1,2,1):
                     for x in range(-1,2,1):
                         y_dr = y
                         x_dr = x
                         while i+y_dr < n-1 and y_dr > -1 and j+x_dr < n-1 and x_dr > -1:
                             if x == 0 and y == 0:
                                 break 
                             y_dr += y
                             x_dr += x
                             
                             if board[i+y_dr][j+x_dr] == 1:
                                 return False
    return True


print(is_solution([[0,0,0,1,0,0],
                   [1,0,0,0,0,0],
                   [0,0,0,0,1,0],
                   [0,1,0,0,0,0],
                   [0,0,0,0,0,1],
                   [0,0,1,0,0,0]],6))

    
                 
        
