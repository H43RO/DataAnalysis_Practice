import numpy as np

# 단일 객체 저장 및 불러오기
array = np.arange(0, 10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print(result)
print()

# 복수 객체 저장 및 불러오기
array1 = np.arange(0, 10)
array2 = np.arange(10, 20)
np.savez('saved.npz', array1=array1, array2=array2)

data = np.load('saved.npz')
result1 = data['array1']
result2 = data['array2']
print(result1)
print(result2)
print()

# Numpy 원소의 정렬
array = np.array([5, 9, 10, 3, 1])
array.sort()  # 오름차순
print(array)
print(array[::-1])  # 내림차순
print()

# 행렬에서의 각 열을 기준으로 정렬
array = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(array)
print()
array.sort(axis=0)
print(array)
print()

# 균일한 간격으로 데이터 생성
array = np.linspace(0, 10, 5)
print(array)
print()

# 난수의 재연 (실행마다 결과 동일)
np.random.seed(7)
print(np.random.randint(0, 10, (2, 3)))
print()

# Numpy 배열 객체 복사
array1 = np.arange(0, 10)
array2 = array1
array2[0] = 99
print(array1)  # array2가 array1과 같은 주소를 가리켜 값이 바뀌어버림
print()

array2 = array1.copy()
array2[0] = 0
print(array1)  # copy()를 사용했기 때문에 값에 영향이 없음
print()

# 중복된 원소 제거
array = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(array))
print()
