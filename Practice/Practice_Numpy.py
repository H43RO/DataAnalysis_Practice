import numpy as np

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
