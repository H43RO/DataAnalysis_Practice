import numpy as np

array = np.random.randint(1, 10, size=4).reshape(2, 2)
print(array)

# 각 원소에 특정 값 곱하기 (반복문이 필요없는 기본 함수)
result = array * 10
print(result)
print()

# 서로 다른 형태의 배열을 동적으로 변환하여 합치기 (Broad-cast)
array1 = np.arange(4).reshape(2, 2)
print(array1)
print()

array2 = np.arange(2)
print(array2)
print()

array3 = array1 + array2  # 동적으로 array2 의 형태를 변환하여 합침
print(array3)
print()

# Broad-cast 의 다른 예
array1 = np.arange(0, 8).reshape(2, 4)
array2 = np.arange(0, 8).reshape(2, 4)
array3 = np.concatenate([array1, array2], axis=0)

print(array3)
print()

array4 = np.arange(0, 4).reshape(4, 1)

print(array4)
print()

array5 = array3 + array4
print(array5)
print()

# 각 원소에 대하여 특정 조건을 체크하는 연산도 가능 : Masking
array1 = np.arange(16).reshape(4, 4)
print(array1)
print()

array2 = array1 < 10  # Masking 연산 사용
print(array2)
print()

# Masking 연산 활용 (대상 배열에 Masking 한 배열을 대입)
array1[array2] = 100  # 조건에 부합하는 원소에만 100을 넣어주겠다
print(array1)  # 이미지 부분 픽셀 색상 변경 등의 구현에 활용가능
print()

# 배열에 대한 집계 함수들 (최대값, 최소값, 합계, 평균값 등)
array = np.arange(16).reshape(4, 4)
print("최대값 :", np.max(array))
print("최소값 :", np.min(array))
print("합 계 :", np.sum(array))
print("평균값 :", np.mean(array))
print()

# 물론, 특정 행이나 특정 열에 대한 집계도 가능하다
print(array)
print("합 계 :", np.sum(array, axis=0))  # 특정 열의 합계를 각각 계산함
