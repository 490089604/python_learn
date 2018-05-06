#!/usr/bin/env python3
# 上面是为了在linux和MAC环境下以exe形式运行
# coding=utf-8
# 输出中文，不写会报错
class  student(object):
	#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
	#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
	#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	pass
def setage(self,age):
	self.age=age
#还可以尝试给实例绑定一个方法.
#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
from types import MethodType
# s=student()#因__solts__先注释掉
# s.setage=MethodType(setage,s)
# s.setage(10)
# print(s.age)

#直接用类来创建一个方法  不过此时还是用链接的方式在类外的内存中创建
student.set_age = MethodType(setage,student)
#此时在创建实例的时候外部方法 set_age 也会复制 这些实例和Student类都指向同一个set_age方法
new1 = student()
new2 = student()
new1.set_age(99)
new2.set_age(98)#第二个会覆盖第一个 
print(new1.age,new2.age)#看结果 2个都是98
#给class绑定方法。
#直接绑定
def set_score(self, score):
	self.score = score
student.set_score = set_score
class Student1(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s=Student1()
s.score=100# OK，实际转化为s.set_score(100)
print(s.score)# OK，实际转化为s.get_score()
"""
python支持多重继承。被称为MixIn。
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass
"""
"""
def __len__(self):
        return len(self.names)
"""
class Student2(object):
	__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	def __init__(self, name=1):
		self.name = name
	def __str__(self):#返回这个对象
		return 'Student object (name: %s)' % self.name
	def __len__(self):
		return len(self.name)
	__repr__ = __str__#使交互界面返回的字符串与直接调用相同
	#以下两个用于迭代。类用于for ... in循环，实现一个__iter__()方法，该方法返回一个迭代对象，然后，
	#Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
	def __iter__(self):
		return self#实例本事就是迭代对象
	def __next__(self):
		self.name=self.name+1# 计算下一个值
		if self.name > 10: # 退出循环的条件
			raise StopIteration()
		return self.name # 返回下一个值
	def __getitem__(self,n):#访问数列的任意一项了
		if isinstance(n, int): # n是索引
			return n;
		L=[]
		if isinstance(n,slice):#n为切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			for x in range(stop):
				if x >= start:
					L.append(x)
			return L
	#没有找到某个这个attribute。那就是写一个__getattr__()方法，动态返回一个属性。
	def __getattr__(self,attr):
		if attr == 'score':
			return 99
		if attr=='age':
			return lambda: 25
		#raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)。如果无此句默认返回error

#__str__
print(Student2('Michael'))#__str__
#测试迭代
for n in Student2():
 	print(n)
#测试getitem
s = Student2()
print(Student2()[1])#调用__getitem__(self,n):
print(Student2()[:10])
print(Student2()[5:10])
#测试__getattr__()
print(Student2().score)
print(Student2().age())
print(Student2().wu)
#用类的转化实现url的转换。这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
class Chain(object):
	def __init__(self, path = ''):
		self._path = path
	def __getattr__(self, path):
	 	return Chain('%s/%s' %(self._path, path))
	def __str__(self):
		return self._path
	__call__ = __getattr__#只需要定义一个__call__()方法，就可以直接对实例进行调用。callable()可以用来判断是否是可调用函数。
	__repr__ = __str__
print(Chain().staus.user)
"""
枚举类

"""
from enum import Enum,unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member1 in Month.__members__.items():#value属性则是自动赋给成员的int常量，默认从1开始计数。
    print(name, '=>', member1, ',', member1.value)
@unique#@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
 #访问方法
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

