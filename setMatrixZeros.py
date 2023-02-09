#Leetcode
#if there is a zero in row or column, change all of row or column to zeros
    #input = array
    #output = array

    #structures
        #rowZeros[]
        #columnZeros[]
    #functions
        #zeroRows(rowZeros)
        #zeroCols(columnZeros)
    #algoritm
        #iterate though each row, check for 0, add index to rowZeros
            #do the same for each column 
        #run zero functions after loop ends
        
    #Assume input is valid
    
def zeroRow(matrix, rowZeros):
    #change whole row to zero
    print(matrix[1])
    for i in range(len(rowZeros)):
        if rowZeros[i] == True:
            for j in range(len(matrix)):
                matrix[i][j]= 0
    return matrix

def zeroColumn(matrix, columnZeros):
    #change whole column to zero
    for i in range(len(columnZeros)):
        if columnZeros[i] == True:
            for j in range(len(matrix)):
                matrix[j][i] = 0
    return matrix
    
def set_matrix_zeros(matrix):
    print(matrix)
    #make sure new lists are same size as input list
    size = len(matrix[0])
    rowZeros=[False]* size
    columnZeros=[False]*size
    #find rows and columns with zeros
    for i in range(0,len(matrix)):
        if matrix[i] == 0:
                rowZeros[i]= True
        for j in range(0,len(matrix[i])):
            if matrix[i][j] == 0:
                columnZeros[j] = True
                rowZeros[j] = True
    print(rowZeros)
    print(columnZeros)
    
    #zero appropriate rows and columns
    zeroRow(matrix, rowZeros)
    zeroColumn(matrix, columnZeros)
    return matrix

if __name__ == "__main__":
    print(set_matrix_zeros([[1,1,1],[1,0,1],[1,1,1]]))
