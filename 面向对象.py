#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
class student(object):
	#注意：特殊方法“__init__”前后分别有两个下划线！！！
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print(('%s: %s') %(self.name,self.score))
	def get_grade(self):
		if self.score >=0:
			return 'a'

s1=student('n',1)
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
#感觉非常有用。
s1.name='wuchangfa'
s1.print_score()
print(s1.get_grade())
class Student1(object):
    def __init__(self, name, score):
        self.__name = name#私有变量，只能从内部访问，不能从外部
        self.__score = score
    def __len__(self):#调用len()自动返回self.__name的长度
        return len(self.__name)
    def set_score(self, score):
        self.__score = score
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
s2=Student1('wu',10)
print('length', len(s2))
s2.set_score(23)
print(s2.get_score())
"""
动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类
，否则，将无法调用run()方法。
对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()
方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
"""
"""
总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
"""
isinstance(123, int)
class MyDog(object):
    def __len__(self):
        return 100
dog=MyDog()
print(len(dog))
"""
仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
"""
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
hasattr(obj, 'x')
setattr(obj, 'y', 19)
getattr(obj, 'y')   
getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
a=obj.power
fn = getattr(obj,'power') # 获取属性'power'并赋值到变量fn
print(fn())
class Student(object):
    name = 'Student'
print(Student.name)
s=Student()
s.name='wuchangfa'
print(s.name)
print(Student.name)
del s.name# 如果删除实例的name属性
print(s.name)
