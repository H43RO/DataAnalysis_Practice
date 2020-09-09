import numpy as np

# 연습문제 자료출처 : https://steemit.com/kr/@rexypark/numpy-pandas

# 1차원 배열(vector) 출력하기
# [ 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
vector = np.array(range(0, 30, 2))
vector = np.arange(0, 30, 2)
print(vector)
print()

# 2차원 배열(matrix) 출력하기
# [[10, 20, 30, 40],
# 50, 60, 70, 80]]
matrix = np.arange(10, 90, 10).reshape(2, 4)
print(matrix)
print()

# 3차원 배열(tensor) 출력하기
# [[[ 1, 2, 3],[ 4, 5, 6]],
#  [[ 7, 8, 9],[10, 11, 12]],
#  [[13, 14, 15],[16, 17, 18]],
#  [[19, 20, 21],[22, 23, 24]]]
tensor = np.arange(1, 25).reshape(4, 2, 3)
print(tensor)
print()

# 배열 값 인덱싱하기
vector = np.arange(0, 30, 2)
# 24 인덱싱하기
print(vector[12])
# 6 인덱싱하기
print(vector[3])
print()

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# 8 인덱싱하기
print(matrix[1, 3])
# 9 인덱싱하기
print(matrix[2, 0])
# 15 인덱싱하기
print(matrix[3, 2])
print()

# 배열을 이용하여 인덱싱하기
vector = np.arange(-1, -6, -1)
# [-1 -2 -3 -4 -5]
boolean_idx = [False, True, False, True, False]
print(vector[boolean_idx])
int_idx = [1, 3]
print(vector[int_idx])
