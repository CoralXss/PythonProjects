# IO编程
#	文件读写
#	StringIO 和 BytesIO
#	操作文件和目录
#	序列化

############################################################
# 一、文件读写

# 背景：在磁盘上读写文件的功能均是由操作系统提供，现代操作系统不允许普通的程序直接操作磁盘。
# 方式：读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
# 	 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入该文件对象（写文件）。

# 1. 读文件
# 方法： Python内置函数 - open(文件名, 标识符['r'只读])	 
# 说明：
  # 1）若文件不存在，该函数会抛出 IOError 错误，并且给出错误码和详细信息告知文件不存在；
  # 2）若文件打开成功，使用 read() 函数可一次性读取文件全部内容；
  # 3）Python 把内容读到内存，用一个 str 对象表示。
  # 4）调用 close() 方法关闭文件。
  #   【文件使用完毕必须关闭，因为文件对象会占用操作系统的资源，并且os同一时间能打开的文件数量是有限的。】

# 以下抛出错误：FileNotFoundError: [Errno 2] No such file or directory: 'Users/xss/notfound.txt'
file = open('./channel', 'r')
content = file.read()
file.close()   # 必须关闭文件
print(content) # 打印文件内容（success）

# 完整定义一个读文件函数：
def readFile(filename):
	try:
		file = open(filename, 'r')
		print(file.read())
	finally:
		if file:
			file.close()

# 简洁代码写法：
def readFile2(filename):
	with open(filename, 'r') as file:
		print(file.read())

# 问题：当文件size太大时，一次性读取文件，内存就会爆满，如何解决呢？
# 方式：保险起见，三种方式：
  # 1）read(size); 每次读取一行内容，每次最多读取 size 个字节的内容；
  # 2）readline(); 每次读取一行内容；
  # 3）readlines(); 一次读取所有内容并按行返回 list.

# 各方式使用场景：
# 1）read() 适用于文件很小时一次性读取；
# 2）无法确定文件大小时，反复调用 read(size) 比较保险；
# 3）若是配置文件，使用 readlines() 最方便。

def readFileByLine(filename):
	file = open(filename, 'r')
	for line in file.readlines():
		print(line.strip())  # 删除末尾'\n'

# 2. 文件读取模式
# 文本文件读取+默认UTF-8： open(filename, 'r')
# 二进制文件读取：open(filename, 'rb')  # 二进制文件-图片视频等
# 非UTF-8编码文件：open(filename, 'r', encoding='gbk')  # 中文

# 关于文件编码不规范问题，会抛出 UnicodeDecodeError 非法编码字符，使用如下方式：
 # f = open('./channel', 'r')
 # print(f.read())

ff = open('./first.py', 'r', encoding='gbk', errors='ignore')
print(ff.read()) # 忽略非法字符，读取中文乱码（改成 encoding='utf-8'）

# 3. 写文件
#	open(filename, 'w' / 'wb') 写文本文件或写二进制文件

filename = './first.py'
f = open(filename, 'w')
f.write('# Hello, world')
f.close()

readFileByLine(filename)

def writeFile():
	with open('./first.py', 'w') as f:
		f.write('Hello, world !')

# 总结： Python 中，文件读写是通过 open() 函数打开的文件对象完成的。使用 with 语句操作文件 IO 是好习惯。


############################################################
# 二、StringIO 和 BytesIO

# 1. StringIO (在内存中读写 str)
# 前言：很多时候，数据读写不一定是文件，也可以从内存中读写。

# 实例：把 str 写入 StringIO。

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())  # hello world!

# 说明：getvalue() 方法用于获得写入的 str。

# 实例：读取 StringIO。
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
# 按行打印如下：
# Hello!
# Hi!
# Goodbye!
		
# 2. BytesIO (在内存中读写二进制数据)

# 实例：创建一个 BytesIO 并且写入 bytes。

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8')) # 写入str经过utf-8编码的bytes
print(f.getvalue())  # b'\xe4\xb8\xad\xe6\x96\x87'


# 总结：StringIO 和 BytesIO 是在内存中操作 str 和 bytes 的方法，使得和读写文件具有一致的接口。


############################################################
# 三、操作文件和目录

# 问题：Python 中如何执行操作目录和文件？
# A：操作目录和文件使用系统命令：dir、cp 等，操作系统命令其实是简单调用了操作系统提供的接口函数，
#	Python 内置的 os 模块可以直接调用操作系统提供的接口函数。

# os 模块的基本功能：

import os

