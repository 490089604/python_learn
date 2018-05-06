#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
'''
通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。
第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
'''
g=(x*x for x in range(1,10))
for n in g:
	print(n)
#斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b#声明函数为geneator,存储在类似于list的表中。只用在函数中
        a, b = b, a + b#triple b赋值给a,a+b赋值给b
        n = n + 1
    return 'done'
x =fib(4)
print(next(x))
print(next(x))
for b in x:
	print (b)
#捕获返回值
# call generator manually:
g = fib(5)#generator函数的“调用”实际返回一个generator对象：也就是在这其实g是一个对象。
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)#捕获错误
        break
