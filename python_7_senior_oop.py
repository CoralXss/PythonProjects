# 面向对象高级编程
#	 使用 __slots__
#	 使用 @property
#	 多重继承
#	 定制类
#	 使用枚举类
#	 使用元类


############################################################
# 一、使用 __slot__

# 问题：既然可以动态给实例绑定属性，那么如何给实例绑定一个方法？

class Student(object):
	pass

# 方式一：

def set_age(self, age):
	self.age = age

from types import MethodType
s = Student()
s.set_age = MethodType(set_age, s)   # 给实例绑定方法
s.set_age(24)  # 调用实例方法
print(s.age)   # 24

# 上述给实例绑定方法，只对当前实例有效，其他实例是无效的，
#		若需要对所以实例均有效，则应该 给 类 class 绑定一个方法。

Student.set_age = set_age   # 给类绑定方法
s1 = Student()
s1.set_age(20)
print('s1.age =', s1.age)   # s1.age = 20



# 方式二： 使用 __slots__，只允许对 Student 实例添加 name 和 age 属性。
# 说明：为了达到限制目的，Python 允许在定义 class 时，定义一个特殊的 __slots__ 变量来限制该 class 实例能添加的属性，
# 							也即是该类实例只能包含被限定的属性，动态对实例添加属性会报错。

class Person(object):

	__slots__ = ('name', 'age')  # 用 tuple 定义允许绑定的属性名称


p = Person()
p.name = 'xss'
p.age = 23

# p.score = 'A' 
# print(p.score)  # has no attribute 'score'


# 注：
# 1）__slots__ 定义的属性仅对当前类实例起作用，对其子类不起作用。
# 2）若要父类中的 __slots__ 也有效，则需要在子类中也定义 __slots__，
#			如此子类实例允许定义的属性就是自身的 __slots__ 加上父类的 __slots__ 。     
# 示例：验证 __slots__ 属性对子类不起作用。

class Teenager(Person):
	pass

t = Teenager()	
t.score = 'B'
t.name = 'coral'
print('t:', t.name, t.score)  # t: coral B


############################################################
# 二、使用@property

# 作用：限制属性的范围，保证属性值的合法性

# 一般地，若设置属性的值不合法，会在 setXxx() 方法中对值做校验，这种方法调用有时较复杂，
#		更简单的方式：使用 @property 装饰器将一个方法变成属性调用。

# 示例一：通过 set 方法来限制属性范围。
class Student0(object):

	# 一般写法对参数进行校验
	# def get_score(self):
	# 	return self._score

	# def set_score(self, score):
	# 	if not isinstance(score, int):
	# 		raise ValueError('score must be an integer !')
	# 	if score < 0 or score > 100:
	# 		raise ValueError('score must be between 0 ~ 100 !')
	# 	self._score = score


	#########################
	# 使用 @property 装饰器将一个方法变成属性调用

	# 添加 @property 把一个 getter 方法变成属性
	@property
	def score(self):
		return self._score

	# @property 本身又创建了另一个装饰器 @score.setter，负责把一个 setter 方法变成属性赋值，
	#		于是我们就拥有了一个可控的属性操作。
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer !')
		if value < 0 or value > 100:
			raise ValueError('score must be between 0 ~ 100 !')
		self._score = value	

	
	# 定义一套读写 _birth 属性方法
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value	


	# 定义只读属性，只定义 getter 方法，不定义 setter 方法
	@property
	def age(self):
		return 2017 - self._birth	


s0 = Student0()
s0.socre = 99
# s0.set_score('A')  # ValueError: score must be an integer !
# s0.set_score(9999) # ValueError: score must be between 0 ~ 100 !	
print('s0._socre =', s0.socre) # s0._socre = 99

# 示例二：使用 @property 装饰器将一个方法变成属性调用。 （详见 类Student0）
s1 = Student0()
s1.score = 80
s1.birth = 1993
# 打印：s1 info: birth = 1993 age = 24 score = 80
print('s1 info: birth = %d age = %d score = %d' % (s1.birth, s1.age, s1.score)) # ValueError: score must be between 0 ~ 100 !


