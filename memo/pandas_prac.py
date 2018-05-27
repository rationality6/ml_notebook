# from pandas import Series
from pandas import Series, DataFrame

obj = Series([1, 3, 5, 7])
# print(obj)
dic = {'first': 10000, 'second': 20000, 'third': 30000, 'forth': 40000}
obj = Series(dic)
# print(obj)

dic = {
    'state': ['Seoul', 'Busan', 'Pohang', 'Gimhae'],
    'year': [2012, 2013, 2014, 2015]
}

frame = DataFrame(dic)
print(frame)
print(frame['state'])
print(frame.ix[2])

frame['capital'] = frame['state'] == 'Seoul'
frame['2013?'] = frame['year'] == 2013
print(frame)

del frame['year']

print(frame)