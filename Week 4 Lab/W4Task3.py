#ANDREW PANG
#FIT1045
#29 MARCH 2019

def empty_graph(n):
    matrix = []
    for i in range(n) :
        newrow= []
        for j in range(n):
            newrow.append(0)
        matrix.append(newrow)

    return matrix
            
def spanning_tree(graph):
    new_matrix = empty_graph(len(graph))
        
    n = len(graph)

    for i in range(n):
        for j in range(n):
            if not i == j :
                if not graph[i][j] == 0:
                    new_matrix[i][j] = 1
                    new_matrix[j][i] = 1
                y = 0
                for k in range(n):
                    if not sum(new_matrix[k]) == 0:
                        y+=1

                if y == len(graph):
                    return new_matrix





def grid_graph(m,n):
    total_p = m*n
    new_matrix = empty_graph(total_p)
    

m = [[0,0,1,1],
     [0,0,1,1],
     [1,1,0,1],
     [1,1,1,0]]
print(spanning_tree(m))

        
                
                
    
