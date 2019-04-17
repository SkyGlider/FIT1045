#ANDREW PANG YONG CHEN
#FIT1045
#WEEK 6 LAB
#TASK 1

#opens reads and puts the weight and value datas into lists
def process_file(filename):

    z = open(filename,'r')
    z = z.read()
    z = z.strip()
    z = z.split('\n')

    #initialize
    item_w = []
    item_p = []
    for i in z :
        i = i.replace('kg','')
        i = i.replace('$','')
        i = i.split(' ')
        item_w.append(float(i[0]))
        item_p.append(float(i[1]))

    return item_w, item_p

#greedy approach using weight per dollar
#item with smallest weight per dollar will be selected first
def greedy_items(values, weights, capacity):

    #initialize
    wpd = []
    for i in range(len(values)):
        wpd.append((i,weights[i]/values[i]))

    #sorts wpd values in ascending order
    wpd.sort(key = lambda x: x[1])

    #items_stolen is a list of all the selected item indexes + 1
    remaining_space = capacity
    items_stolen = []
    for i in range(len(wpd)):
        item_index = wpd[i][0]
        item_weight = weights[item_index]
        if item_weight <= remaining_space:
            items_stolen.append(item_index+1)
            remaining_space -= item_weight
            
    return items_stolen

#calls process_file, ask for capacity, calls greedy_items and prints the answer
usr_file = input('File name: ')
x,y = process_file(usr_file)
usr_in = input('Welcome to smart.theft, enter bag capacity in kg:')
usr_in = usr_in.strip(' ')
usr_in = usr_in.strip('kg')
final = greedy_items(y,x,float(usr_in))
val = 0
for i in final :
    val += y[i-1]
    print('Take item ' + str(i))
print('Total value : $' + str(val))
