unsortedArray = [6,7,1.55,4,5,8,9,3,2,1,5,4,6,9,8,5,7,4,5,15,85,1551]
print(f"Unsorted Array: {unsortedArray}")


def bubbleSort(array):
    trueArray = []
    sortedArray = array[:]
    sortedArrayLength = len(sortedArray)
    for item in sortedArray:
        itemIndex = sortedArray.index(item)
        if itemIndex != sortedArrayLength - 1:
            if item > sortedArray[itemIndex + 1]:
                sortedArray.pop(itemIndex)
                sortedArray.insert(itemIndex + 1, item)
                trueArray.append(False)
    if not all(trueArray):
        bubbleSort(sortedArray)
    else:
        print(f"Sorted Array: {sortedArray}")



bubbleSort(unsortedArray)
