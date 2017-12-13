# 函数式编程 ##############
#    高阶函数
#       map/reduce
#		filter
#		sorted
#	 返回函数
#    匿名函数
# 	 装饰器
#    偏函数

# 前言
# 1. 几个定义
#    a. 任意一个函数，只要输入是确定的，输出就是确定的，这种没有变量的纯函数为无副作用；
#    b. 允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不通的输出，此种函数式有副作用的。

# 函数式编程的一个特点：允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# Python 对函数式编程提供部分支持，由于 Python 允许使用变量，因此不是纯函数式编程语言。

############################################################
# 一、高阶函数
# 定义：变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数为高阶函数。
#      简言之，就是把函数作为参数传入的函数称为高阶函数。

# 1. 变量可以指向函数
# 分为两种情况：一是将函数结果赋给变量；二是将函数本省赋值给变量，可当做是给函数取别名。
f = abs
print(f(-10))  # 10，说明 f 指向了 abs 函数本身，f()函数同于 abs()

# 2. 函数名也是变量
# 函数名其实就是指向函数的变量，如 abs 看成变量，指向一个可以计算绝对值的函数。
# abs = 10  # 重新将abs 指向一个变量 10，会改变原来的函数，操作后无法使用 abs()

# 3. 传入函数
# 变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数为高阶函数。
# 一个简单的高阶函数：
def add(x, y, f):
	return f(x) + f(y)

print('Simple 高阶 Function: ', add(10, -10, abs)) # 20


############################################################
# 4. Python内置函数之 map(函数，Iterable)
# map() 接收两个参数，一是函数，一是 Iterable，map 将传入的函数依次作用在序列的每个元素，并把结果作为新的 Iterator 返回。

# 示例一：使用 map() 将函数 f(x)=x*x 作用在 序列 [1, 2, 3, 4, 5]，也即是将序列编程对应元素的平方。
def power2(x):
	return x * x
L = map(power2, [1, 2, 3, 4, 5])  # 返回 Iterator，需 list() 方法计算并返回一个 list
print(list(L))     # [1, 4, 9, 16, 25]

print(list(map(str, [1, 2, 3, 4, 5]))) # 将整数序列编程字符串序列，['1', '2', '3', '4', '5']


############################################################
# 5. Python内置函数之 reduce(函数，序列)
# reduce() 把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累计计算，效果就是：
# reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)

# 示例一：序列求和，使用 reduce() 很方便。
from functools import reduce
def add2(x, y):
	return x + y

print(reduce(add2, [1, 3, 5, 7, 9]))	 # 25

# 示例二：将序列 [1, 3, 5, 7, 9] 变成整数13579.
def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))	

# 综合：将 str 转成 int 的函数。
# 第一步，将 str 序列转成 int 序列
def char2Int(ch):
	d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return d[ch]
# 将 char2Int 函数作用在字符串 '13579'的每一字符上，也即去除对应字符的int值		
it = map(char2Int, '13579') 
# print("first ", list(it))  # 返回的是一个序列 [1, 3, 5, 7, 9]
print(reduce(fn, it))   # 13579

# 整理成 str2int() 函数如下：
def str2int(stri):
	def fn(x, y):
		return x * 10 + y
	def char2Int(ch):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ch]
	return reduce(fn, map(char2Int, stri))

# 进一步简化
def str2int2(stri):
	return reduce(lambda x, y: x * 10 + y, map(char2Int, stri))

print('str2int2(\'1234\') = ', str2int2('12345')) # str2int2('1234') =  12345


############################################################
# 练习：利用 map()，把用户输入的不规范英文名字编程首字母大写，其他小写的规范名字。
def standardName(s):
	return s[:1].upper() + s[1:len(s)].lower()

L = ['adam', 'LISA', 'barT']
print(list(map(standardName, L)))	# ['Adam', 'Lisa', 'Bart']

# 练习：Python 提供的 sum() 可以接受一个 list 求和，编写一个 prod() 函数，可以接受一个 list 并利用 reduce() 求积。
def multiply(x, y):
	return x * y

def prod(L):
	return reduce(multiply, L)

print(prod([1, 2, 3, 4, 5]))	# 120

# 练习：利用 map 和 reduce 编写一个 str2float 函数，把字符串 ‘123.456’转换成浮点数 123.456.
def charFloat2Int(ch):
	d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}
	return d[ch]

point = 0
def arr2int(x, y):	
	global point   # point要作为全局变量才行，变为 global不管用		
	print(x, y, point)
	if point == 0:
		if y > 0:
			return x * 10 + y
	if y < 0:
		point = 1
		return x
	else:
		point = point / 10
		return x + y * point		

def str2float(s):
	it = map(charFloat2Int, s)
	return reduce(arr2int, it)

