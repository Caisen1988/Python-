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