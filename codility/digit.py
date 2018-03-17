#c=1529
def solution(A, B):
    # write your code in Python 3.6
    if (A < 0 or A > 100000000):
        return -1
    if (B < 0 or B > 100000000):
        return -1
    a = str(A)
    b = str(B)
    aLen = len(a)
    bLen = len(b)
    C = "".join([x + y for (x, y) in zip(a, b)]) + a[min(aLen, bLen):] + b[min(aLen, bLen):]
    C = int(C)

    if (C > 100000000):
        return -1
    else:
        return C
