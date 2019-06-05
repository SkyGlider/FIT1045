import itertools

#write your code here
def is_clique(S, G):

        #goes thru every value in S
        for i in range(len(S)):

                #empty vector conn
                conn = []
                
                #goes thru each connection in each node in S
                for j in range(len(G[S[i]])):

                        #if 1 and the node is in S then append to conn
                        if G[S[i]][j] == 1 and j in S:
                                conn.append(j)

                #true if conn length < S length -1
                if len(conn) < len(S)-1:
                        return False
                
        return True


def is_indset(S, G):
        
	#goes thru every value in S
        for i in range(len(S)):

                #empty vector conn
                noconn = []
                
                #goes thru each connection in each node in S
                for j in range(len(G[S[i]])):

                        #if 0 (no connection) and the node is in S then append to conn
                        if G[S[i]][j] == 0 and j in S:
                                noconn.append(j)

                #true if conn length < S length -1
                if len(noconn) < len(S)-1:
                        return False     
        return True


def complement(G):
        
        #Runs thru every node
        for i in range(len(G)):
                #gets connection status with every otehr node
                for j in range(len(G[i])):
                        #Swaps
                        if G[i][j] == 0:
                                G[i][j] = 1
                        else:
                                G[i][j] = 0
        return G


def get_clique(G,k):

        #gets every node
        nodes = list(range(len(G)))
        #get all possible node conifguration subsets with size k
        all_combi = list(itertools.combinations(nodes,k))
        
        #checks if subset is feasible and is a clique
        for i in all_combi:
                if is_clique(list(i),G):
                        return list(i)

        #by default no subset found
        return False


def get_largest(G):

        #gets every node
        nodes = list(range(len(G)))

        #goes from largest possible clique size to smallest
        for k in range(len(G)-1,0,-1):

                #same as above
                all_combi = list(itertools.combinations(nodes,k))
                for i in all_combi:
                        if is_clique(list(i),G):
                                return list(i)
        return False

        
andrew_graph = [[0, 1, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 1, 1, 1, 0],
		[0, 1, 1, 0, 1, 1, 0],
		[0, 0, 1, 1, 0, 1, 1],
		[0, 0, 1, 1, 1, 0, 1],
		[0, 0, 0, 0, 1, 1, 0]]

another_graph= [[1, 0, 1, 1, 1, 1, 1],
		[0, 1, 0, 0, 1, 1, 1],
		[1, 0, 1, 0, 0, 0, 1],
		[1, 0, 0, 1, 0, 0, 1],
		[1, 1, 0, 0, 1, 0, 0],
		[1, 1, 0, 0, 0, 1, 0],
		[1, 1, 1, 1, 0, 0, 1]]


#print(is_indset([1,3,5],andrew_graph))
#print(complement(andrew_graph) == another_graph)
#print(get_largest(andrew_graph))

