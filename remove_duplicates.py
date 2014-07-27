#a function that takes in  a list and removes any duplicates
def remove_duplicates(alist):
    #we'll return the shrunken list as a new one
    nodupes = []
    #if element in alist is already not in new list, add element to newlist
    for i in range(len(alist)):
        if alist[i] not in nodupes:
            nodupes.append(alist[i])
    return nodupes
