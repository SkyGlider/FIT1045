#ANDREW PANG
#19 MAR 2019
#TASK 6

def tpose(matrix):

    #create empty matrix
    new_matrix = []

    #runs through each column of matrix
    for i in range(len(matrix[0])):
        #empty vector
        new_rows = []

        #runs through every row of matrix
        for j in range(len(matrix)):
            new_rows.append(matrix[j][i])
            
        new_matrix.append(new_rows)

    #returns the answer   
    return new_matrix

#print(tpose( [[1,2,3],[4,5,6],[7,8,9]] ))

def multip(matrix,vector):
     
    new_vector = []
    
    for i in range(len(matrix)) :
        new_vector.append(vector[i] * sum(matrix[i]))
            
    return new_vector

#print(multip([[1,2],[3,4],[5,6]],[1,2,3]))

def nutrition(usr_list):

    #input list
    cols = ['energy','water','protein','carbs','sugars','fats','fiber']
    rows = ['apple','orange','brocoli','beef','lamb','bread']
    nutr_vals = [[229,84.3,0.4, 12.0 ,11.8,0.0,2.3],
                 [186,84.3,1,9.5,8.3,0.2,2.1],
                 [124,89.6,3.2,2.0,2.0,0.1,4.1],
                 [613,70,22.8,0.2,0.0,6.0,0.0],
                 [1057,60.2,18.6,0.0,0.0,20.2,0.0],
                 [1446,37.6,8.4,43.5,1.5,2.6,6.9]]

    #empty list answer
    ans = []

    #runs through each column of matrix
    for i in range(len(nutr_vals[0])):

        #empty vector to be fileld with multiplied answer of each column
        total = []

        #runs through each row of matrix
        for j in range(len(nutr_vals)):
            total.append(usr_list[j] * nutr_vals[j][i])
            
        ans.append(sum(total))


    return ans


#print(nutrition([1,0,0,3,2,1]))
    
        
    

