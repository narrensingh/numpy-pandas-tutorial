import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x = np.arange(-10,11)
plt.figure(figsize=(12,6))
plt.title('My Nice Plot')
plt.subplot(1,2,1)
plt.plot(x,x**2)
plt.xlabel('X')
plt.ylabel('X squared')
plt.legend(['x^2'])


plt.subplot(1,2,2)
plt.plot(x,-x**2)
plt.xlabel('X')
plt.ylabel('minus X squared')
plt.legend(['-x^2'])

plt.show()