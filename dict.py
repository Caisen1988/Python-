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