# 面向对象编程
#    类和实例
#	 访问限制
#    继承和多态
#    获取对象信息
#    实例属性和类属性

############################################################
# 前言
# 1. OOP ，面向对象编程，把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 2. Python 中，所以数据类型都可以视为对象，也可以自定义对象。自定义对象数据类型就是 类（Class）的概念。
# 3. 面向对象的设计思想：抽象出 Class，根据 Class 创建 Instance .
# 4. 面向对象的抽象程度 比 函数高，因为一个 Class 既包含数据，又包含操作数据的方法。
# 5. OOP 三大特点：继承、封装 和 多态。

# 示例一：编写一个 Student 类，打印信息。
class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_info(self):
		print('%s: %s' % (self.name, self.score))	

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'			

# 创建对象，调用对象函数给对象发消息
bart = Student('Bart', 59)
lisa = Student('Lisa', 80)

print(bart)         # <__main__.Student object at 0x102a865f8> 打印实例（at 后面为内存地址）
print(Student)      # <class '__main__.Student'> 打印类

bart.print_info()   # Bart: 59
lisa.print_info()   # Lisa: 80
print(bart.get_grade()) # C


############################################################
# 一、类和实例

# 1）Python 中，定义类是通过 class 关键字，格式为：class Student(object): pass
# 2）class 后是类名，通常大写开头，object 表示该类是从哪个类继承而来。
#			一般若没有合适的继承类，则使用 object，所有的类均继承于 object .
# 3）__init__ 方法，在创建实例时，把必需的属性强制绑定上去。
#	 参数：第一个参数永远都是 self，表示创建的实例本身。
# 4）类中定义的函数 -> 类方法，第一个参数永远都是实例变量 self，调用时不用传递，
#			其他参数同于普通函数，可传入 默认参数、可变参数、关键字参数 和 命名关键字参数。

# 1、数据封装
# 一种写法，函数以类对象作为参数：
def print_stu(student):
	print('%s: %s' % (student.name, student.score))

# 调用
print_stu(bart) # Bart: 59

# 总结：
# 1）方法：与实例绑定的方法，和普通函数不通，方法可直接访问实例的数据；
# 2）不同于静态语言，Python 允许对实例变量绑定任何数据，
# 	  	也即，对于两个实例变量，虽然都是同一个类的不同实例，但拥有的变量名称 都可能不同！！！

# 示例二：对总结2）依旧针对上述 Student 类说明：

bart = Student('Bart', 59)
lisa = Student('Lisa', 80)
bart.age = 10

print('bart.age =', bart.age)  # bart.age = 10
# print(lisa.age)  # 因 lisa 对象没有绑定 age 属性，此处会报错：AttributeError: 'Student' object has no attribute 'age'


############################################################
# 二、访问限制
# 1）若要让内部属性不被外部访问，也即是 private 属性，在属性名称前加上两个下划线 __；
#		Python 中，实例的变量名若以 __ 开头，就变成了一个私有变量，只有内部可以访问，外部不能访问。

