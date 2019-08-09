sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9] # Length of 9

def binarySearch(array, item):
    low = 0
    high = len(array) -1
    while low <= high:
        middle = (low + high) / 2
        guess = array[int(middle)]
        if guess == item:
            return guess
        elif guess > item:
            high = middle -1
        else:
            low = middle + 1
    return None

print(binarySearch(sortedArray, 8))
