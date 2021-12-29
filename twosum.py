def twosum(listA, x):
    if len(listA) < 2:
        print("Could not find elements in list that sum to", x)
        return
    try:
        small = listA[0]
        large = listA[-1]
    except:
        print("Could not find elements in list that sum to", x)
        return
    if small + large == x:
        return [small, large]
    elif small + large > x:
        listA.pop(-1)
        return twosum(listA, x)
    else:
        listA.pop(0)
        return twosum(listA, x)
        
