#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
#对一个list的操作。添加删除修改。
"""
1.每一个变量的数据类型可以不一样。
2.tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
"""
classmates = ['Michael', 'Bob', 'Tracy']#list[,,,,]
print(classmates[-1])#倒数第一个
classmates.append('Adam')
classmates.insert(1, 'Jack')
classmates.pop()
classmates.pop(0);
print(classmates)
"""
1.tuple一旦定义无法修改。但内容可以是list,list内容可以更改
"""
t = (1,2,['a','a']) 
print(t)
t = (1,)#定义一个元素的tuple
print(t)
t = (1)#t就是1
print(t)
'''
else if判断
'''
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
    if age == 3:
    	print('hahah')
'''
s = input() 
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
'''
'''
1.for循环。
2.range(101)生成0到100的数
'''
sum = 0
for x in range(101):
	#for y in [1,2,2,3,4,5,6]:
    sum = sum + x
print(sum)
#while
sum = 0
n = 99
while n > 0:
#while 1 :
    sum = sum + n
    n = n - 2

print(sum)
#dict,map,hash表,利用存储空间在来替代查询速度。dict{a:b,c:d}
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Michael'] = 67
print(d.pop('Bob'))
d.get('Tracy')
d.get('21312',-1)#不存在返回-1
#set。set([1,2,3,4,5,2,6])
'''
1.一组key值的集合。但是没value.key不能重复
1.注意，传入的参数[1, 2, 3]是一个list，
而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
2.重复元素在set中自动被过滤.
'''
s = set([1, 1, 2, 2, 3, 3])
s = set([1,2,3,4,'aa'])
s.add(4)
s.remove(4)
'''
1.str是不可变对象，而list是可变对象。注意例子。
'''
a = ['c', 'b', 'a']
a.sort()
print(a)
a = 'abc'
b=a.replace('a', 'A')
print(a)
print(b)