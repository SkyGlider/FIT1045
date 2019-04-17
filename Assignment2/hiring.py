#ANDREW PANG YONG CHEN (30506271)
#FIT1045
#ASSIGNMENT 2 TASK 1 - HIRING
#STARTED: APRIL 2019
#COMPLETED: APRIL 2019
#SUBMITTTED:

#datum
jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)
candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua", "go"]


#run through candidate list and sum their costs
def cost(candidates) :
    
    cost_sum = 0
    for i in candidates:
        each_cost = i[1]
        cost_sum += each_cost

    return cost_sum


#runs through candidate list and get the list of skills 
def skills(candidates) :
    
    skill_covered = []
    for i in candidates :
        for j in i[0]:
            if not j in skill_covered :  
                skill_covered.append(j)
                
    return skill_covered


#compares skills required by project and input list of skils
#if needed skill not in list of skills, appends to not_covered
def uncovered(project,skills):

    not_covered = []

    for i in project :
        if i not in skills :
            not_covered.append(i)
            
    return not_covered


#finds the candidate in the input list with the best skills per dollar ratio
def best_individual_candidate(project,candidates):
    
    best_price = 0
    
    for i in candidates :

        #counts the number of useful skills for each person
        #(skills required for project)
        useful_skills = 0
        for j in i[0] :
            if j in project :
                useful_skills += 1

        #calculates the skills per dollar
        price = useful_skills / i[1]

        #gets the person with the largest spd ratio
        if  price > best_price :
            best_person = candidates.index(i)
            best_price = price

    return best_person
        

#finds the team of best indiidual based on the largest spd
def team_of_best_individuals(skills_required,candidates) :
    
    pending_skills = skills_required
    team = []
    
    #take in candidates using greedy approach (largest spd first)
    while not pending_skills == []:
        
        c_index = best_individual_candidate(pending_skills,candidates)
        team.append(candidates[c_index])
        pending_skills = uncovered(pending_skills,candidates[c_index][0])
    
    return team


#ADDITIONAL FUNCTION
#NOTE: the function get_combi and lex_suc are from the lecture slides
#Adapted to suit the needs of this assignment
def get_combi(candidates):

    #initialize a bitlist of zeroes(start) and ones(end)
    n = len(candidates)
    first = n*[0]
    last = n*[1]
    res = [first]
    
    #loops until the last element in res is ones(end)
    while res[-1] != last:
        res += [lex_suc(res[-1])]

    all_combi = []
    #gets the list of all possible combinations of candidates except null
    for i in res:

        #using the bitlist, if value 1, the candidate in that index is added
        each_combi = []
        for j in range(len(i)) :
            if i[j] == 1:
                each_combi.append(candidates[j])
        if each_combi != [] :
            all_combi.append(each_combi)
        
    return all_combi


#ADDITIONAL FUNCTION
#Note: Taken from lecture slides
def lex_suc(bitlst):
    res = bitlst[:]
    i = len(res) - 1
    
    while res[i] == 1:
        res[i] = 0
        i -= 1

    res[i] = 1
    
    return res


#Brute force apporach to find optimal answer

def best_team(skills_required,candidates):

    #gets the cost of all possible combinations of candidates
    #checks for feasibiity of each combination
    combi_list = get_combi(candidates)
    feasible_list = []
    for i in combi_list:
        if uncovered(project,skills(i)) == []:
            feasible_list.append(i)

    #compares the costs of all feasible combinations, note minimum
    min_cost = cost(feasible_list[0])
    final = feasible_list[0]
    for j in feasible_list:
        if cost(j) < min_cost:
            min_cost = cost(j)
            final = j
            
    return final

#Execute 
print(best_team(project,candidates))


