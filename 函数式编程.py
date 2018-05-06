#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
'''
1.函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，***任意一个函数，只要输入是确定的，输出就是确定的*，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
2.函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
3.Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''
"""
1.传入函数.既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
"""
def add(x,y,f):
	return(f(x)+f(y))
print(add(-5,2,abs))
"""
map/reduce
1.map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次***作用到序列的每个元素，并把结果作为新的Iterator返回。
"""
def f(x):
	return(x*x)
r= map(f,[1,2,3,4,5])
print(list(r)) # 因此通过list()函数让它把整个序列都计算出来并返回一个list。
#变成整数
def fn(x,y):
	return x*10+y
from functools import reduce
#print(reduce(add1,[1,2,3]))
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
print(reduce(fn,map(char2num,'111')))#利用mapdeduce.先单个处理成数字。在利用reduce合并成数字
print('111')
def str2int(s):#字符串转化成整数的代码。
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))#注lambda函数
print(str2int('11'))
"""
2.Python内建的filter()函数用于过滤序列。
和map()类似，filter()也接收一个函数和一个序列。
和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
"""
def is_odd(n):
    return n % 2 == 1
print (list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
def not_empty(s):
    return s and s.strip()#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格)
print(list(filter(not_empty,[' ','s'])))

"""
3.sorted()函数就可以对list进行排序：
"""
sorted(['bob','z','a'],key=str.lower,reverse=True)#实现关键字函数，并实现反序调用
"""
4.函数作为返回值
"""
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3,3)
print(f())
#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
"""
>>> f1 = lazy_sum(1, 3, 5, 7, 9)
>>> f2 = lazy_sum(1, 3, 5, 7, 9)
>>> f1==f2
False
"""
"""
1.函数的闭包。
返回的函数并没有立刻执行，而是直到调用了f()才执行。
2.返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。可使用下例。
3.方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，
无论该循环变量后续如何更改，已绑定到函数参数的值不变：
"""
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
#print(count())
f1,f2,f3=count()
print(f1())
print(f2())
"""
1.匿名函数。lambda x: x * x 前面x表示参数
"""
f=lambda x:x*x
print(f(5))
"""
装饰器：这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
"""
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log#等价于now = log(now)
def now():
	print('2015-3-25')
now()
#定义需要传参的日志。
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)#相当于wrapper.__name__ = func.__name__****保证依赖函数签名的代码执行不会出错。
        def wrapper(*args,**kw):#所以缩进很重要你把Tab都换成空格就好了,竟然还有这种错
            print('%s %s():'%(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log('eexx')# 相当于now= log('eexx')(now)
def now():
	print('2015-3-25')
now()
print(now.__name__)
"""
偏函数：把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
下面这个函数等价于
def int2(x, base=2):
    return int(x, base)
"""
int2=functools.partial(int,base=2)
print(int2('1000'))
max2=functools.partial(max,10)#实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(1,3,3))