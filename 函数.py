#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
"""
1.abs()绝对值
2.max()最大值
3.int(),float(),str(),bool()类型转化.eg:bool(1),bool('')
4.可以把一个函数名赋给一个变量。类似于起别名
5.如果想定义一个什么事也不做的空函数，可以用pass语句
6.可以在参数传递时设置值
"""
import math
print(bool(''))
print(bool(10))
a = abs
print(a(-1))
def myabs(x):
    if x > 0:
        print(x)
    else:  # 注意else也有冒号
        print(-x)
    return x
print(myabs(-1))
def function1():
	pass
#返回的参数可以为多个，为tuple,见下例
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
print(move(1,2,1,)[1])
x, y = move(100, 100, 60, math.pi / 6)
print(x,y)
'''
1.必选参数在前，默认参数在后，否则Python的解释器会报错
2.eg:默认求平方，但是可以求多次
3.定义默认参数要牢记一点：默认参数必须指向不变对象！见例子。
'''
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(4,3))
print(power(4))
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
def addend(l=[]):
	l.append('end');
	return l
addend()
addend()
addend()
print(addend())
#上例解释：Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，
#默认参数的内容就变了，不再是函数定义时的[]了。应改为一下模式
def addend(l=None):
	l.append('end');
	return l
'''
1.可变参数。参数numbers接收到的是一个tuple，因此，函数代码完全不变，仅仅在参数前面加了一个*号。
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2)
calc()
nums = [1, 2, 3]#list，传的时候有list,tuple均可
calc(*nums)#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
'''
1.关键字参数，可用于注册时等。
2.可自选参数，传的是一个dict,注意此处的用法。
3.注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
'''
def person(name,age,**kw):
	print(name,age,kw)
person('Adam', 45, gender='M', job='Engineer')#注意与下面用法的区别
extra={'city':'Beijing','job':'programmer'}
person('wuchangfa',22,**extra)#注意此处的用法，**extra
'''
命名关键字参数
1.如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
2.*之后的视为命名关键字参数
3.如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
4.*之前的为位置参数，之后的命名关键字参数
5.命名关键字参数必须传入参数名，这和位置参数不同
'''
def eg_2(name, age, *, city, job):
    print(name, age, city, job)
def person_3(name, age, *args, city, job):
    print(name, age, args, city, job)
#person_3('wuchangfa',123,(1,2),fuck = 123 )city ,job此时为命名关键字
person_3('wuchangfa',123,1,2,3,2,job=12,city= 123 )#args接收到的为tuple
'''
参数组合
1.参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
2.所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''
def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)
f1(1,2,4)
f1(1,2,4,'1','2','3')
f1(1,2,4,'1','2','3',wu=12)
f2(1,2,d=0,ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1,2,3)
kw ={'d': 99,'x':'#'}
f2(*args,**kw)
"""
尾递归：在函数返回的时候，调用自身本身，并且，
return语句不能包含表达式。
这样，编译器或者解释器就可以把尾递归做优化，
使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
例如下例，自己调用自己
"""
def fact(n):
	return fact_iter(n,1);
def fact_iter(num,product):
	if num == 1:
		return product
	return fact_iter(num-1,num*product)
print(fact_iter(4,4))
print(fact(4))