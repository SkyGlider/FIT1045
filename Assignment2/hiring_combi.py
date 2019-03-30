#ANDREW PANG
#ASSIGNMENT 2

jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)

candidates = [jess, clark, john, cindy]
project = ["php", "java", "c++", "lua", "go"]

def cost(candidates) :
    
    cost_sum = 0
    for i in candidates:
        each_cost = i[1]
        cost_sum += each_cost

    return cost_sum



def skills(candidates) :
    
    skill_covered = []
    for i in candidates :
        for j in i[0]:
            if not j in skill_covered :  
                skill_covered.append(j)
                
    return skill_covered


def uncovered(project,skills):

    not_covered = []

    for i in project :
        if i not in skills :
            not_covered.append(i)
            
    return not_covered

def best_individual_candidate(project,candidates):
    best_price = 0
    
    for i in candidates :
        
        useful_skills = 0
        for j in i[0] :
            if j in project :
                useful_skills += 1
          
        price = useful_skills / i[1]
        
        if  price > best_price :
            best_person = candidates.index(i)
            best_price = price

    return best_person
        
    
def team_of_best_individuals(skills_required,candidates) :
    pending_skills = skills_required
    team = []
    while not pending_skills == []:
        c_index = best_individual_candidate(pending_skills,candidates)
        team.append(candidates[c_index])
        pending_skills = uncovered(pending_skills,candidates[c_index][0])
    
    return team

def team_combos(n,teamlist,combos=[]):

    
    if combos is None:
        combos = []

    if len(teamlist) == n:
        if combos.count(teamlist) == 0:
            combos.append(teamlist)
        return combos
    else:
        for i in range(len(teamlist)):
            new_list = teamlist[:i] + teamlist[i+1:]
            combos = team_combos(n,new_list,combos)
        return combos
            


def best_team(skills_required,candidates):
    for i in range(1,len(candidates)+1):
        combolist = team_combos(i,candidates)
   
    pricelist = []
    newlist =[]
    for i in combolist :
        if uncovered(skills_required,skills(i)) == [] :
            newlist.append(i)
            pricelist.append(cost(i))
    
    y = min(pricelist)
    z = pricelist.index(y)
    final = newlist[z]
    
    return final





            
    
    
     
        
        
print(best_team(project,candidates))


