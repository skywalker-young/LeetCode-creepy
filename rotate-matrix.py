class Solution:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
        
        
class Solution:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
   m=eval(input())  
ans=[]  
try:  
           while True:  
                      ans+=m.pop(0)  
                      for l in m:  
                                 ans.append(l.pop())    '''''将每一行的最后一个元素加到列表里'''  
                      ans+=m.pop()[::-1]                '''''将最后一行反转后加入列表'''   
                      for l in m[::-1]:                  '''''将剩余的行反转，将每一行的第一个加入'''    
                                 ans.append(l.pop(0))  
except:  
           print(ans) 
