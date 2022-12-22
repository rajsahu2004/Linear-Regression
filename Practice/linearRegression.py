import numpy as np
import matplotlib.pyplot as plt

def gradientDescent(x,y):
    '''
    Gradient Descent method to do Linear Regression.
    # <arguments>
    `x` : (array)
    `y` : (array)
    '''
    plt.scatter(x,y,c='r')
    w,b=0,0
    m=len(x)
    assert len(x) == len(y)
    alpha,iterations = 1e-1,1000
    for i in range(iterations):
        dw = (1/m)*np.sum((w*x+b-y)*x)
        db = (1/m)*np.sum(w*x+b-y)
        w = w-alpha*dw
        b = b-alpha*db
    plt.plot(x,x*w+b)
    plt.show()
gradientDescent(np.array([1,2,3,4,5]),np.array([1,3,2,5,6]))
