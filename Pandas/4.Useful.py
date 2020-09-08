import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1, 10, (2, 2)), index=[0, 1], columns=["A", "B"])
print(df)
print()

# 컬럼 A의 각 원소가 5보다 작거나 같은지 출력
print(df["A"] <= 5)
print()

# 컬럼 A의 원소가 5보다 작고, 컬럼 B의 원소가 8보다 작은 행 출력
print(df.query("A <= 5 and B <= 8"))
print()

# Data Frame 개별 연산
# Data Frame의 apply() 를 통해 요소 각각에 대한 연산을 정의할 수 있음
df = pd.DataFrame([[1, 2, 3, 4], [1, 2, 3, 4]], index=[0, 1], columns=["A", "B", "C", "D"])
print(df)
print()

# lambda 식을 활용한 연산
df = df.apply(lambda x: x + 1)
print(df)
print()


# 사용자 정의 함수를 활용한 연산
def add_one(x):
    return x + 1


df = df.apply(add_one)
print(df)

# 특정 대상 원소에 대한 교체 연산
df = pd.DataFrame([
    ['Apple', 'Apple', 'Carrot', 'Banana'],
    ['Durian', 'Banana', 'Apple', 'Carrot']],
    index=[0, 1],
    columns=["A", "B", "C", "D"])

print(df)
print()
df = df.replace({"Apple": "Airport"})  # 'Apple' 을 'Airport'로 변경함
print(df)
print()

# Data Frame 그룹화 및 그룹 연산
df = pd.DataFrame([
    ['Apple', 7, 'Fruit'],
    ['Banana', 3, 'Fruit'],
    ['Beef', 5, 'Meal'],
    ['Kimchi', 4, 'Meal']],
    index=["A", "B", "C", "D"],
    columns=["Name", "Frequency", "Type"])
print(df)
print()
# 같은 Type 의 index 끼리 sum() 연산, Frequency 가 계산 가능한 columns
print(df.groupby(['Type']).sum())
print()

df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    index=["A", "B", "C", "D"],
    columns=["Name", "Frequency", "Importance", "Type"])
print(df)
print()
# 같은 Type 의 index 그룹의 min, max, avg 를 구함
print(df.groupby(['Type']).aggregate([min, max, np.average]))
print()


# Frequency 의 평균이 5 이상인지 여부 판단
def my_filter(data):
    return data['Frequency'].mean() >= 5


print(df)
print()
# Frequency 의 평균이 5 이상인 그룹을 출력
df = df.groupby('Type').filter(my_filter)
print(df)
print()

# 특정 그룹을 출력
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    index=["A", "B", "C", "D"],
    columns=["Name", "Frequency", "Importance", "Type"])
print(df)
print()
df = df.groupby('Type').get_group('Fruit')
print(df)
print()

# 특정 그룹의 특정 컬럼에 대하여 평균값과 얼마나 차이나는지 출력
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])

df["Gap"] = df.groupby('Type')["Frequency"].apply(lambda x: x - x.mean())
print(df)
print()

# Data Frame 다중화
df = pd.DataFrame(
    np.random.randint(1, 10, (4, 4)),
    index=[['1차', '1차', '2차', '2차'], ['공격', '수비', '공격', '수비']],
    columns=['1회', '2회', '3회', '4회']
)
print(df)
print()
# 1회 그리고 2회의 2차 값만 가져옴
print(df[["1회", "2회"]].loc["2차"])
print()

# 피벗 테이블
df = pd.DataFrame([
    ['Apple', 7, 5, 'Fruit'],
    ['Banana', 3, 6, 'Fruit'],
    ['Coconut', 2, 6, 'Fruit'],
    ['Rice', 8, 2, 'Meal'],
    ['Beef', 5, 2, 'Meal'],
    ['Kimchi', 4, 8, 'Meal']],
    columns=["Name", "Frequency", "Importance", "Type"])
print(df)
print()

# 같은 Importance 를 갖고 있으면 Frequency 를 기준으로 한다
df = df.pivot_table(
    index="Importance", columns="Type", values="Frequency",
    aggfunc=np.max
)
print(df)
