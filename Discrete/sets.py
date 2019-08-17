import numpy as np
import matplotlib.pyplot as plt

n=20
a = np.zeros([n,n])
for i in range(0, n):
    for j in range(0, n):
        if (j**2+i**2)%3==0:
            a[i,j] = 1
print(a)
plt.imshow(a)
plt.show()
