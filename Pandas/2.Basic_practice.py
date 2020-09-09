import pandas as pd
import numpy as np

array = pd.Series(['사과', '바나나', '당근'], index=['a', 'b', 'c'])
print(array)

data = {
    'a': '사과',
    'b': '바나나',
    'c': '당근'
}

array = pd.Series(data)
print(array)
print(array['a'])

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
summary['score'] = score

print(summary)

