import numpy as np

a=bin(1041)[2:]

c=a.split('1')

d=max([len(i) for i in c])

print(d)


