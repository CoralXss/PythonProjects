# Python 基础

# 一、输入输出 & 数据类型（整数、浮点数、字符串''、布尔值、空值）

#####################
# 1）浮点数：小数，不用添加 f，直接用小数表示；
# 2）字符串
# 3）布尔值：and, or 和 not 与或非运算；
# 4）空值：None，不能理解为0；
# 5）整数：+， -， *，/ (结果为浮点数)，//（地板除，整数地板除为整数），%（取余数）

print('hello, world')
print('100 + 200 =', 100 + 200)
print('1024 - 768 =', 1024 - 768)
print('1024 * 768 =', 1024 * 768)
# 两种除法运算：1) / 除法运算结果是浮点数，即使是两个整数恰好整除； 2） // 地板除，整数的地板除仍是整数
print('9 / 3 =', 9 / 1)  # 3.0
print('10 / 3 =', 10 // 3) # 3

# 用户输入字串，存到变量中
name = input()
print('Hello', name)

name = input("Please input your name: ")
print('Hello', name)

# 多个字符串输出，用逗号隔开，分开的字串输出会用 空格 分开连成一串
print("The quick brown fox", 'jumps over', 'the lazy dog .')

# 当语句以 : 结尾，缩进的语句视为 代码块
a = 100
if (a >= 0):
	print(a)
else:
	print(-a)	

# 小诀窍：若字符串中有很多需要加\转义，可以使用 r'' 表示 ''内部的字符串默认不转义
print('\\\t\\') # \  \t制表符  \
print(r'\\\t\\')# \\\t\\

# 小诀窍（交互式 >>> 适用）：若字符串中有很多换行，可使用 '''...''' 表示多行内容
print('''line1
	line2
	line3''')

# 布尔值：两种值，True False
print(1 > 2)     # False 布尔值
print(True)      # True 直接使用大写的 True False 表示布尔值
# not 单目，非运算
print(not True)  # False
print(not 1 > 2) # True

# 空值： None 不能理解为0
print(None)      # None

# 常量：不能变得变量，大写变量名表示，但是值仍然可以改变，只不过表示一种编码习惯
PI = 3.14159265359


# 二、变量：程序中直接用一个变量名表示，变量名规则：大小写、数字和_组合，不能数字开头

# 符号 = 是赋值语句，可以把任意数据类型赋给同一个变量
# 动态语言：变量本身类型不固定，可以赋值为不通类型，如下示例：
a = 123
print("int a = ", a)
a = 'ABC'   # Python解释器做了两件事：一是在内存中创建了'ABC'字符串；二是在内存中创建了 a 变量，并指向'ABC'
print('string a = ' + a)

# 静态语言：定义变量时必须制定变量类型，若赋值时类型不匹配，则会报错：
# int i = 123  // b 时整型变量
# b = 'ABC';    // 此时会报错

# 将一个变量a赋值给另一个变量b，实际是把变量b指向变量a所指向的数据
a = 'ABC'
b = a
a = 'XYZ'
print(b)  # ABC

n = 123
print('n = ', n)

f = 456.789
print('f =', f)
print('s1 =', "'Hello, world'")
print('s2 =', 'Hello', "\\\'Adam\\\'\'")
print('s2 =', r'Hello, \'Adam\'\'')

print('中')


# 三、格式化 - 占位符 % 运算符用来格式化字符串，多个占位符 %s %d %f ...就用 ()包围
#  %s 字符串   %f 浮点数   %d 整数   %x 十六进制整数

print('Hello, %s' % 'World', 'give me %d' % 5)
print('Hi, %s, give me %d' % ('Coral', 5)) # Hi, Coral, give me 5

# 四、使用 list 和 tuple

# 1. list 列表：Python 内置的一种数据类型，可随时添加和删除元素
classmates = ['Michale', 'Bob', 'Coralline'] 
print(classmates)  # ['Michale', 'Bob', 'Coralline']
# len() 获取 list 元素的个数
print("classmates,len =", len(classmates))
# 索引访问 list 中每一个位置元素
print(classmates[0], classmates[1], classmates[2]) # Michale Bob Coralline
print(classmates[-1]) # -1为索引，直接取最后一个元素
# list 追加元素到末尾
classmates.append("Adam")
print(classmates)
# 插入元素
classmates.insert(1, 'Jack')
print(classmates)
# 删除末尾元素
classmates.pop()
# 删除指定索引元素
classmates.pop(3)

# list 中可包含不通类型的元素
p = ['asp', 'php']
s = ['python', 'java', p, 123, True]
print(s)
print(p[1] + " = " + s[2][1])


# 2. tuple元组：有序列表，同 list 区别：tuple一旦初始化就不能修改
classmatesTuple = ('Michale', 'Bob', 'Coralline')
print(classmatesTuple)

# 因为初始化就不能改变，所以也没有插入方法，元素获取也是通过所以获取，但是不能修改值
# 注：tuple 不可变，所以代码更安全；在定义时，tuple的元素必须被确定下来。


# 五、条件判断  if...elif...else
age = 3
print('your age is', age)
if (age >= 18):      # 注意不要少些了 : 
	print('Adult')
elif (age >= 6):
	print('Teenager')
else:
	print('Kid')

x = 1
if x:
	print('True')  # 此处简写，只要 x = {非零数值，非空字串，非空list等}，则为True

# 针对 input() 返回的数据类型是 字符串，不能直接和整数比，会报错，需要使用 int()函数转型。
birth = input('birth: ')
birth = int(birth)
if (birth < 2000):
	print('00前')
else:
	print('00后')


# 六、循环 [for while break continue]

# 1. 计算 1-10整数之和。
sumResult = 0
elements = [1, 2, 3, 4, 5, 6, 7,8, 9, 10]
for i in elements:
	sumResult = sumResult + i
print("sumResult = ", sumResult)

# 2. 计算 1-100 整数之和。
sumResult = 0
elements = range(101) # 生成0-100的整数序列
for i in elements:
	sumResult = sumResult + i
print("sumResult of 0-100 = ", sumResult)	

# 3. 计算100以内所以奇数之和。
sumResult = 0
n = 99
while n > 0:
	sumResult = sumResult + n
	n = n - 2
print('sumResult = ', sumResult)	

# 4. break 语句提前退出循环。
n = 1
while n <= 100:
	if (n > 10):
		break   # 提前结束循环
	print(n)
	n = n + 1
print('END')

# 5. continue 跳过本次循环，继续下一次循环
n = 0
while n < 10:
	n = n + 1
	if (n % 2 == 0):
		continue
	print(n)	# 打印1-10内的奇数	


# 七、使用 dict 和 set

# 1. dict 
# 说明：Python 内置了字典：dict 支持，也即 dictionary，同 Map，使用键值对存储，查找速度极快。
gradeDict = {'Michale': 95, 'Bob': 75, 'Coralline': 85}
print(gradeDict['Coralline'])

# 重新赋值
gradeDict['Coralline'] = 89
print(gradeDict['Coralline'])

# 若 key 不存在，则会报错，有两种方法避免，一是通过 in 判断 key 是否存在：
if ('Coralline' in gradeDict):
	print(gradeDict['Coralline'])

# 二是通过 dict 提供的 get 方法，若 key 不存在，可以返回 None 或者指定的默认值：
print(gradeDict.get('Coralline', 0))

# 删除 key，pop(key)
gradeDict.pop('Bob')
print(gradeDict)   # {'Michale': 95, 'Coralline': 89}

# 对比于list，dict的特点: 1) 查找和插入块，不会随着 key 增加而变慢； 2）占用内存大，因而内存浪费多
# 总结：dict 是用空间来换取时间。

# 2. set 也是一组 key 集合，但不存储 value，因为 key不重复，所以 set 没有重复 key。
# 创建一个 set，需要一个 list 作为参数
mySet = set([1, 2, 3])
print(mySet)   # {1, 2, 3}

# 添加元素
mySet.add(4)
print(mySet)

# 删除元素
mySet.remove(4)
print(mySet)

# set 无序 & 无重复元素，可计算交集和并集。
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print("交集：", s1 & s2)
print('并集：', s1 | s2)

# 3. 可变和不可变对象
# 1) set 和 dict 唯一区别在于 set 没有存储对应的 value，但是两者都不能存放 可变对象，因为无法判断两个可变对象是否相等，导致重复元素；
# 2) str 字符串是不可变对象，而 list 是可变对象；

a = 'abc'
print(a.replace('a', 'A'))  # Abc 创建新串并返回
print(a)                    # abc
# 总结：对于不可变对象，调用对象自身的任意方法，也不会改变对象自身的内容。
# 相反，这些方法会创建新的对象并返回，如此就保证了不可变对象本身永不改变。

mySet.add((5, 6)) # set中添加 list 会直接报错，但是存放 tuple 不会
# mySet.add((7, 8, [9, 0]))  # 报错，tuple 是不可变对象，但是其中的 list 元素可变，所以无法保证元素不重复
print(mySet)  # 1, 2, 3, (5, 6)}
















