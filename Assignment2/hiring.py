#ANDREW PANG
#ASSIGNMENT 2

jess = (["php", "java"], 200)
clark = (["php", "c++", "go"], 1000)
john = (["lua"], 500)
cindy = (["php", "go", "word"], 240)


candidates = [ cindy, jess, clark, john ]
project = ["php", "java", "lua", "go", "c++"]

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


def sort2(element) :
    return element[1]


def best_team(skills_required,candidates):

    #re-sort by price of each candidate
    candidates = sorted(candidates,key = sort2)
    
    #calls the team of best individuals to get best team by price
    #removes expensive, excessive candidates, but still retains specialised ones 
    cheapcand = team_of_best_individuals(skills_required,candidates)
    
    #returns a list of each skill comprising of the candidates having that skill
    #eg. lua : john, go : cindy, clark
    finallist =[]
    for i in skills_required:
        y = []
        for j in cheapcand: 
            if i in j[0] :
                y.append(j)
        finallist.append(y)
        
    #sorts by number of candidates avalilable in each skill
    #the rarer the skill, the greater priority given to list
    finallist = sorted(finallist,key=len)
    
    #in finallist, the bests of bests candidates tops the list
    #those who have the most speciallised skills for cheapest price are on top
    #adds members to a new list called team
    team = []
    
    #this nested for loops adds the members to list from the top of finallist
    #if one person has more that one skill then,
    #it removes the need for hiring people of those other skills he has
    #hence those skills are removed from pending_skills
    #once all the skills are fulfilled, it returns the optimum team
    pending_skills = skills_required
    for each_lang in finallist:
        for each_person in each_lang:
            for each_skill in each_person[0]:
                if each_skill in pending_skills:
                    if not each_person in team:
                        team.append(each_person)
                    pending_skills.remove(each_skill)
                    if pending_skills == []:
                        return team
    

mcheck = uncovered(project,skills(candidates))
if not mcheck == [] :
    print("Missing skills, hire more candidates with these skills:")
    print(*mcheck)
    
else :
    print(best_team(project,candidates))


