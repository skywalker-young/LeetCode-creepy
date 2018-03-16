A=[0]*12
A[0] = 1
A[1] = 5
A[2] = 3
A[3] = 4
A[4] = 3
A[5] = 4
A[6] = 1
A[7] = 2
A[8] = 3
A[9] = 4
A[10] = 6
A[11] = 2

from math import sqrt


def create_peaks(A):
    N=len(A)
    peaks=[False]*N
    for i in range (1,N-1):
        if (A[i]>max(A[i-1],A[i+1])):
            peaks[i]=True
    return peaks

def checks(x,A):
    N=len(A)
    peaks=create_peaks(A)
    flags=x
    pos=0
    while (pos<N and flags > 0):
        if peaks[pos]:
            flags=flags-1
            pos=pos+x
        else:
            pos=pos+1
    return flags==0

def next_peak(A):
    N=len(A)
    peaks=create_peaks(A)
    next=[0]*N
    next[N-1]=-1
    for i in range (N-2,-1,-1):
        if peaks[i]:
            next[i]=i
        else:
            next[i]=next[i+1]
    return next

def flag (A):
    N=len(A)
    next=next_peak(A)
    i=1
    results=0
    while ( (i-1)*i<=N ):
        pos=0
        num=0
        while ( pos<N and num <i ):
            pos =next[pos]
            if (pos==-1):
                break
            num=num+1
            pos=pos+i
        results=max(results,num)
        i=i+1
    return results

print(flag(A))
