def best_sum3(target, items, memo):
    if target in memo.keys():
        return memo[target].copy()
    if target<0:
        return None
    if target==0:
        return []
    best_item = 0
    min_length = -1
    for i in items:
        out = best_sum3(target-i,items,memo)
        if(out!=None):
            if((len(out)<min_length) or (min_length==-1)):
                min_length = len(out)
                best_item = i
                best_out = out.copy()
    if min_length!=-1:
        best_out.append(best_item)
        memo[target] = best_out
        return memo[target]
    else:
        return None

def best_sum2(target, items):
    if target<0:
        return None
    if target==0:
        return []
    best_item = 0
    min_length = -1
    for i in items:
        out = best_sum2(target-i,items)
        if(out!=None):
            if((len(out)<min_length) or (min_length==-1)):
                min_length = len(out)
                best_item = i
                best_out = out
    if min_length!=-1:
        best_out.append(best_item)
        return best_out
    else:
        return None

def best_sum(target,items, path):
    if target < 0:
        return []
    if target==0:
        return path
    master_list = []
    size = 0
    index_size=0
    for i in range(len(items)):
        temp = list(path)
        temp.append(items[i])
        master_list.append(best_sum(target-items[i],items,temp))
        if ((len(master_list[i])>0) and (len(master_list[i]) <size) or (size==0)):
            size = len(master_list[i])
            index_size = i
    return master_list[index_size]


z=best_sum3(55,[7,5,1],{})
print(z)

z=best_sum2(55,[7,5,1])
print(z)


