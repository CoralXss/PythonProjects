# 函数（http://docs.python.org/3/library/functions.html#abs）

# 一、内置函数：Python 内置了很多函数可以直接调用：

# abs() 函数，只能有一个参数
print('abs(-10) =', abs(-10))

# max() 函数，可以接收多个参数，并返回最大的数，但是不能 整数和字串比较
print('max(2, 5, 3, 9, -1) =', max(2, 5, 3, 9, -1))     # 9
print("max('coral', 'bella') =", max('coral', 'bella')) # coral
print(max(9, 2.0)) # 9

# 数据类型转换函数，int()函数 -> 将其他数据类型转为整数
print(int('123')) # 123
print(int(12.34)) # 12
print(int(12.59)) # 12
print(int(-11.2)) # -11
print(int(-11.5)) # -11

print(str(1.23))  # 1.23

print(bool(1))    # True
print(bool(''))   # False

# 给函数起别名：将函数名赋给一个变量
a = abs
print(a(-1))  # 1


# 二、定义函数
# 使用 def语句，格式： def 函数名(参数名): 在缩进块中写函数体，return 返回值

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x

print('my_abs(-2) =', my_abs(-2)) # my_abs(-2) = 2

# 函数引用：若在文件 myfunction.py 中定义了函数 my_abs() ，则
from python_2_myfunc import my_sum
my_sum(10)  # 1 + 2 + ... + 10 = 45

# 空函数：一个什么事都不做的空函数，用 pass 语句
def pop():
	if (True):
		pass
	pass  # pass 可以作为占位符，如没想好函数体，可先放一个pss，让代码跑起来

# 函数返回多个值，其实是一种假象，返回仍是单一值，且是一个 tuple 
import math  # 表示导入 math包
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

# move:  (151.96152422706632, 70.0)	
print('move: ', move(100, 100, 60, math.pi / 6))

# 总结：
# 1. 定义函数时，需要先确定函数名和参数个数；
# 2. 若有必要，可以先对参数进行数据类型检查；
# 3. 函数体内部可以用 return 随时返回函数结果；
# 4. 函数无返回数据执行 return 时，自动 return None;
# 5. 函数可以同时返回多个值，但其实就是一个 tuple。

# 练习
import math
def quadratic(a, b, c):
	if (a == 0):
		if b:
			return c / b
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return x1, x2

print(quadratic(2, 3, 1))  # (-0.5, -1.0)
print(quadratic(0, 3, 1))  # 0.3333333333333333
print(quadratic(1, 3, -4)) # (-0.5, -1.0)


# 三、函数的参数

# def power(x):
# 	return x * x
# print(power(2))  # 4

# 默认参数 n = 2，当调用 power(5) = power(5, 2)，
# 也即是一个参数时，默认计算平方， n>2 ，则计算 x 的n次方
def power(x, n = 2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
print(power(5, 3))	# 125	

# 1. 默认参数
# 说明：1）必选参数在前，默认参数在后，否则解释器会报错；
#      2) 如何设置默认参数？当函数有多个参数时，把变化大的参数放前面，变化小的放后面，变化小的参数就可作默认参数。
# 好处：降低调用函数的难度，无论简单还是复杂调用，函数只需要定义一个。

# 例子：将年龄和城市设置为默认参数
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name: %s, gender: %s, age: %d, city: %s' % (name, gender, age, city))
enroll('Coral', 'Female')
enroll('Coral', 'Female', 24)
# enroll('Coral', 'Female', 'Shanghai')  # 报错
enroll('Coral', 'Female', 24, 'Shanghai')

# name: Coral, gender: Female, age: 6, city: Beijing
# name: Coral, gender: Female, age: 24, city: Beijing
# name: Coral, gender: Female, age: 6, city: Shanghai
# name: Coral, gender: Female, age: 24, city: Shanghai

# 默认参数特殊情况
def add_end(arr = []):
	arr.append('END')
	return arr
print(add_end())  # ['END']
print(add_end())  # ['END', 'END']

# 注：这里有一个问题，默认参数为 [] ，L为变量指向对象[]，
# 每次调用该函数，若改变了 L 的内容，下次调用时，默认参数内容就改变，不在是函数定义时的 [] 了。
# 因此，默认参数必须指向不变对象！

# 修改上述函数
def add_end2(arr = None):
	if arr is None:
		L = []
	L.append('END')
	return L	
print(add_end2())  # ['END']
print(add_end2())  # ['END'] 为 None 时重新赋值


# 2. 可变参数
# 说明：传入参数个数可变，在函数调用时，自动组装为一个 tuple
# 例子： 计算 a2 + b2+ ...

# 方式一：参数以 list 或者 tuple 传入
def calculate(numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum	
print('cal(1, 2, 3) =', calculate([1, 2, 3]))   # cal(1, 2, 3) = 14
print('cal(1, 2, 3, 4, 5, 6) =', calculate([1, 2, 3, 4, 5, 6]))  # cal(1, 2, 3, 4, 5, 6) = 91

# 方式二：可变参数-参数个数可变
def calculate2(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum	
print('cal(1, 2, 3) =', calculate2(1, 2, 3))   # cal(1, 2, 3) = 14
print('cal(1, 2, 3, 4, 5, 6) =', calculate2(1, 2, 3, 4, 5, 6))

# *nums 将一个数组的所有元素都作为可变参数传入
nums = [1, 2, 3]
print(calculate2(*nums))


# 3. 关键字参数
# 说明：允许传入0-n个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict。

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)              # name: Michael age: 30 other: {}
person('Bob', 35, city='Beijing')  # name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer')    # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
myDict = { 'city': 'Beijing', 'job': 'Engineer' }
person('Jack', 20, **myDict)       # name: Jack age: 20 other: {'city': 'Beijing', 'job': 'Engineer'}
# 注：kw 获得的dict是 myDict 的一份拷贝，对 kw 的改变不会影响到函数外的 myDict 。


# 4. 命名关键字参数：限定只接受某几个参数，使用 * 标志其后面的参数为命名关键字参数。
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

person2('Jane', 1, 'hello', city = 'shanghai', job = 'Paint')


# 5. 多个参数组合，单参数定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数 和 关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

########################################################
# 四、递归函数

# 1. 计算阶乘 n! = 1 * 2 * ... * n .
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)

print('fact(%d) = %d' % (5, fact(5)))

# 注：类似 fact(n) 递归函数要防止栈溢出，递归调用次数过多，会导致栈溢出。
# 解决递归调用栈溢出方法：尾递归优化，在函数返回时，调用自身本身，并且 return 语句不能包含表达式。
# 改变上述递归为尾递归：
def fact2(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if (num == 1):
		return product
	return fact_iter(num - 1, num * product)

print('fact2(%d) = %d' % (5, fact2(5)))

# 练手：汉罗塔，打印出把n个盘子从A借助B移动到C的方法，n表示3个柱子中第一个柱子A的盘子数量。
def move(n, a, b, c):
	if n == 1:
		printStep(n, a, b, c)
	else:
		move(n - 1, a, c, b) # 将 n-1 个盘子从 A -> B
		move(1, a, b, c)     # 将最底下一个从 A -> C
		move(n - 1, b, a, c) # 将剩余 n-1 个盘子从 B -> A （一轮结束，重复上述步骤）	


def printStep(n, first, second, third):
	if (n == 1):
		print('把第%d个盘子从%s -> %s' % (n, first, third))
	else:
		print('把剩余%d个盘子从%s -> %s' % (n, first, third))
					
move(3, 'A', 'B', 'C')

			
















