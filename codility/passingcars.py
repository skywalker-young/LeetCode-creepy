def solution(A):  
    # write your code in Python 2.6  
    curZeroCnt = 0  
    totalPairs = 0  
    for value in A:  
        if value == 0:  
            curZeroCnt += 1  
        else:  
            totalPairs += curZeroCnt  
      
    if totalPairs > 1000000000:  
        return -1  
    else:  
        return totalPairs  
    pass 
