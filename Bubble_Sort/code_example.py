def bubbleSort(array):
    arrayLength = len(array)

    # Traverse through all array elements
    for index in range(arrayLength):

        # Last i elements are already in place
        for j in range(0, arrayLength - index - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 22, 11, 90] # length of 8

bubbleSort(arr)

print (f"Sorted array is: {arr}")