# it = str2float('123.456')
print('str2float(\'123.456\')', str2float('123.456'))


# L = [1, 2, 3, -1, 4, 5, 6]
# i = 0
# point = 0
# sum = L[0]
# for x in L:
# 	if (i < len(L) - 1):
# 		if (L[i + 1] < 0):
# 			point = 1
# 		else:
# 			point = point / 10	
# 		sum = arr2int(sum, L[i + 1], point)
# 	i = i + 1
# print(sum)	


############################################################
# 6. Python内置函数之 filter(函数，序列)
# 作用：用于过滤序列，参数：函数和序列
# 区别于map()：filter() 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素。
# 特点：此高阶函数，关键在于正确实现一个“筛选”函数；返回 Iterator 惰性序列。

# 示例一：在一个 list 中，删除偶数，只保留奇数。
def is_odd(n):
	return n % 2 == 1

L = [1, 2, 4, 5, 6, 9, 10, 15]
it = filter(is_odd, L)
print(list(it))	   # [1, 5, 9, 15]

# 示例二：将一个序列中的空字串删除。
def isEmptyChar(ch):
	return ch and ch.strip() 

print(list(filter(isEmptyChar, ['A', '', 'B', None, 'C', '']))) # ['A', 'B', 'C']

# 示例二：埃氏筛法计算素数。
# 埃氏筛法：
# 1）列出从 2 开始的所有自然数，构造一个序列；
# 2）取序列的第一个数 2，它一定是素数，然后用 2 把序列中 2 的倍数筛掉；
# 3）取新序列的第一个数 3，它一定是素数，然后用 3 把序列中 3 的倍数筛掉；
# 4）之后取新序列第一个数 5，一样的流程，如此便可得到所有素数。

# 1.构造一个从3开始的无限奇数序列/生成器
def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

# 2.定义一个筛选函数
def _not_divided(n):
	return lambda x: x % n > 0

# 3.定义一个生成器，不断返回下一个素数
def _primes():
	yield 2          # 先返回 2
	it = _odd_iter() # 初始序列
	while True:
		n = next(it) 
		yield n      # 每次返回序列的第一个数
		it = filter(_not_divided(n), it) # 取得的第一个数对序列中每个数进行除法运算筛选

# _primes() 是一个无限序列，调用时需要设置一个退出循环的条件
print('---素数---')
it = _primes()  # 返回 Iterator，所以 _primes() 生成器可以表示“全体素数”
for n in it:
	if n < 100:
		print(n) # 输出100以内的素数
	else:
		break	


# 练习：回数是从从左向右和从右向左读都是一样的数，如 12321，909。利用 filter() 过滤掉非回数。
# 1）定义一个从1开始的无限自然数序列
def allDigits():
	n = 0
	while True:
		n = n + 1
		yield n

# 2）判断一个数是否是回数
def isPalindrome(n):
	m = n
	p = 0
	q = 0
	while n != 0:
		p = n % 10
		q = q * 10 + p
		n = n // 10
	return m == q

# 3）获取自然数中的回数序列
def palindrome():
	it = allDigits()
	return filter(isPalindrome, it)

# 4）打印1-1000之间的回数。
print('---回数---')
it = palindrome()   
for n in it:       # 只有在循环取 filter() 结果时，才会真正筛选并每次返回下一个筛出的元素
	if (n < 1000):
		print(n)
	else:
		break


#############################################################
# 7. Python 内置函数之 sorted(list, key)
# 作用：sort() 接收一个 key 函数来实现自定义的排序，如按绝对值大小排序；
#      key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序。
# 说明：高阶函数，用 sorted() 排序的关键在于实现一个映射函数。

# 示例一：按绝对值大小排序列表。
L = [30, 5, -12, 9, -21]
print(sorted(L, key=abs))  # [5, 9, -12, -21, 30]

# 实例二：字符串排序，忽略大小写，按字母序列排序。
L = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(L, key=str.lower)) # 忽略大小写进行排序  # ['about', 'bob', 'Credit', 'Zoo']

# 实例三：对实例二中的字串进行反向排序，不改变 key 函数，传入第三个参数 reverse=True
print(sorted(L, key=str.lower, reverse=True))      # ['Zoo', 'Credit', 'bob', 'about']


# 练习：假设学生名字和成绩用tuple 表示，用 sorted() 对上述列表 按名字排序。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sort_by_name(tup):
	return str.lower(tup[0])

def sort_by_grade(tup):
	return tup[1]


# sort 作用在 tuple 的 名字元素
print(sorted(L, key=sort_by_name))  # [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
print(sorted(L, key=sort_by_grade)) # [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]



# ********************************************************* #

