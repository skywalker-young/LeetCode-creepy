import numpy as np
import random
a=np.linspace(0,10,11)
a=list(a)
b=[0,1,2,3,4,5,6,7,8,9,10,11,12]
c=random.choice(a)
d=random.choice(range(0,99))

e=random.sample(b,1)
#e=[int(i) for i in e]

print (b[e[0]])
print(e)
