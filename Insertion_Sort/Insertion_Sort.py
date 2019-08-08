unsortedArray = [5,7,6,9,8,4,2,1,3]

def insertionSort(array):
    sortedArray = array[:]
    for index in range(1, len(sortedArray)):
        key = sortedArray[index]
        indexToTheLeft = index - 1
        while indexToTheLeft >= 0 and key < sortedArray[indexToTheLeft]:
            sortedArray[indexToTheLeft + 1] = sortedArray[indexToTheLeft]
            indexToTheLeft -= 1
        sortedArray[indexToTheLeft + 1 ] = key
    return sortedArray


print(insertionSort(unsortedArray))
