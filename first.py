# Hello, world

gradeDict = {'Michale': 95, 'Bob': 75, 'Coralline': 85}

print(gradeDict.get('key')) # None
print(gradeDict.get('key') == None) # True

if (not gradeDict.get('key')):
	print("right")

if (None):
	print('false')
else:
	print('true')	

if (not None):
	print('true')

if ('1'):
	print('1 right')	


# animals = ('cat', 'dog', 'parrot', 'bird')
# new_animal = ('sheep', )
# new_animals = animals, new_animal
# print(new_animals)
# print(new_animals[1][0])

student0 = {'s01': 'Amy', 's02': 'Cindy', 's03': 'Bob'}
print('s01 is', student0['s01'])

for number, name in student0.items():
	print('{} is Student {}'.format(number, name))

animals = ['cat', 'dog', 'parrot', 'bird']
print(animals[2])   # parrot
animals.insert(2, 'sheep')
print(animals)      # ['cat', 'dog', 'sheep', 'parrot', 'bird']


# 关于继承的几个问题
# 	1. 子类 能否继承 父类绑定的 属性？（每个类通过 self 或者 给实例动态绑定的 属性都是该类实例 独立拥有，跟子类没有任何关联？）
#		A: 子类不能继承 父类中通过 self或者 动态绑定的属性；

# 	2. 子类 是否只能继承 父类绑定的 类属性？
#		A：子类能继承 父类中的 类属性，在操作该类属性时，使用 ChildClass.property 访问该类属性；

# 	3. 子类可以继承 父类的所有方法？
#		A：Python 中方法没有 访问限制符修饰；

#   4. 子类和父类有同名的 属性，优先使用哪个？（避免这种情况，直接继承使用父类的属性）
#		A：有列举 tips 。

class Animal(object):
	animal_type = "animal"

	def __init__(self, name):
		self.__name = name
		self.age = 10
		print("Animal name")

	def parent(self):
		print("parent method")	

# animal = Animal("Panda")
# print(animal.__name)  # 直接报错没有该属性

class Dog(Animal):
	def __init__(self, name):
		# super(Dog,Animal.__init__()
		# self.__name = name
		print("Dog name")
		print(Dog.animal_type)  # animal

	def get_name(self):
		print(self.__name)	

	def get_age(self):
		print(self.age)	


dog = Dog("ddd")
print(dog)
# dog.get_name()    # 使用自身的 __name 属性
# dog.get_age()
dog.parent()        # parent method  子类能继承父类方法，但不能继承父类属性？？？




class Student(object):
	count = 0  # 类变量

	def __init__(self, name):
		self.name = name  # 实例变量
	
	def say_hi(self):
		print(r'Hello, I''m', self.name)


student = Student('Coral')
# grade是给实例动态绑定的属性，name是通过 self绑定的属性
student.grade = 90 
print('{} grade = {} '.format(student.name, student.grade)) 

student2 = Student('Jane')
# print(student2.grade)


def person(name, *habits, **friends):
	print('My name is', name)

	# 遍历tuple
	for item in habits: 
		print('My habits are:', item, end = ' ')

	print('')	
	# 遍历dict
	for name, city in friends.items():
		print('Friend name is', name, ' in', city)

person('Coral', 'Reading', 'Coding', Jane = 'Wuhan', Saint = 'Nanjing')



# 这里，如果默认参数位于可变参数之前，后面的可变参数就会覆盖默认参数的值，因此默认参数要放在后面。

str_test = 'Hello,World'

def reverse(s):
	return s[::-1]

def reverse2(s):
	if s == '':
		return s
	else:	
		return reverse2(s[1:]) + s[0] 	

print(reverse('Hello, World'))  # dlroW ,olleH
print(reverse2('Hello'))        # 递归：olleH

print('字串前三个字符：', 'ABCDEFG'[:3])    # 'ABC'

print(list(range(1, 9)))