# 二、返回函数-闭包
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 示例一：不反悔求和的结果，二是返回求和的函数。
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum    # 返回求和的函数

# 调用 lazy_sum() 时，返回的并不是求和结果，而是求和函数
func_sum = lazy_sum(1, 3, 5, 7, 9)	# 返回求和函数	
print(func_sum)         # <function lazy_sum.<locals>.sum at 0x102198598>	
# 调用 func_sum 时，才真正计算求和的结果
print(func_sum())       # 25

# 说明：
# 1）在 lazy_sum() 函数中，定义了内部函数 sum()，其可以引用外部函数的参数和局部变量；
# 2）当 lazy_sum() 返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为 “闭包” 的程序结构有极大的威力。
# 3）每次调用 lazy_sum() 时，都会返回一个新的不等的函数，即使传入相同的参数。

# 1. 闭包（注：返回的函数没有立刻执行，而是知道调用 f() 才执行）
def count():
	fs = []
	for i in range(1, 4):
		def func():
			return i * i
		fs.append(func)
	return fs

f1, f2, f3 = count()
print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

# 注意，上述返回均为9，而不是1，4，9，原因在于返回的函数引用了变量 i ，但它并非立刻执行。
#    等到3个函数都返回时，它们所引用的变量 i 已经变成了 3，因此最终结果为 9。

# 记住：返回闭包时，返回函数不要引用任何循环变量 或者 后续会发生变化的变量。

# 问题：若一定要引用循环变量如何办？
# 方法：再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
	def func(j):
		def gunc():
			return j * j
		return gunc
	fs = []
	for i in range(1, 4):
		fs.append(func(i)) # 此处 f(i) 立刻被执行，因此 i 的当前值被传入 func()
	return fs			
f1, f2, f3 = count2()
print(f1()) # 1
print(f2()) # 4
print(f3()) # 9

# 闭包缺点：代码较长，可以使用 lambda 函数缩短代码。


# ********************************************************* #

# 三、匿名函数 lambda关键字
# 在传入函数时，有时不需要显式地定义函数，直接传入匿名函数更方便。

# 示例一：对 map() 传入匿名函数 lambda x: x * x
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5])))  # [1, 4, 9, 16, 25]

# 说明：
# 1）lambda 关键字表示匿名函数，冒号前面的 x 表示函数参数；
# 2）匿名函数有一个限制，就是只能有一个表达式，不用写 return，返回值就是该表达式的结果；
# 3）匿名函数的好处就是函数没有名称，不必担心函数名冲突；
# 4）匿名函数也是一个函数对象，可以把匿名函数赋值给一个变量，再利用变量调用该函数。

# 例如：lambda x: x * x 等价于：
# def f(x):
# 	return x * x

f = lambda x: x * x
print(f)    # <function <lambda> at 0x1022987b8>
print(f(5)) # 25

# 同样的，可以把匿名函数作为返回值返回，如以下所示：
def build(x, y):
	return lambda: x * x + y * y

func0 = build(2, 3)
print(func0) # <function build.<locals>.<lambda> at 0x101a986a8>
print(func0())	# 13

# 总结：Python 对匿名函数的支持有限，只在一些简单情况下才可以使用匿名函数。


# ********************************************************* #

# 四、装饰器
# 说明：
# 1）由于函数也是一个对象，可以被赋值给变量，因此，通过变量也能调用该函数；
# 2）函数对象有一个属性 __name__ ，可以获取函数的名字。

# 示例一：函数对象示例以及通过 __name__属性获取函数名。
def now():
	print('2017-09-13')

func1 = now
func1()  # 变量调用
print('func name =', func1.__name__, now.__name__)	# func name = now now

# 装饰器：若要增强 now() 函数的功能，如在调用前后打印日志，
#        但又不希望修改 now() 的定义，这种在代码运行期间动态增加功能的方式，称为“装饰器”。
# decorator 本质是是一个返回函数的高阶函数。
#【回顾：返回函数指函数可作为结果值返回（闭包）；高阶函数：函数作为变量名或者为另一个函数的参数】

# 示例二：定义一个能打印日志的 decorator.
def log(func):
	def wrapper(*args, **kw):  # 可变参数个数可为0-任意个
		print('call %s()' % (func.__name__))
		return func(*args, **kw)
	return wrapper

#  需要使用 Python的@语法，把 decorator 置于函数的定义处：
@log
def now():
	print('2017-09-13')	

now()  # call now()  2017-09-13	
# 上述调用 now() 函数，不仅会运行 now()函数本身，还会在运行now()前打印一行日志。
# 把 @log 放到 now() 函数定义处，相当于执行语句：  now = log(now)

