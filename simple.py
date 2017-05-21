# -*- coding: utf-8 -*- 
import os

def main():
    print('Hello Word!')
    print ("this is Alic\' 阿姨")
    foo(5,10)
    print ('_' * 10)
    print ('这将直接执行'+os.getcwd())
    counter = 0
    counter += 1

    food = ['苹果','西红柿', '香蕉']
    for i in food:
        print ('我喜欢吃:'+i)


    print ("数到10")
    for i in range(10):
        print (i)

def foo(param1,secondParam):
    res = param1 + secondParam
    print ("%s 加上 %s 等于 %s"%(param1,secondParam,res))
    if res < 50:
        print ("这个")
    elif (res >= 50) and ((param1 == 42) or (secondParam == 24)):
        print ("那个")
    else:
        print ('嗯。。。。')
    return res

if __name__ == '__main__':
    main()



