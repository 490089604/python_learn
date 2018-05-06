#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
class  student(object):
	#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
	#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
	#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
	#__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	def __len__(self):
        return len(self.names)
def setage(self,age):
	self.age=age
#还可以尝试给实例绑定一个方法.
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
from types import MethodType
s=student()
s.setage=MethodType(setage,s)