# 上述 log 是 decorator 接收一个函数作为参数，并返回一个函数，
#      所以原来的 now() 函数仍然存在，只是现在同名的 now变量 指向了新的函数，
#      于是调用 now() 将执行新函数，即在 log()函数中返回的 wrapper() 函数。

# 示例三：若 decorator 本身需要传入参数，则需要编写一个返回 decorator 的高阶函数。
#		自定义 log 的文本。
def log(text):
	def decorator(func):
		def wrapper(*args, **kw):  # 可变参数个数可为0-任意个
			print('%s %s()' % (text, func.__name__))
			# wrapper.__name__ = func.__name__
			return func(*args, **kw)
		return wrapper
	return decorator

# 三层嵌套的 decorator，用法如下：
@log('log:execute')
def now():
	print('2017-09-13')			
now()                 # log:execute now() 2017-09-13
# 等价于 now = log('log:execute')(now) = decorator(now) = wrapper(now)

print(now.__name__)   # 此时返回的却是 wrapper ？？？
# 解释：因为最后返回的是 wrapper() 函数，所以需要把原始函数的 __name__ 等属性复制到 wrapper() 函数中，
#		否则有些函数依赖签名的代码执行就会出错。
# 改进：上述并不需要在 wrapper() 中重新对其 __name__ 属性赋值，可直接使用 Python 内置 functools.wraps .
import functools

def log(text):
	def decorator(func):
		@functools.wraps(func)     # 在最后一个返回函数定义前加上可解决上述问题
		def wrapper(*args, **kw):  # 可变参数个数可为0-任意个
			print('%s %s()' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('log:execute')
def now():
	print('2017-09-12')	
	
now()   			# log:execute now()  2017-09-12
print(now.__name__) # now	

# 练习：编写一个 decorator，在函数调用前后打印 'begin call' 和 'end call' 日志。
def my_log(*txt):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):	
			print('begin call')
			f = func(*args, **kw)  # 这里传入 now() 后调用
			if len(txt) != 0:
				print('end call log:', txt)
			else:	
				print('end call')
			return f
		return wrapper
	return decorator

# 调用一：不传参
@my_log()   # 问题：如果判断是否传入了参数 *txt 其实是一个 tuple
def now():
	print('2017-09-14')	
now()  # begin call  2017-09-13  end call

# 调用二：传入参数
@my_log('my_log_txt')   # 问题：如果判断是否传入了参数 *txt 其实是一个 tuple
def now():
	print('2017-09-14')	
now()  # begin call  2017-09-13  end call log: ('my_log_txt',)


# ********************************************************* #

# 五、偏函数
# Python 的 functools 模块：偏函数
# 偏函数：可以通过设定参数的默认值，降低函数调用的难度（对比函数参数-默认参数一节）。

# 示例一：int() 函数把字符串转换为整数，当仅传入字符串时，int() 默认转成十进制。
print(int('123'))          # 十进制数 123
print(int('123', base=8))  # 八进制 83
print(int('123', 16))      # 十六进制 291
# base 默认参数可以设置转换为几进制

# 实例二：定义一个直接将字符串转成二进制的函数，默认 base=2 传参。
def int2(x, base=2):
	return int(x, base)
print(int2('1000')) # 8，给 base=10后转换是十进制 1000

# 针对实例二，functools.partial 可以创建一个 偏函数，不需要我们自定义 int2()，创建如下：
import functools
int2 = functools.partial(int, base=2)
print('偏函数实现: ', int2('10000'))   # 偏函数实现: 32

# 总结：functools.partial 的作用是：
#			把一个函数的某些参数给固定住（也即是设置默认值），返回一个新的函数，调用这个新函数会更简单。

# 1）得到的偏函数，默认base 参数值为 2，但是在函数调用时可以设置 base=10 转换为十进制。
# 2）创建偏函数时，实际可以接受 函数对象、*args 和 **kw 这3个参数
#    如： int2('10010') -> kw = {'base': 2} int('10010', **kw)


# 示例三：以下 max2 偏函数创建，会把参数 10 作为 *arg2 的一部分自动加到左边
max2 = functools.partial(max, 10)  
print(max2(5, 6, 7)) # 10 等价于  args = (10, 5, 6, 7)  max(*args)

# 小结：当函数参数个数太多，需简化时，使用 functools.partial(函数，参数) 可创建一个新的函数，
#	 		这个新函数可以固定住原函数的部分参数，从而调用时更简单。




###########################
# 以下为 python_5_module 模块这一节内容的测试函数（作用域）
# 仅内部调用
def _isGirl(id):
	if id == 1:
		return True
	return False

# 供外部调用
def printGender(id):
	if _isGirl(id):
		print('She is a girl.')
	else:
		print('He is a boy.')














