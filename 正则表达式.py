#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错

import re
'''
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''
"""
用\d可以匹配一个数字，\w可以匹配一个字母或数字..可以匹配任意字符.
'00\d'可以匹配'007'
'\w\w\d'可以匹配'py3'
'py.'可以匹配'pyc'、'pyo'、'py!
用*表示任意个字符（包括0个），用+表示至少一个字符，用?表示0个或1个字符，用{n}表示n个字符，用{n,m}表示n到m个字符。用在上述的后面作后缀
\d{3,8}表示3-8个数字，例如'1234567'。
\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
"""

if re.match(r'^\d{3}\-\d{3,8}$', '010-231'):
	print('ok')
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))#空格逗号分号都可以在切分的时候识别
'''
正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）。可用于提取子串
如果正则表达式中定义了组，就可以在Match对象上用group()方法提取出子串来。
注意到group(0)永远是原始字符串，group(1)、group(2)……表示第1、2、……个子串。
'''
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0))
print(m.group(1))
print(m.group(2))
t = '19:15:30'
#可以用来识别时间
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())
'''
由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
'''
print(re.match(r'^(\d+?)(0*)$', '102300').groups())
'''
如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：
'''
re_telephone= re.compile(r'^(\d{3})-(\d{3,8})$')#预编译
print(re_telephone.match('010-2102').groups())

