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


###### 4.dict

```
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} #如果key不存在，dict就会报错
print(d['Michael'])
#print(d['nick'])
print('Michael' in d)  #通过in判断key是否存在
print('Mich' in d)
print(d.get('Thomas'))
print(d.get('Thomas',-1)) #如果key不存在，可以返回None，或者自己指定的value


d.pop('Bob')#用pop(key)方法，对应的value也会从dict中删除
print(d)

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法

```

##### 5.set

```
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
s = set([1, 2, 3]) #要创建一个set，需要提供一个list作为输入集合：
print(s)

s = set([1, 1, 2, 2, 3, 3]) #重复元素在set中自动被过滤
print(s)

s.add(4) #通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
print(s)


s.remove(4)#通过remove(key)方法可以删除元素
print(s)

s1 = set([1, 2, 3])#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

```

##### 6.不可变的str 与可变的list

```
a = ['c', 'b', 'a']
print(a.sort())

a = 'abc'
b = a.replace('a', 'A')
print(a)
print(b)

```

##### 7.一些常用的内置函数

```
abs()
max()

```

##### 8.切片

```
r = ['Michael', 'Sarah', 'Tracy']
print(L[0:3])
t = (0, 1, 2, 3, 4, 5)
print(t[:3])
```

##### 9.迭代

```
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
```

##### 10.生成器
创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generato
可以直接打印出list的每一个元素,可以通过next()函数获得generator的下一个返回值
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
```
# -*- coding: utf-8 -*-
g = (x * x for x in range(10))
for n in g:
  print(n)


def fib(max):
   n, a, b = 0, 0, 1
   while n < max:
       print(b)
       a, b = b, a + b
       n = n + 1
   return 'done'


fib(6)

def odd():
   print('step 1')
   yield 1
   print('step 2')
   yield(3)
   print('step 3')
   yield(5)

o = odd()
next(o)
next(o)


# -*- coding: utf-8 -*-

def triangles():
   L=[1]
   while True:
       yield(L)
       L.append(0)
       L = [L[n - 1] + L[n] for n in range(len(L))]
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
   print(t)
   n = n + 1
   if n == 10:
       break


```
