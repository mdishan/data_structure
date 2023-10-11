import numpy as np

a = int(input('Enter the size: '))
m = []


for i in range(a):
    i = int(input("Enter elements in pocket [" + str(i) + "]"))
    m.append(i)

b = np.array(m)
print(b)