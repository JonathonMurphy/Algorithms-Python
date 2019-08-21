unsortedArray = [5,7,6,9,8,4,2,1,3]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        middle = len(array) / 2
        pivot = array.pop(int(middle))
        less = [i for i in array[0:] if i <= pivot]
        greater = [i for i in array[0:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

print(quickSort(unsortedArray))
