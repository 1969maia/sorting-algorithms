def MergeSort(list):
    # Splitting the list into two halves until the size of the list becomes lesser than 1
    if len(list)>1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        MergeSort(left)
        MergeSort(right)
        # i -> index to iterate through the left sublist, j -> index to iterate through right sublist
        # k -> index used to update the elements in the list on which the MergeSort function is applied 
        i, j, k = (0,0,0)

        # Compares, one by one, the elements of the left sublist to those of the right sublist
        # The loop below ends when either sublist is traversed completely.
        while i<len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i+= 1
            else:
                list[k] = right[j]
                j+= 1
            k+=1

        # One of the loops below will be entered in order to "discard" the remaining elements.
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1
    return list