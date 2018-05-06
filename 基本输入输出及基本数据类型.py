#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
print('hello, world，我教吴长发')
print('The quick brown fox', 'jumps over', 'the lazy dog')
"""
输入输出
name = input()
print('hello,', name)
"""
print('I\'m learning\nPython.')
print(r'\\\t\\')#默认不转义r''
print('''line1
line2
line3''')#多行显示
print( 5 > 3 and 3 > 1)
#or not
PI = 3.14159265359 # 定义常量，可被修改
a= 10 // 3 #取整除，%取余
print(a)
s2 = 'Hello, \'Adam\''
s3 = r'Hello, \"Bart\"'
s4 = r'''\\Hello,
Lisa!'''#r执行不转义
print(s4)
b=None;#空值
print(b)
'''
Python 3的字符串使用Unicode，如果在网络中传输，则需要在转化成bytes或由bytes转换成str,一般使用utf-8
'''
print('ABC'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('中文asdsa'))#输出字符长度
print( 'Hi, %s, you have $%02d.' % ('Michael',1))#类似于C的输出方法
'''
1.注意02用法。
2.如果不清楚，可以直接使用%s
3.在输出时，用%%来表示一个%
%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
'''
s1 = 72
s2 = 85
print( 'Hi, you have $%.1f%%.' % (s1/s2*100))#类似于C的输出方法