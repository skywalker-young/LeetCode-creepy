import random 
def solution(A):
    # write your code in Python 3.6
    a=len(A) #a-1
    b=[]
    
    
   # for index,item in enumerate (A):
   #     b.append(index)
    P=a-1
    c=[0]*P
    for i in range (1,P+1):
        c[i-1]=abs(sum(A[:i])-sum(A[i:P+1]))
    
    return min(c)
    
    #问题核心是A[:i],左闭右开