# 练习：利用 @property 给一个 Screen 对象添加 width 和 height 属性以及一个只读属性 resolution .
class Screen(object):

	def __init__(self, width, height):
		self._width = width
		self._height = height

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height	

	@property
	def area(self):
		return self._width * self._height

	def printInfo(self):
		print('screen: %dx%d, area = %d' % (self._width, self._height, (self._width * self._height)))	

screen = Screen(100, 200)
# screen: 100x200, area = 20000
print('screen: %dx%d, area = %d' % (screen.width, screen.height, screen.area))

screen.width = 300
screen.height = 300
screen.printInfo()   # screen: 300x300, area = 90000
		
# 总结：@property 在类定义中被广泛应用，可以写出简短代码，
#		同时保证对参数进行必要检查，如此可减少程序运行时出错的可能性。


############################################################
# 三、多重继承（区别于 Java 的单继承，多实现）
# 动物：狗，蝙蝠，鹦鹉，鸵鸟
# 分类一：
	# 哺乳：狗，蝙蝠
	# 鸟类：鹦鹉，鸵鸟
# 分类二：
	# 能跑：狗，鸵鸟
	# 能飞：蝙蝠，鹦鹉
# 分类三：
	# 能跑的哺乳类，能飞的哺乳类
	# 能跑的鸟类，能飞的鸟类

class Animal(object):
	pass

# 哺乳和鸟类
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

# 行为：飞和行走
class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

# 各种具体动物

# 能行走的哺乳动物
class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flyable):
	pass

class parrot(Bird):
	pass

class Ostrich(Bird):
	pass

# 说明：
# 1）在设计类继承关系时，主线通常是单一继承，如 Bird 父类，
#		其他额外的功能，如 Flyable ，可以多重继承，这种设计通常称为 MixIn 。
# 2）为了更好地看出继承关系，可以将 跑和飞的行为方式 命名为 RunnableMixIn 和 FlyableMixIn 。
# 3）MixIn 目的是为了给一个类增加多个功能，这样，在设计类时，优先通过多继承来组合多个 MixIn 的功能，
#		而不是设计多层次的复杂继承关系。

# Python 中自带很多 MixIn，如 TcpServer 和 UDPServer 两类网络服务，
#				ForxingMixIn 和 ThreadingMixIn 多进程和多线程模型。

# 编写一个多进程模式的 TCP 服务：
# class MyTcpServer(TCPServer, ForkingMixIn):
# 	pass

# # 编写一个多线程的 UDP 服务：
# class MyUDPServer(UDPServer, ThreadingMixIn):
# 	pass


############################################################
# 四、定制类
# 类似继承下来的通用方法，可加上自己的定义，如 toString() 方法。 
#	如，Python 中的实现了 __len__()方法 可以让 class作用于 len() 函数。
# 下面介绍几种此类特殊用途函数，以此定制类。

# 1. __str__()
class Student1(object):
	def __init__(self, name):
		self.name = name

	# def __str__(self):
	# 	return 'Student object (name: %s)' % self.name

# 直接打印实例，类似 Java 中类的  toString() 方法
s1 = Student1('Coralline')
# 不实现 __str__() 方法，直接打印对象的到：<__main__.Student1 object at 0x10219e9b0>
print(s1) # 实现后打印：Student object (name: Coralline)

# 解释：直接打印对象，调用的是 __repr__() 方法，返回的是程序开发者看到的字符创；__str__()返回的是用户看到的字符串。

# 2. __iter__()
# 如果类想使用 for...in 循环，则必须实现 __iter__() 方法，该方法返回一个迭代对象，
#		之后for 循环不断调用该迭代对象的 __next__() 方法拿到循环的下一个值，直到遇到 StopIteration 异常对出循环。
# 以斐波那契数列为例，实现一个 Fib 类，能作用于 for 循环。
class Fib(object):
	def __init__(self, n):
		self.a, self.b = 0, 1 # 初始化两个计数器 a, b
		self.n = n

	def __iter__(self):
		return self           # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if (self.a > self.n):
			raise StopIteration()
		return self.a

	# __getitem__() 按下标取元素
	def __getitem__(self, n):
		a, b = 1, 1
		if isinstance(n, int):      # n 是整形索引
			for x in range(n):
				a, b = b, a + b
			return a	
		elif isinstance(n, slice):  # n 是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L				

	# 动态返回一个属性，在没有找到属性时才会调用 __getattr__() 查找，默认返回 None
	def __getattr__(self, attr):
		if attr == 'score':   # 返回属性值
			return 99
		elif attr == 'getage': # 返回函数
			return lambda: 24	
		raise AttributeError('\'Student1\' object has no attribute \'%s\'' % attr)	

