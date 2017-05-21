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