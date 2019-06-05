
def insert(value,tree,label,v,parent = 0):

    if v is None:
        label.append(value)
        parent_index = label.index(parent)
        if parent > value:
            tree[parent_index] = (value,tree[parent_index][1])
        else:
            tree[parent_index] = (tree[parent_index][0],value)
        tree.append((None,None))
        return tree
    
     
    left, right = tree[label.index(v)]
    if v>value:
        return insert(value,tree,label,left,v)
    else:
        return insert(value,tree,label,right,v)
            

tree = [(3,12),(2,4),(11,13),(None,None),(None,None),(None,None),(None,None)]
label = [5,3,12,2,4,11,13]
print(insert(20,tree,label,label[0]))
                                
