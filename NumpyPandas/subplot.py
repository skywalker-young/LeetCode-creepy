

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd






a=np.linspace(0,100,100)
b=np.random.normal(0,1,100)
ax=plt.subplot(2,1,1)  #这个图画在第一行

ax.plot(a,label='a')
plt.subplots_adjust(top=None,bottom=None)
ax2=plt.subplot(2,1,2)  #这个图画在第二行
plt.plot(b,label='b')

plt.subplots_adjust(   wspace=None, hspace=0)
plt.grid(True)
plt.legend()
plt.show()
##http://www.cnblogs.com/darkknightzh/p/6117528.html
##
##一些不同颜色和线条组成的选择