# 使用
for n in Fib(20):
	print(n)		 # 1 1 2 3 5 8 13
					
# 说明，上述类虽然实现了 for 循环功能，但是依然不具备 list 的功能，如像list那样按下标取出元素，则需要实现 __getitem__()

# 2. __getitem__()
# 将实现 for 循环类，能通过下标取出元素。见 Fib 类。
f = Fib(100)
print('f[0] =', f[0]) # f[0] = 1
print('f[1] =', f[4]) # f[1] = 5

# list 有切片功能 lsit(range(100))[5:10]，如何让 Fib 类也实现切片功能呢？ 
#	见 Fib 类，对 __getitem__() 方法传入参数做判断，可能是 int，也可能是切片对象 slice .
print('f[0:5] =', f[0:5])     # f[0:5] = [1, 1, 2, 3, 5]
print('f[:10] =', f[:10])     # f[:10] = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print('f[:10:2] =', f[:10:2]) # 没有对 step做处理 [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# 3. __getattr__()
# 使用场景：当类没有某个属性时，使用会直接报 AttributeError，
#	要避免该错误，除了动态添加属性外，还可以通过 __getattr__() 方法，动态返回一个属性.
# 详见 Fib 类。

print(f.score)    # 99
print(f.getage()) # 24
# print(f.age)  # AttributeError: 'Student1' object has no attribute 'age'

# 总结：针对上述把一个类的属性和方法全都动态处理，可以实际用于完全动态的情况调用。
#		如 API 的 URL 调用。

# 实例：利用动态的 __getattr__() 实现链式调用。
class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))	

	def __str__(self):
		return self._path

print(Chain().status.user.list)  # /status/user/list		



############################################################
# 五、使用枚举类
# 一般地，定义常量的写法为 用大写变量通过整数来定义，如：JAN = 1;
#        优点：简单；缺点：类型是 int，并且仍是变量，值可改变。

# 解决：为上述枚举定义一个 class 类型，每个常量都是 class 的一个唯一实例。
# Python 提供 Enum 类来实现该功能：

from enum import Enum, unique

# 1. 定义 Week 枚举类
Week = Enum('Week', ('Mon', 'Tue', 'Wen', 'Thu', 'Fri', 'Sat', 'Sun'))

# 获取一个常量
# 打印：Week.Mon = Week.Mon 1
print('Week.Mon =', Week.Mon, Week.Mon.value)

# 枚举所有成员
for name, member in Week.__members__.items():
	print(name, '=>', member, ',', member.value)

# 打印结果如下：
# Mon => Week.Mon , 1
# Tue => Week.Tue , 2
# Wen => Week.Wen , 3
# Thu => Week.Thu , 4
# Fri => Week.Fri , 5
# Sat => Week.Sat , 6
# Sun => Week.Sun , 7

# 枚举说明：
# 1) value 属性时自动赋给成员的 int 常量，默认从 1 开始计数；
# 2）若需要更精确地控制枚举类型，可以从 Enum 派生出自定义类。

# 2. 自定义枚举派生类
# 导入 from enum import Enum, unique ，@unique装饰器可以保证无重复值

@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

# 不通方式获取枚举常量：一是成员名称，二是直接根据 value 值获取。
print('day1 =', Weekday.Mon)	         # day1 = Weekday.Mon
print('day2 =', Weekday['Tue'])          # day2 = Weekday.Tue
print('day3 =', Weekday(3))              # day3 = Weekday.Wed
print('day4.value =', Weekday(4).value)  # day4.value = 4
print('day5.value =', Weekday.Fri.value) # day5.value = 5

# 遍历所有枚举值
for name, member in Weekday.__members__.items():
	print(name, '=>', member)

# 打印结果如下：
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat

# 总结： Enum 可以把一组相关常量定义在一个 class 中，且 class 不可变，而且成员可以直接比较。
















