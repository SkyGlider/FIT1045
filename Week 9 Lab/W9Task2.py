#ANDREW PANG
#30506271
#FIT1045
#WEEK 9 TASK 2
#RECURSION + BACKTRACKING
#note: some functions adapted from hamiltonian cycle


#finds the connected neighbours for specific node
#utilizes the adjacency matrix and returns a list of connected neighbours
def getNeighbours(M,u):
    
    nlist = []
    for i in range(len(M)):
        if M[u][i] == 1:
            nlist.append(i)
            
    return nlist


#this is a recursive functions from slides
#with addition parameters of u and v
#first check if the partial solution is complete, exits the recursion if yes
#orelse creates a new augmented solution, and repeats the process vis recursion
def solutions(completed,options,u,v,partial):
    
    if completed(partial,v):
        return [partial]
    else:
        res = []
        for o in options(partial,u):
            augmented = partial+ [o]
            res += solutions(completed,options,u,v,augmented)
        return res


def get_paths(M,u,v):

    #function to check if it is complete
    def completed(part,v):
        return part[-1] == v
    
    #gets all the neighbours and add the neighbours to the current path
    #giving the path(s) of next step
    def options(part,u):
        res = []
        path = [u] + part
        for k in getNeighbours(M,path[-1]):
            if not k in path:
                res += [k]
        return res

    return solutions(completed,options,u,v,[u])

#Execute
print(get_paths([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]],0,3))

    

    

    
