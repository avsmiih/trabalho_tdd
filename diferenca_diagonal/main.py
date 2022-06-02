import numpy as np
from random import sample

num_m = [1,2,3,4,5,6,7,8,9]

m = np.array([num_m[i:i + 3]
              for i in range(0, len(num_m), 3)])

print(m)

D = np.diag(m)
d = np.fliplr(m).diagonal()

print("diagonal principal: ", D)
print("diagonal secundaria: ", d)

a = sum(D)
b = sum(d)

print("soma da diagonal principal: ", a)
print("soma da diagonal secundaria: ", b)
print("diferenca diagonal: ", abs(b - a))
