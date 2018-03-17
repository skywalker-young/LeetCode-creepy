AA=[5,-2,3,8,6]
BB=[-5, -5, -5, -42, 6, 12]
def solution(T):
    # write your code in Python 3.6
    m = max(T) - min(T)
    summer = T
    sLen = len(T)
    i = 0

    winterHigh=T[0]
    overallHigh=T[0]
    temperature=T[0]
    for j in range (sLen):

     if (temperature<=overallHigh):
        overallHigh=T[j]
        winterHigh=overallHigh
        i=i+1
     else:
        overallHigh=temperature


    return i-1
