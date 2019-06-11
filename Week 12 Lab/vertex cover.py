


def isVertexCover(vertices,graph):
   
    for i in range(len(graph)):
        for j in range(i+1,len(graph)):
            if graph[i][j] == 1 :
                if not (i in vertices or j in vertices) :
                    return False
                
    return True
    

grh  = [[0,1,0,0],
        [1,0,1,0],
        [0,1,0,1],
        [0,0,1,0]]

vert = [1,2]

print(isVertexCover(vert,grh))



    
