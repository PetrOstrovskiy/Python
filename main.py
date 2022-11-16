import numpy as np
print('Задание 1.1.10')
A = np.random.randint(0, 10, 10)
n = 3
print(A)
print(A[np.argpartition(-A, n)[:n]], '\n')
