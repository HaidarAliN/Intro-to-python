#Boiling Point
def boiling_material(boiling_map, boiling_point):
    for i in boiling_map:
        if boiling_point < 0:
            if boiling_point >= (boiling_map[i] + boiling_map[i]*0.05) and boiling_point <= (boiling_map[i] - boiling_map[i]*0.05) :
                return i
        else:
            if boiling_point <= (boiling_map[i] + boiling_map[i]*0.05) and boiling_point >= (boiling_map[i] - boiling_map[i]*0.05) :
                return i
    return 'Unknown'

#Cycles
def cycles(indices):
    lst=[]
    cycle = []
    flag = True
    for i in range(len(indices)):
        flag = True
        for item in lst:
            if i in item:
                flag = False
                break
        counter = i
        cycle=[]
        while flag:
            counter = indices[counter]
            if counter not in cycle:
                cycle.append(counter)
            else:
                lst.append(cycle)
                break  
    return lst

