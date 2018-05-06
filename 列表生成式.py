#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
print(list(range(1,11)))#
##
L = []
for x in range(1, 11):#1到10
	L.append(x * x)
print(L)
#列表表达式
[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0]
#双层循环
[m + n for m in 'ABC' for n in 'XYZ']
#列出当前文件夹下的目录
import os
[d for d in os.listdir('.')]
 d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k + '=' + v for k, v in d.items()]
#以上对应的代码如下
d = {'x': 'A', 'y': 'B', 'z': 'C' }
	for k, v in d.items():
	    print(k, '=', v)
#将大写转化成小写。eg:[s.lower() for s in L] 
