import pandas as pd
import numpy as np

# 연습문제 자료 출처 : https://steemit.com/kr/@rexypark/python-numpy-pandas-2

# 1 ~ 25 숫자를 가지는 Data Frame 만들기
s = pd.Series([np.random.randint(1, 9) for i in range(5)])
print(s)
print()

# 랜덤으로 5개의 실수를 만들어 시리즈로 생성하기
s = pd.Series([float(np.random.randint(1, 9)) for i in range(5)])
print(s)
print()

# 혈액형 통계 수치를 이용하여 인덱스를 가지는 시리즈 생성하기
blood = ['A형', 'B형', 'O형', 'AB형']
st = [34.2, 27.1, 26.7, 11.5]
s = pd.Series(st, index=blood)
print(s)
print()

# 1 ~ 25 숫자를 가지는 Data Frame 만들기 - Numpy 이용
array = np.arange(1, 26).reshape(5, 5)
s = pd.DataFrame(array)
s.columns = ['A', 'B', 'C', 'D', 'E']
s.index = ['#1', '#2', '#3', '#4', '#5']
print(s)
print()

data = [
    {'번호': 1, '이름': 'A', '점수': 100, '나이': 15},
    {'번호': 2, '이름': 'B', '점수': 60, '나이': 16},
    {'번호': 3, '이름': 'C', '점수': 80, '나이': 15},
    {'번호': 4, '이름': 'D', '점수': 90, '나이': 14},
]

df = pd.DataFrame(data)
print(df)
df = df.sort_values('점수', ascending=False)
print(df)
print()


