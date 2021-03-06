import math

def euclideanDistance( instance1, instance2, length ):
    distance = 0
    for x in range(length):
        distance += pow(instance1[x] - instance2[x])
    return math.sqrt(distance)
