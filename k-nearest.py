"""given array of points, arr, and an iteger, k, find the k nearest
    points to [0,0].

    input - array(list of resturaunts points)
            integer k-closest points
    output - array of k-closest points

    algorithm
    loop through array and find x^2 - y^2
        add values to dictionary
    sort values in ascending order
    select first k values
 """
import math
arr=[[1,2],[3,4],[1,-1]]
def nearest(arr,k):
    result = []
    distanceDict = {}
    for i in arr:
        diff = (i[0]**2) + (i[1]**2)
        distanceDict[i[0],i[1]] = diff
    
    orderedDist = sorted(distanceDict.items(), key = lambda d: d[1])
    [result.append(orderedDist[i][0]) for i in range(k)]
    return result
print(nearest(arr,3))

