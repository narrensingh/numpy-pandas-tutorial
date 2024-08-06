import matplotlib.pyplot as plt
import numpy as np
# object oriented approach
x= np.arange(-10,11)
plotobjects= plt.subplots(nrows=2,ncols=2,figsize=(14,6))
fig , ((ax1,ax2),(ax3,ax4)) = plotobjects
ax1.plot(x,x**2 , '--b',marker='o')
ax2.plot(np.random.randn(50),'--r')
ax3.plot(x,x**4 ,'--y')
ax4.hist(np.random.rand(1000),bins=100)
plt.show()