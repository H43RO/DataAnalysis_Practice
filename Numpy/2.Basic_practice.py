import numpy as np

array = np.arange(4)
print(array)  # 0, 1, 2, 3
print()

array = np.zeros((4,4), dtype=int)
print(array)
print()

array = np.ones((3,3), dtype=float)
print(array)
print()

array = np.random.randint(0, 10, (3, 3))
print(array)
print()

array = np.random.normal(0, 1, (3, 3))
print(array)
print()

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])
print(array3)
print()

array1 = np.arange(4).reshape(1, 4)
array2 = np.arange(4, 12).reshape(2, 4)
print(array1)
print()

print(array2)
print()

array3 = np.concatenate([array1, array2], axis=0)
print(array3)
print()

array1 = np.arange(8).reshape(2, 4)
print(array1)
print()
left, right = np.split(array1, [2], axis=1)
print(left)
print()
print(right)
print()

array1 = np.arange(16).reshape(2,8)
print(array1)
print()

left, right = np.split(array1, [3], axis=1)
print(left)
print()

print(right)
print()
