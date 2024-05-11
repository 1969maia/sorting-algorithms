import timeit
import random

# List containing the sizes of the data sets that the sorting algorithm will be applied to
data_set_sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000]

# Generator function to populate the lists to be sorted with random numbers
def generate_data_set(size):
    for number in range(size):
        yield random.randint(1, 100000)

# Function to display execution time in appropriate time units 
# The default time unit for the "timeit" function is the second
def format_execution_time(execution_time):
    if execution_time < 1:
        return f"{execution_time * 1000:.2f} milliseconds"
    elif execution_time < 60:
        return f"{execution_time:.2f} seconds"
    else:
        return f"{execution_time / 60:.2f} minutes"

algorithm = "Merge Sort"
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

# The sorting algorithm is applied to randomly generated lists of the sizes considered.
for size in data_set_sizes:
    data_set = list(generate_data_set(size))
    execution_time = timeit.timeit(lambda: MergeSort(data_set), number=1)
    formatted_time = format_execution_time(execution_time)
    print(f"Sorting a list of {size} randomly generated integers, using {algorithm}, takes {formatted_time}.")

