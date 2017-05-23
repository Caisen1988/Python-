### Python 基础知识

###### 1.列表 :Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

```
# -*- coding: utf-8 -*- 
classmates = ['Michael', 'Bob', 'Tracy']
print classmates[0]
print len(classmates)  #打印字符长度
print classmates[-1]   #最后一个元素
print classmates[-2]   #倒数第二个元素
classmates.append('Adam')  #最加元素
print classmates       
classmates.insert(2, 'Jack')  #在指定位置插入元素
print classmates
classmates.pop()              #删除最后一个元素
print classmates
classmates.pop(1)
print classmates             #删除指定位置元素
classmates[1] = 'Sarah'      #替换指定位置
print classmates
L = ['Apple', 123, True]      #list里面的元素的数据类型也可以不
s = ['python', 'java', ['asp', 'php'], 'scheme']
print len(s)
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']  #s可以看成是一个二维数组
print s[2][1]
```

###### 2.元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

```
# -*- coding: utf-8 -*- 
#另一种有序列表叫# -*- coding: utf-8 -*- 
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
t = (1)
print t
t = (1,)
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t

classmates = ('Michael', 'Bob', 'Tracy')
t = (1)
print t
t = (1,)
print t
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t

```

###### 3.循环
```
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
```