import pandas as pd
import numpy as np

# 연습문제 자료 출처 : https://steemit.com/kr/@rexypark/python-numpy-pandas-2

# 1 ~ 25 숫자를 가지는 Data Frame 만들기
s = pd.Series([np.random.randint(1, 9) for i in range(5)])
print(s)
print()

