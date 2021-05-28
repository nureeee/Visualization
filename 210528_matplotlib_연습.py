import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()
plt.plot([1, 4, 9, 16])
plt.show()

a1 = np.array([1, 2, 3, 4])
a2 = np.array([1, 4, 9, 16])
plt.plot(a1, a2)


plt.plot(['a', 'b', 'c', 'd'])

a3 = ['a', 'b', 'c', 'd']
plt.figure(figsize=(4, 8))
plt.plot(a3, a2)
plt.show()

plt.plot(a3, a2, color='000000', marker ='>')
plt.plot(a3, a2, color='green', marker ='>', linestyle='dotted')
plt.plot(a3, a2, 'mp:')

x= np.arange(1, 11)
y1 = x**2
y2 =x**3
y3 = x**4
x, y1, y2, y3
plt.plot(x,y1, 'gp--', markersize=6)
plt.plot(x,y2, 'b_:', markersize=6)
plt.plot(x,y3, 'r^-', markersize=6)
plt.title('nuri')
plt.legend('green', 'blue', 'yellow')