#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
#本文件是一个模块
'a test module'
_author_='cf_wu'
import sys
def test():
    args = sys.argv#argv变量，用list存储了命令行的所有参数
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print ('Hello, %s' % args[1])
    else:
        print('Too many arguments!')
'''
当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，
这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。*****
注意是命令行，命令行
'''
if __name__=='__main__':
    test()