# os.name = posix(代表系统是 Linux, Unix 或 Mac OS X，nt 表示 Windows)
print('os.name =', os.name) 

# 获取系统详细信息 (..., machine='x86_64)
print(os.uname())

# 查看os中定义的环境变量。
print(os.environ)
# 获取某个环境变量的值。
print(os.environ.get('ANDROID_HOME')) # /Users/xss/Library/Android/sdk


# 1. 操作文件和目录

# 实例一：查看、创建和删除目录（os.path模块）。

# 查看当前目录绝对路径
print(os.path.abspath('.')) 

# 在当前目录下创建一个新目录testdir，以下为获取新目录完整路径
testdir = os.path.join('.', 'testdir') 
print(testdir)   # ./testdir
# 创建新目录
# os.mkdir(testdir)
# 删除目录
# os.rmdir(testdir)

# join()方法将两个路径合成一个，可以正确处理系统路径分隔符
print(os.path.join('.', 'testdir'))       # ./testdir

# split()方法拆分路径为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split('./python_9_io.py'))  # ('.', 'python_9_io.py')

# splitext()方法获取文件扩展名
print(os.path.splitext('./python_9_io.py')) # ('./python_9_io', '.py')

# 注：上述合并、拆分路径的函数并不要求文件和目录真实存在，仅针对字符串进行操作。

# 实例二：（os 模块）

# rename()方法对文件重命名
# os.rename('test.txt', 'test.py')

# 删除文件
# os.remove('test.py')

# 复制文件(非os模块，因为文件复制不是操作系统提供的系统调用)
# shutil.copyfile()

# 实例三：列出当前目录下的所有目录。

def listFiles():
	arr = [x for x in os.listdir('.') if os.path.isdir(x)]
	print(arr)
listFiles() # ['.9', '__pycache__']

# 列出所有的 .py文件：
arr = [x for x in os.listdir('.') if os.path.isfile(x) 
			and os.path.splitext(x)[1] == '.txt']
print(arr)  # ['python_0_exception.txt']


# 练习

# 利用os模块编写一个能实现dir -l输出的程序。

# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。



############################################################
# 四、序列化

# 说明：
# 1）序列化：将变量从内存变成可存储或传输的过程称为序列化，Python 中为 pickling；
# 2）作用：把序列化后的内容可以写入磁盘或者通过网络传输给别的机器；

import pickle

# 将对象序列化为一个 bytes
d = dict(name = 'Bob', age = 20, score = 88)
print(pickle.dumps(d))

# 将一个序列化对象写入文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 从磁盘文件中读取对象到内存
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)  # {'name': 'Bob', 'age': 20, 'score': 88}



############################################################
# 五、JSON

# Python内置数据类型 和 JSON对应关系：
# JSON类型	    Python类型
# {}		    dict
# []		    list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None

import json

# 把Pytho对象变成 Json字符串
d = dict(name = 'Bob', age = 20, score = 8)
print(json.dumps(d))  # 返回str，{"name": "Bob", "age": 20, "score": 8}

# 将 json 格式字符串反序列化为 Python 对象
json_str = '{"name": "Bob", "age": 20, "score": 8}'
dict_json = json.loads(json_str)
print(dict_json) # {'name': 'Bob', 'age': 20, 'score': 8}

# 将对象序列化为json字符串（dict可以直接转化为json串）

class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


s = Student('Bob', 20, 88)
# print(json.dumps(s)) # TypeError: Object of type 'Student' is not JSON serializable
# 说明：上述操作不做任何处理，将对象转化为json串，会直接报错，
#	因为Student对象不是可序列化为JSON的对象。

# 解决：定制 JSON 序列化。默认情况下，dumps() 方法不知如何将 Student 实例变为 JSON {} 对象。
def student2dict(std):
	return {'name': std.name, 'age': std.age, 'score': std.score}

print(json.dumps(s, default=student2dict))	# {"name": "Bob", "age": 20, "score": 88}

# Tips: 将每个类序列化为JSON串，简单写法可以将任意 class 变成 dict:
# 原理：每个 class 实例均有一个 __dict__ 属性，除了定义了 __slots__的class。
print('Simple to JSON: ', json.dumps(s, default=lambda obj: obj.__dict__))

# 将JSON串反序列化为对象
def dict2Student(dict_json):
	return Student(dict_json['name'], dict_json['age'], dict_json['score'])
json_str = '{"name": "Bob", "age": 20, "score": 8}'
# <__main__.Student object at 0x1021d5d68>
print(json.loads(json_str, object_hook=dict2Student))	

























