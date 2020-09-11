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

z = np.random.random((3, 3, 3))
print(z)

z = np.random.randint(0, 10, (3, 3))
print(z)

z = np.ones((10, 10))
z[1:-1, 1:-1] = 0
print(z)
print()

z = np.ones((5, 5))
z = np.pad(z, pad_width=1, mode='constant', constant_values=0)
print(z)
print()

# 대각 행렬 diag() 를 구현할 때, k 특성은 시작점을 바꿔줄 수 있다. (k=-1 등)
z = np.diag(np.arange(1, 5), k=0)
print(z)
print()

# 체크보드 패턴
'''
z[A::B] 는 A 인덱스로부터 B만큼 건너뛰면서 Slicing 한다.
따라서 [1::2, ::2]는 0행을 건너뛰고 1행부터 step size 2만큼 Slicing 한다.
그리고 동시에 0열부터 step size 2만큼을 갖고 Slicing 한다.
'''
z = np.zeros((8, 8))
z[1::2, ::2] = 1
z[::2, 1::2] = 1
print(z)
print()

# tile() 을 활용한 체크보드 패턴
z = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))
print(z)
print()

# (6, 7, 8) 모양의 Tensor 에서, 100번째 요소의 값은?
'''
np.unravel_index(indices, dims, order='C')
-> "플랫 인덱스 또는 플랫 인덱스 배열을 좌표 배열의 튜플로 변환한다."
-> C = 행 주요 / F = 열 주요
'''
z = np.unravel_index(100, (6, 7, 8))
print(z)
print()

# 표준 정규 분포
z = np.random.normal(0, 1, (5, 5))
print(z)
print()

# 표준 정규 분포를 나타내는 다른 방법
# (5, 5) 랜덤 행렬을 만들고 Normalize 공식을 이용
x = np.random.random((5, 5))
normalize = (x - np.mean(x)) / np.std(x)
print(normalize)
print()

# 5 * 3 행렬과 3 * 2 행렬 곱하기
A = np.random.randint(1, 20, (5, 3))
B = np.random.randint(1, 20, (3, 2))
print(A @ B)
print()

z = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print(z)
print()

# 배열의 특정 범위 내 요소에 마스킹 작업 하기
z = np.arange(11)
z[(3 < z) & (z < 8)] *= -1
print(z)
print()

# 두 배열 간 공통 요소 출력하기
A = np.random.randint(0, 10, 10)
B = np.random.randint(0, 10, 10)
print(A, B)
print(np.intersect1d(A, B))
