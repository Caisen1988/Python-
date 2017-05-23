# -*- coding: utf-8 -*- 

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


m = list(range(5))  #range()函数，可以生成一个整数序列
print(m)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:  #while循环，只要条件满足，就不断循环，条件不满足时退出循环。比如我们要计算100以内所有奇数之和
    sum = sum + n
    n = n - 2
print(sum)