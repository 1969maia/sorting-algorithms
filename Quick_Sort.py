def Partition(list,leftmost,rightmost):
    # Selecting the rightmost element of the list as pivot
    pivot = list[rightmost]
    # i -> indicates the element at the greatest found index that has a value lesser than the pivot's
    # Initially set to the index of the pivot
    i = leftmost - 1
    #Iterating through the elements of the list before the pivot
    for j in range(leftmost,rightmost):
        # i gets incremented when an element with a value lesser than the pivot's is found
        if list[j] <= pivot:
            i = i+1
            # First element with a greater value than the pivot's gets swapped with new found low element
            (list[i], list[j]) = (list[j], list[i])
    # First element with a greater value than that of the pivot gets swapped with the pivot
    (list[i+1],list[rightmost]) = (list[rightmost],list[i+1])
    # The index of the pivots gets returned
    return i+1

def QuickSort(list,leftmost,rightmost):
    if leftmost < rightmost:
        pivot = Partition(list,leftmost,rightmost)
        QuickSort(list,leftmost,pivot-1)
        QuickSort(list,pivot+1,rightmost)
    return list