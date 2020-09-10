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
print()

# 5 * 6 행렬 만든 후 조건에 맞는 코드 작성
matrix = np.arange(1, 31).reshape(5, 6)
print(matrix)
# 데이터 최대값 구하기
print(np.max(matrix))
# 각 행의 합계 구하기
print(np.sum(matrix, axis=1))
# 각 열의 합계 구하기
print(np.sum(matrix, axis=0))
# 각 열의 평균 구하기
print(np.mean(matrix, axis=0))
print()

# 각 행에 새로운 데이터 삽입하기
matrix = np.arange(1, 7).reshape(2, 3)
new = np.array([[10, 20]])
print(matrix)
print()

# transpose() 메소드 또는 T 속성을 이용하여 전치행렬 출력 가능
# 다만 transpose() 는 T 속성과 다르게 축을 바꾸고 싶은 위치 등을 지정할 수 있음
result = np.concatenate((matrix, new.transpose()), axis=1)
result = np.concatenate((matrix, new.T), axis=1)
print(result)
print()

# 연습문제 자료출처 : https://leechamin.tistory.com/30

z = np.zeros(10)
print(z)

z = np.zeros((10, 10))
print("%d bytes" % (z.size * z.itemsize))

z = [1, 2, 0, 0, 4, 0]
print(np.nonzero(z))

z = np.eye(10, 10)
print(z)

z = np.random.random((3,3,3))
print(z)

z = np.random.randint(0, 10, (3, 3))
print(z)