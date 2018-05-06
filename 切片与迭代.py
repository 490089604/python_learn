#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
'''
切片的使用
1.L[0:3]取得0,1,2
2.L[-2:-1]倒数第二个数
注Python支持L[-1]取倒数第一个元素。记住倒数第一个元素的索引是-1. 
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[0:3]
L[:3]
L[1:3]
L[-2:]
L[-2:-1]
L = list(range(100))
L[:10:2]#前10个数每两个取一个
L[::5]#隔5个写一个
#甚至可以直接写成这样
(0, 1, 2, 3, 4, 5)[:3]
'''
迭代
1.对于字典的迭代见下式.(注：字典具有无序性)
'''
d = {'a':1,'b':2,'c':3}
#for key in d :
#for value in d.values() :
for k,v in d.items() :
	print(k,v)
#对字符串的迭代
for ch in 'ABC':
    print(ch)
lisa=['a','b','c']
for i,value in enumerate(lisa):#的enumerate函数可以把一个list变成索引-元素对
	if i==2:
		print(value)
	