#!/usr/bin/env python3
#上面是为了在linux和MAC环境下以exe形式运行
#coding=utf-8
#输出中文，不写会报错
"""
判断是否是可迭代对象
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
注意可迭代对象与迭代器的区别。
1.生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
把list、dict、str等Iterable变成Iterator可以使用iter()函数：
2.这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
"""
from collections import Iterable
isinstance([],Iterable)
from collections import Iterator
isinstance({}, Iterator)
isinstance(iter([]), Iterator)#iter把可迭代对象变成迭代器。