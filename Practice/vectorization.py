import numpy as np

x = np.array([10,20,30])
w = np.array([1,2,3])

def productWithoutDot(w,x):
    n = len(x)
    ans =0
    for i in range(n):
        ans = ans + w[i]*x[i]
    return ans

def productWithDot(w,x):
    ans = np.dot(w,x)
    return ans

print(f'Without Dot product = {productWithoutDot(w,x)}')
print(f'With Dot product = {productWithDot(w,x)}')