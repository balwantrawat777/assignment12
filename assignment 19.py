#QUESTION 1

import numpy as np
e=np.random.random((10,1))
c=np.mean(e)
print(c)


#QUESTION 2

import numpy as np
e=np.random.random((20,1))
dtype=np.float(64)
print((np.std(e)),(np.var(e)))


#QUESTION 3

import numpy as np
a=np.random.random((10,20))
b=np.random.random((20,25))
c=np.matmul(a,b)

print(c.reshape(10,25))
print(np.sum(c))


#QUESTION 4

import numpy as np
a=np.random.random((10,1))
b=np.empty((10,1))
for i in np.nditer(a, op_flags=['readwrite']):
    i[...]=1/(1+np.exp(-i))
print(b)

