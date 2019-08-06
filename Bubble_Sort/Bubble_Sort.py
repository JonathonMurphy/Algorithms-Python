unsortedArray = [5,6,4,4,3,2,1]
print(f"Unsorted Array: {unsortedArray}")


def bubbleSort(array):
    sortedArray = array[:] #duplicate the array to be sorted
    sortedArrayLength = len(sortedArray) # Get the length of the array
    for index in range(sortedArrayLength): # Loop through all the items in the array by their index
        for item in range(0, sortedArrayLength - index - 1):
            if sortedArray[item] > sortedArray[item + 1]:
                sortedArray[item], sortedArray[item + 1] = sortedArray[item + 1], sortedArray[item]
    return sortedArray

print(f"Sorted Array: {bubbleSort(unsortedArray)}")
