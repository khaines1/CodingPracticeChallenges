#Leetcode
#input is a 2D array boxTypes and an integer Trucksize
    #truck size  = total boxes that can be placed
    
    #output: max number of possible boxes
    #goal = put as many boxes on the truck as possible
    
    #Put smaller boxes on first, box size is 2nd column of boxTypes
        #order arrays by size
        
    #algorithm   
    #iterate through each element
        #check if truck can hold size
            #check if size is available
                #if so, add box sixe to total
                    #subtract one from number of box type
                    
    #Asume input is accurate:
def maximumUnits(boxTypes, truckSize):
    boxTypes = sorted(boxTypes, key=lambda i:i[1])
    truckLoad = 0
    totalBoxes= 0
    for i in range(0,len(boxTypes)):
        while boxTypes[i][0] > 0:
            if truckLoad + boxTypes[i][1] == truckSize:
                truckLoad += boxTypes[i][1]
                totalBoxes +=1
                boxTypes[i][0] -= 1
                return totalBoxes
            elif truckLoad + boxTypes[i][1] < truckSize:
                truckLoad += boxTypes[i][1]
                totalBoxes +=1
                boxTypes[i][0] -= 1
            elif truckLoad + boxTypes[i][1] > truckSize:
                break
    return totalBoxes

if __name__ == "__main__":
    print(maximumUnits([[1,3],[2,2],[3,1]],4))
