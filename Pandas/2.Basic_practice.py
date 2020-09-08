import pandas as pd
import numpy as np

array = pd.Series(['사과', '바나나', '당근'], index = ['a','b','c'])
print(array)

data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근'
}

array = pd.Series(data)
print(array)
print(array['a'])
