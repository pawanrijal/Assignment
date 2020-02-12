def is_sorted(stuff):
    for i in range(len(stuff)):
        if stuff[i] > stuff[i-1]:
            return True
    else:
        return False
numbers = [5,4,3,2,1]
print(is_sorted(numbers))