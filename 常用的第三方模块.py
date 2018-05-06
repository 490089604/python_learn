#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#生成验证码图片
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(2):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
"""
#访问url.直接访问出错、、、
import io  
import sys  
import requests
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') #改变标准输出的默认编码
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')    
r = requests.get('https://www.douban.com/') # 豆瓣首页
#str转bytes叫encode，bytes转str叫decode，就是讲字符串转化为相应的字符编码叫encode
print(r.status_code)
#print(r.content)
r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
#print(r.content)
#需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post('https://accounts.douban.com/login', json=params) # 内部自动序列化为JSON
"""
类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
以后还有很多，注意查询。
"""
#chardet用于检测字符类型
import chardet
#检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。
print(chardet.detect(b'Hello, world!'))
"""
相关编码
编码名称	用途
utf8	所有语言
gbk	简体中文
gb2312	简体中文
gb18030	简体中文
big5	繁体中文
big5hkscs	繁体中文

"""
"""
psutil.它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
"""
import psutil
print(psutil.cpu_count())# CPU逻辑数量
print(psutil.cpu_count(logical=False)) # CPU物理核心
print(psutil.cpu_times())
#CPU使用率
# for x in range(10):
# 	print(psutil.cpu_percent(interval=1, percpu=True))
#查看内存使用率。
print(psutil.virtual_memory())
#交换区,磁盘分区，磁盘使用情况，磁盘io
#psutil.net_if_stats()print(psutil.swap_memory(),'\n',psutil.disk_partitions(),psutil.disk_usage('C:\\'),psutil.disk_io_counters())
## 获取网络读写字节／包的个数
print(psutil.net_io_counters()) 
# # 获取网络接口信息
print(psutil.net_if_addrs())
#要获取当前网络连接信息
#print(psutil.net_connections()) 
"""
获取进程信息
通过psutil可以获取到所有进程的详细信息：
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001511052957192bb91a56a2339485c8a8c79812b400d49000 
"""
"""
virtualenv是如何创建“独立”的Python运行环境.原理很简单，就是把系统Python复制一份到virtualenv的环境，
用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境。
"""
