def BubbleSort(list):
    length = len(list)
    for element_index in range(length):
        swapped = False
        # Sorted elements "bubble up" to the left side of the list, we sort the remaining elements to the right
        for unsorted_element in range(0, length - element_index - 1):
            # We compare elements at consecutive indices to the right. Whenever a bigger element is encountered, a swap is made.
            if list[unsorted_element] > list[unsorted_element+1]:
                (list[unsorted_element], list[unsorted_element+1]) = (list[unsorted_element+1], list[unsorted_element])
                swapped = True
        # If no swaps have been made, the loop is exited. The list is already sorted.
        if (swapped == False):
            break
    return list