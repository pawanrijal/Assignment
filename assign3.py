def remove_duplicates(List):
    newList = []
    for item in List:
        if item not in newList:
            newList.append(item)
    return newList

print(remove_duplicates([1,2,3,3,3,3,4,5])) 
