x = 250
y = 50

def euclidsAlgorithm(x,y):
    if y == 0:
        return x
    else:
        return euclidsAlgorithm(y, x % y)

print(euclidsAlgorithm(x,y))
