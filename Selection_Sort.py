def Selection_Sort(list):
    for element_index in range(len(list)):
        minimum_index = element_index
        for element_to_the_right_index in range(element_index + 1, len(list)):
            if list[minimum_index] > list[element_to_the_right_index]:
                minimum_index = element_to_the_right_index

        (list[element_index], list[minimum_index]) = (list[minimum_index], list[element_index]) 
    return list