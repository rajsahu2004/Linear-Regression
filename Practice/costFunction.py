import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = 2*x+3
w, b = 0, 0


def costFunction(x, y, w, b):
    length = len(x)
    cost = (1/2*length)*(sum(w*x+b-y))**2
    return cost


extend = 50
bTest = np.arange(-extend, extend)
wTest = np.arange(-extend, extend)
costArray = np.array([])
count = 0
for btest in bTest:
    for wtest in wTest:
        cost = costFunction(x, y, wtest, btest)
        costArray = np.append(costArray, cost)
        print(count, cost)
        count = count+1
size = len(bTest)
costArray = np.reshape(costArray, (size, size))
plt.contourf(bTest, wTest, costArray)
plt.show()
