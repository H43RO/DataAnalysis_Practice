import numpy as np

# arange(n) : n 만큼의 1차원 배열 생성
# arange(n, m) : n ~ m 만큼의 1차원 배열 생성
array1 = np.arange(4)
print(array1)

# zeros(shape, dtype) : dtype 으로 이루어진 0으로 shape 형태로 행렬 생성
array2 = np.zeros((4, 4), dtype=float)
print(array2)

# ones(shape, dtype) : dtype 으로 이루어진 1으로 shape 형태로 행렬 생성
array3 = np.ones((3, 3), dtype=str)
print(array2)

# random.randint(min, max, shape) : min~max 사이 값으로 채운 shape 형태의 행렬 생성
array4 = np.random.randint(0, 10, (3, 3))
print(array4)

# 표준 정규 분포
array5 = np.random.normal(0, 1, (3, 3))
print(array5)

# concatenate([array, array, ...]) : 여러 개의 배열을 합침
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate([arr1, arr2])
print(arr3.shape)
print(arr3)

# reshape(shape) : 자료의 형태를 바꿈 ex) 배열 -> 행렬
arr1 = np.array([1, 2, 3, 4])
arr2 = arr1.reshape((2, 2))
print(arr2)

# reshape()의 활용 형태
arr1 = np.arange(4).reshape(1, 4)
arr2 = np.arange(8).reshape(2, 4)
print(arr1)
print(arr2)

# concatenate([array, array, ...], axis) : axis 를 기준으로 배열을 합침
arr3 = np.concatenate([arr1, arr2], axis=0)  # axis 0 : 행 (세로로 합친다는 뜻)
print(arr3)

# split(array, standard, axis)vector 나누기
arr1 = np.arange(8).reshape(2, 4)
print(arr1)
left, right = np.split(arr1, [2], axis=1)  # axis 1 : 열 (가로로 쪼갠다는 뜻)
print(left.shape)
print(right.shape)
print(left)
print(right)
