import pandas as pd
import numpy as np

# Data Frame 의 Null 여부 판단
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': np.nan,  # Not a Number (데이터 누락 상황)
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})

print(summary)
print()

print(summary.notnull())
print(summary.isnull())
print()

summary['frequency'] = summary['frequency'].fillna('Empty data')
print(summary)
print()

# Series 간의 연산
# 같은 index 에 한해서 값을 더하고, 없으면 연산을 하지않거나 Null 값을 채움
# (fill_value 를 통해 초기값 설정 가능)
array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])
array = array1.add(array2, fill_value=0)

print(array1)
print()
print(array2)
print()
print(array)
print()

# Data Frame 간의 연산
# 같은 index 에 한해서 값을 더하고, 없으면 연산을 하지않거나 Null 값을 채움
# (fill_value 를 통해 초기값 설정 가능)
array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])

array = array1.add(array2, fill_value=0)

print(array1)
print()
print(array2)
print()
print(array)
print()

# Data Frame 집계 함수 - 합계
array1 = pd.DataFrame([[1, 2], [3, 4]], index=['A', 'B'])
array2 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['B', 'C', 'D'])
array = array1.add(array2, fill_value=0)
print(array)
print("컬럼 1의 합 :", array[1].sum())  # 특정 시리즈의 합계
print()
print(array.sum())  # 전체 시리즈 각각의 합계
print()

# Data Frame 집계 함수 - 정렬
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 1,
    'Durian': 2
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1,
    'Durian': 1
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)
importance = pd.Series(importance_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency,
    'importance': importance
})
print(summary)
print()
summary = summary.sort_values('frequency', ascending=False)  # 내림차순으로 정렬
print(summary)
