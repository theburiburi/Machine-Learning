import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#numpy -> list구조 -> array 구조 or series 구조로 바꾸는데 사용  (행렬 Transfort 하는 과정임)
#(series 는 세로로 돼있음) 그걸 이어붙여서 data frame으로 만듦
#pandas -> series -> dataframe으로 바꿔줌
# a = [1,2,3]
# b = np.array(a)
# c = pd.Series(b)

# print(type(b), type(c))
# print(b)
# print(c)

# d = pd.Series([10,20,30], index = ['a','b','c'])
# print(d)

# raw_data = {'col0':[1, 2, np.NaN, 4],
#             'col1':[5,6,7,0],
#             'col2':[10,20,30,40]}

# print(type(raw_data))
# print(raw_data['col0'])

# data = pd.DataFrame(raw_data)
# print(data)

# df = pd.DataFrame({'A': 1.,
#                    'B': pd.Timestamp('20130102'),
#                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
#                    'D': np.array([3]*4,dtype='int32'),
#                    'E': pd.Categorical(["test","train","test","train"]),
#                    'F': 'foo'})

# print(df)
# # print(df.dtypes)
# # print(df.head(2))
# # print(df.tail(2))


A = pd.DataFrame({'col':['g', 'r', 'y'], 'num':[1,2,3]})
B = pd.DataFrame({'col':['g', 'r', 'p'], 'size':['S','M','L']})
print(A)
print(B)

# inner-join
join = pd.merge(left=A, right =B, how = 'inner')
print(join)

# outer-join
join = pd.merge(left=A, right =B, how = 'outer')
print(join)