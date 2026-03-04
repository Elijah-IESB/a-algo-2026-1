# Insertion Sort Example with Python's sorted() function

## Insertion Sort Implementation

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

## Example usage

# Creating a sample list
sample_list = [12, 11, 13, 5, 6]

# Performing insertion sort
print("Original List:", sample_list)

insertion_sort(sample_list)
print("Sorted List using Insertion Sort:", sample_list)

# Using Python's built-in sorted() function
sorted_list = sorted([12, 11, 13, 5, 6])
print("Sorted List using Python's built-in sorted() function:", sorted_list)