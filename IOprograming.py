#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
"""
使用import 模块名  是导入该模块，该模块下所有的方法都可以使用  使用规范： 模块名.方法名
from 模块名 import 函数名    是导入该模块下的特定的函数名，使用时直接使用函数名。
eg:
import math
print(math.pi)

from math import sqrt
print（sqrt(2, 3)）
"""
with open('python基础学习\\test.txt','r') as f:#可以不用写f.close() encoding='gbk'参数，errors='ignore'
	#print(f.read())
	for line in f.readlines():
		print(line.strip())
with open('python基础学习\\test.txt', 'w') as f:#以'w'模式写入文件时，如果文件已存在，会直接覆盖。可以传入'a'以追加（append）模式写入不会覆盖。
    f.write('Hello, world!')
#StringIO与BytesIO 
from io import StringIO
f =  StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s=='':
		break
	print(s.strip())
#Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
import os
os.path.abspath('.')
#os.path.join('E:\\学习\\python','cfwu')
#os.mkdir('E:\\学习\\python\\cfwu')
#os.rmdir('E:\\学习\\python\\cfwu')
#os.rename('test.txt', 'test.py')
#列出当前路径上所有尾缀为py的[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
#序列化
import pickle#只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))
f = open('dump.txt', 'wb')
pickle.dump(d, f)#直接写入文件
f.close()
f = open('dump.txt', 'rb')
#也可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
d=pickle.load(f)
f.close()
print(d)
#json序列化
import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))#json序列化
print(json.loads(json.dumps(d)))#json反序列化
"""
序列化一个class:
print(json.dumps(s, default=lambda obj: obj.__dict__))# 可选参数default就是把任意一个对象变成一个可序列为JSON的对象.一个提供的写参数的地方
反序列化一个class:
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json.loads(json_str读出来的json对象, object_hook=dict2student)# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
"""