# # 改进类变量为私有变量 
class Student2(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_info(self):
		print('%s: %s' % (self.__name, self.__score))	

	def get_name(self):
		return self.__name	


bob = Student2('Bob', 9)
# print(bob.__name)   # 外部访问直接报错：'Student2' object has no attribute '__name'
# 但是 Python 中仍然可通过 _Student2__name 访问 __name 变量。
print(bob._Student2__name)

print(bob.get_name()) # Bob

# 说明：
# 1）修改类中私有变量，可提供 set 方法，相较于 直接通过 对象.属性名 = value ，
#		通过方法修改，可以对参数做检查，避免传入无效参数。
# 2）注意：在 Python 中，变量名 __xx__ 为特殊变量，可以直接访问，不是 private 变量，
#		所以在类中定义私有变量时，不能定义  __xx__ 变量。

# 注意以下写法会产生错觉，在外部直接给 __name 属性赋值，其实相当于重新创建了一个变量
jane = Student2('Jane', 10)
jane.__name = 'Coral'
print(jane.__name, jane.get_name()) # Coral Jane


############################################################
# 三、继承和多态
# 1）被继承的 class 称为基类、父类或超类；

class Animal(object):

	def run(self):
		print('Animal is running...')


class Dog(Animal):
	
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	
	def run(self):
		print('Cat is running...')			

dog = Dog()
dog.run()   # Animal is running... 重写了 run() 方法后， Dog is running...
cat = Cat()
cat.run()   # Animal is running... 重写了 run() 方法后， Cat is running...



a = list() # a 是 list 类型
b = Animal() # b 是 Animal 类型
c = Dog()  # c 是 Dog 类型

# 判断一个变量是否是某个类型可以用 isinstance() 判断：

print('a is list:', isinstance(a, list))     # True
print('b is Animal:', isinstance(b, Animal)) # True
print('c is Dog:', isinstance(c, Dog))       # True
print('c is Animal:', isinstance(c, Animal)) # True


# 这里的继承和多态 同于 Java，也遵循著名的“开闭”原则：
# 1）对扩展开放：允许新增 Animal 子类；
# 2）对修改封闭：不需要修改依赖 Animal 类型的 runTwice(Animal)，动态绑定Animal;


# 静态语言 VS 动态语言

class Timer(object):
	 def run(self):
	 	print('Time is flying...')


def run_twice(obj):
	obj.run()
	obj.run()

run_twice(Animal())  # Animal is runnung
run_twice(Dog())     # Dog is runnung
run_twice(Cat())     # Cat is runnung
run_twice(Timer())   # Timer is runnung

# 总结上面的实例，为什么传入 Timer() 也能调用 run() 方法？
# 1）对于静态语言（如 Java），若需要传入 Animal 类型，则传入的对象必须是 Animal 及其子类，否则无法执行 run() 方法；
# 2）对于动态语言 Python ，不一定需要传入 Animal 类型，只需要保证传入的对象有一个 run() 方法即可。
	# 因为 Python 中对参数/变量类型并没有指定，所以 只要对象有相同的方法，都可以传参。
# 3）动态语言的鸭子类型（一个对象只要看起来、走路像鸭子，就可以看做为鸭子） 特点决定了继承不像静态语言那样是必须的。


############################################################
# 四、获取对象信息
# 1.判断对象类型 —— type() 函数
#   作用范围：基本类型、指向函数或类的变量
#	返回值：对应的 Class类型

print(type(123))    # <class 'int'>
print(type(None))   # <class 'NoneType'>
print(type('str'))  # <class 'str'>
print(type(print))  # <class 'builtin_function_or_method'>
print(type(dog))    # <class '__main__.Dog'>

# 比较两个变量的 type 类型是否相同
def isSameType(x, y):
	print(type(x) == type(y))

isSameType(123, 234)   # True
isSameType(123, '123') # False
isSameType(Dog(), Animal()) # False

import types
# 是否为自定义函数
def isFunctionType(x):
	return type(x) == types.FunctionType

# 是否为系统函数
def isBuiltinFunctionType(x):
	return type(x) == types.BuiltinFunctionType		 

# 是否为 lambda 表达式
def isLambdaType(x):
	return type(x) == types.LambdaType

# 是否为生成器
def isGeneratorType(x):
	return type(x) == types.GeneratorType

print(isFunctionType(isSameType))    # True
print(isBuiltinFunctionType(abs))    # True
print(isLambdaType(lambda x: x * x)) # True
print(isGeneratorType((x for x in range(10)))) # True

# 2.使用 isinstance() 函数
# 区别于 type，对于 class 继承关系，不便使用 type()，要判断 class 类型，使用 isinstance() 函数
# 因为 type() 只能返回对象本身的类型，比如 type(dog) != type(animal)，
#								  但是 isinstance(dog, Dog) = isinstance(dog, Animal)

# 作用：判断一个对象是否是该类型本身，还是位于该类型的父继承链上。

# 能用 type() 判断的基本类型也可以用 isinstance() 判断：
print(isinstance('a', str))    # True
print(isinstance(123, int))    # True
print(isinstance(b'a', bytes)) # True

# 另外，isinstance() 还可以判断一个变量是否是某些类型中的一种：
# 判断变量是否是 list 或 tuple.
def is_list_or_tuple(x):
	return isinstance(x, (list, tuple))

print(is_list_or_tuple([1, 2, 3])) # True
print(is_list_or_tuple((1, 2, 3))) # True	  

# 3.使用 dir() 函数
# 作用：获取对象所有属性和方法
# 返回值：一个包含字符串的 list

# 获取一个 str 对象的所有属性和方法：
print(dir('ABC'))
print('ABC'.isdigit()) # False

# str 对象的几个方法： __len__()
# 说明： Python 中 __xxx__ 的属性和方法时有特殊用途的，如 __len__() 方法返回长度。
#  在 Python 中，若调用 len() 函数获取一个对象的长度，实际上在 len() 内部会自动调用对象的 __len()__ 方法：
#  所以若某个对象内部包含 __len__() 方法，就可以通过 len() 获取对象长度。


class MyList(object):

	def __len__(self):
		return 3

my_list = MyList()
print('len(my_list) =', len(my_list))  # len(my_list) = 3		

print('ABC'.__len__() == len('ABC'))   # True

# 4. 使用 getattr() setattr() 和 hasattr()
# 作用：使用上述方法直接操作一个对象的状态
# getattr() 获取对象某个属性的值或方法
# setattr() 为对象设置一个属性
# hasattr() 判断对象是否有某个属性或方法

class MyObject(object):

	def __init__(self):
		self.x = 9

	def power(self):
		return self.x * self.x

myobj = MyObject()	
# 判断对象是否
print(hasattr(myobj, 'x'))	# True	
print(getattr(myobj, 'x'), myobj.x)  # 9 9

# 若获取的属性不存在，则会抛出 AttributeError 错误，可以传入一个 default 参数，若不存在返回默认值：
print(getattr(myobj, 'z', 404))  # 404

print(hasattr(myobj, 'power'))   # True
fn = getattr(myobj, 'power')     # 获取方法后赋给一个变量
print(fn(), myobj.power())       # 81 81

print(dir(myobj))

# 正确的例子：
def printPower(x):
	if (hasattr(myobj, 'power')):
		myobj.x = x
		print(myobj.power())
	else:	
		print('has no power function !')	

printPower(10)  # 100


############################################################
# 五、实例属性和类属性
# 1）由于 Python 是动态语言，根据类创建的实例可以任意绑定属性。
# 2）给实例绑定属性的方法是通过实例变量 或者 通过 self 变量。

# 给实例绑定属性方式：
# 1）在 __init__(self, attr...) 中通过 self 绑定；
# 2）对象 obj.attr = xxx ，绑定新属性。

# 问题：如何给 Student 类本身绑定属性呢？
# 1）可以直接在 class 中定义属性，这种属性是类属性，归 Student 类所有，对比 Java 中静态变量。

# 示例一：给类绑定属性。
class Person(object):
	name = 'Person'

p = Person()
print(p.name)        # Person 打印name属性，因实例没有 name 属性，所有会继续查找 class 的 name 属性
print(Person.name)   # Person 打印类的name属性

p.name = 'Coralline' # 给 实例 绑定 name 属性
print(p.name)        # Coralline 由于实例属性优先级高于类属性，所以会屏蔽掉name属性
print(Person.name)   # Person    类属性依旧没有消失，仍可以访问

# 对于实例属性 和 类属性 总结：
# 1）实例属性和类属性不要使用相同的名字，因为相同名字的属性 实例属性会屏蔽掉类属性；

















