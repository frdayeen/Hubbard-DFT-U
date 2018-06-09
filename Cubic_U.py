import matplotlib.pyplot as plt
import numpy as np

x1, y1 = np.loadtxt('with_cubic.txt', delimiter=',', unpack=True)
x2, y2 = np.loadtxt('without_cubic.txt', delimiter=',', unpack=True)

slope1, intercept1 = np.polyfit(x1, y1, 1)
slope2, intercept2 = np.polyfit(x2, y2, 1)
print('slope 1 =',slope1)
print('slope 2 =',slope2)
U= (1/slope2)-(1/slope1)
print('U =',U)
plt.plot(x1,y1, label='With ',marker='o')
plt.plot(x2,y2, label='Without',marker='D')
plt.show()
