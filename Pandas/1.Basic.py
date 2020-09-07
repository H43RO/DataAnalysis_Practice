import pandas as pd

# Pandas 에서는 Dict 형태의 자료형을 Series 라고 정의함 ('index' 라는 Key 값을 가짐)
array = pd.Series(['사과', '바나나', '당근'], index=['a', 'b', 'c'])

print(array)
print()
print(array['a'])  # index 로 원소 접근 가능
print()

# Series 는 다음과 같이 기존의 Dict 를 통해서 생성할 수도 있음
data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근'
}

array = pd.Series(data)
print(array['a'])  # index 로 원소 접근 가능
print()

# Data Frame : 다수의 Series 를 모아 처리하기 위한 자료형 (엑셀의 표 형태)
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

word = pd.Series(word_dict)
frequency = pd.Series(frequency_dict)

summary = pd.DataFrame({
    'word': word,
    'frequency': frequency
})

print(summary)
print()

# Series 연산 : 다수의 시리즈를 서로 연산하여 새로운 시리즈를 만들 수 있음

word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7
}

importance_dict = {
    'Apple': 3,
    'Banana': 2,
    'Carrot': 1
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

score = summary['frequency'] * summary['importance']
summary['score'] = score  # 일련 Series 간 연산을 통해 'score'라는 Series 생성

print(summary)
print()

# Data Frame 의 슬라이싱
word_dict = {
    'Apple': '사과',
    'Banana': '바나나',
    'Carrot': '당근',
    'Durian': '두리안'
}

frequency_dict = {
    'Apple': 3,
    'Banana': 5,
    'Carrot': 7,
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

print(summary.loc['Banana': 'Carrot', 'importance'])  # 이름 기준으로 슬라이싱
print()

print(summary.iloc[1:3, 2:])  # 인덱스 기준으로 슬라이싱
print()

# 데이터의 변경 및 삽입도 가능
summary.loc['Apple', 'importance'] = 5  # 데이터 변경
summary.loc['Elderberry'] = ['엘더베리', 5, 3]  # 데이터 삽입
print(summary)
print()

# Excel 로 데이터 내보내기 / 불러오기
summary.to_csv("summary.csv", encoding="utf-8-sig")
saved = pd.read_csv("summary.csv", index_col=0)

