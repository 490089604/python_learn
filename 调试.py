#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
"""
1.此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
eg:
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
2.在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。
eg:
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。所以会一直捕获第一个.
3.Python内置的logging模块可以非常容易地记录错误信息.
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')
4.在bar()函数中，打印一个ValueError!后，又把错误通过raise语句抛出去了，捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么
处理该错误，所以
，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，
最终会抛给CEO去处理。
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
"""