def InsertionSort(list):
    for compared_element_index in range(1,len(list)):
        key = list[compared_element_index]
        element_compared_against_index = compared_element_index - 1
        # Key gets compared to its predecessors and gets swapped as long as it encounters predessor with greater values.
        while element_compared_against_index >=0 and key < list[element_compared_against_index]:
            # Element at key's index gets the value of the greater element encountered.
            list[element_compared_against_index + 1] = list[element_compared_against_index]
            element_compared_against_index -= 1
        # Sorted sublist gets built to the left. First unsorted element becomes the new key.
        list[element_compared_against_index + 1] = key
    return list