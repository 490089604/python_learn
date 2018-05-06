#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
1.当前时间就是相对于epoch time的秒数，称为timestamp。
'''
from datetime import datetime,timedelta,timezone
t = 1429417200.0
print(datetime.fromtimestamp(t)) # 本地时间,北京时间。UTC+8:00正8.
print(datetime.utcfromtimestamp(t)) # UTC时间。格林威治标准时间
#很多时候人们输入的日期和时间是字符串。要处理日期和时间，首先必须把str转换为datetime。
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
now= datetime.now()
print(now.strftime(('%a, %b %d %H:%M')))
print(now + timedelta(hours=10))
tz_utc_8 = timezone(timedelta(hours=8))
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
'''
时区转换
'''
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
from collections import deque,defaultdict,OrderedDict,Counter
q = deque(['a', 'b', 'c'])
#deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
#这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd = defaultdict(lambda: 'N/A')
print(dd['key1'])
#如果要保持Key的顺序，可以用OrderedDict：
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
#FIFOdict
class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0 #包含为1不包含为0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)

            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
a=LastUpdatedOrderedDict(2)
a['1']=1
a['2']=2
print(a)
a['3']=3
print(a)
a['2']=3
#Counter是一个简单的计数器。Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，其计数作为value。
c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
#base64
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
# d = base64.b64decode(s).decode('utf-8')
# print(d)
# s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
# print(s)
# d = base64.urlsafe_b64decode(s).decode('utf-8')
# print(d)
####
#struct
####
#struct的pack函数把任意数据类型变成bytes：
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
import struct
struct.pack('>I', 10240099)
#unpack把bytes变成相应的数据类型：
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
#十六进制转义字符
"""
struct.unpack('>B', b'\n')
(10,)
>>> struct.unpack('>B', b'\x0a')
(10,)
>>> struct.unpack('>H', b'\x00\x01')
(1,)
>>> struct.unpack('<H', b'\x00\x01')
(256,)
>>> struct.pack('>I', 16)
b'\x00\x00\x00\x10'
>>> struct.pack('>I', 255)
b'\x00\x00\x00\xff'
>>> struct.pack('>H', 2)
b'\x00\x02'
\x02一个这个东西表示一个字节，按照16进制编码
用法：
struct.unpack('<ccIIIIIIHH', s)
(b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
"""
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
"""
可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
"""
import hashlib
#md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))#.encode('utf-8')Unicode-objects must be encoded before hashing
print(md5.hexdigest())
#sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
"""
如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。
由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。

但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？

如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
"""
import hashlib, random
def calc_md5(password):
    return get_md5(password + 'the-Salt')#可以使用户名加盐然后存储
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user = db[username]
    return get_md5(password)#user.password == get_md5(password)
print(login('michael', '123456'))
print([chr(random.randint(48, 122)) for i in range(5)])
#chr返回ASCII码对应的字符，相反的操作为ord
print(' '.join([chr(random.randint(48, 122)) for i in range(20)]))#join返回通过指定字符连接序列中元素后生成的新字符串。这里的指定字符为' '
#它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。
#hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
h.update(message)
print(h.hexdigest())
#Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
import itertools
"""
count()会创建一个无限的迭代器， natuals = itertools.count(1)
for n in natuals:
 	print(n)
cycle()会把传入的一个序列无限重复下去：
cs = itertools.cycle('ABC') # 注意字符串也是序列的一种
for c in cs:
     print(c)
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
ns = itertools.repeat('A', 3)
for n in ns:
     print(n)
无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
"""
natuals = itertools.count(3)#参数指定从几开始
ns = itertools.takewhile(lambda x: x<10, natuals)
print(list(ns))
"""
chain()
chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
>>> for c in itertools.chain('ABC', 'XYZ'):
...     print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z'
groupby()把迭代器中相邻的重复元素挑出来放在一起：
>>> for key, group in itertools.groupby('AAABBBCCAAA'):
...     print(key, list(group))
"""
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):#通过函数判断的。取消大小写差异。只要例如A和a识别均可。
    print(key, list(group))
#contextlib
from contextlib import contextmanager
class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('Query info about %s...' % self.name)
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
with create_query('Bob') as b:
    print('auauau')
    b.query()
"""
执行顺序，先执行with后面的，遇到yield执行with函数体里面的。然后执行yeild后面的。
很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
"""
@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)
with tag("h1"):
    print("hello")
    print("world")
"""
closing它的作用就是把任意对象变为上下文对象，并支持with语句

from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.python.org')) as page:#此处用于实现网络爬虫
    for line in page:
        print(line)
"""
"""
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应.
写爬虫需要进一步探索
"""
# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))
#如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)
"""
正常情况下，优先考虑SAX，因为DOM实在太占内存。
在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了。
"""
xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)