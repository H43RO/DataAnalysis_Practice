import numpy as np

arr = np.arange(4)
print(arr)

arr = np.arange(9).reshape(3, 3)
print(arr)
print()

arr1 = np.array([1, 2, 3])
arr2 = np.arange(4, 7)
result = np.concatenate([arr1, arr2])
print(result)
print()

arr1 = np.arange(4).reshape(1, 4)
arr2 = np.arange(4, 8).reshape(1, 4)
result = np.concatenate([arr1, arr2], axis=0)
print(result)


