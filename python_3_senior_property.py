# 高级特性 ################
#   切片
#   列表生成式
#   生成器
#   迭代器

# Python 中，代码不是越多越复杂越好，二是越少越简单才好。Python高级特性，1行代码能实现的功能决不用5行实现。

############################################################
# 一、切片操作：列表循环遍历 —> 切片操作符（简化取指定索引范围操作）

# 实例一：取列表的前三个元素并打印。
def traverseArr(L):
	r = []s
	n = 3
	for i in range(n):
		r.append(L[i])
	print('r = ', r)

L = ['Michale', 'Coralline', 'Cindy', 'Jane']
traverseArr(L)	

# 1. 切片优化 
print('L[0:3] =', L[0:3]) # 从索引0开始取，直到索引3为止，但不包括索引3
# 若第一个索引是0，可省略
print('L[:3] =', L[:3])

# 2. 取倒数第一个元素
print('L[-1] =', L[-1])  # L[-1] = Jane
print('L[-2:] =', L[-2:])  # L[-1] = ['Cindy', 'Jane']

# 3. 倒数切片
print('L[-2:-1] =', L[-2:-1])  # 取倒数第二个: L[-2:-1] = ['Cindy']

# 4. 切片的作用体现
# 创建0-99的数列
L = list(range(100))
print('列表前10个数：', L[:10])   # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('列表后10个数：', L[-10:])  # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print('列表前11-20个数：', L[10:20])
print('列表前10个数中，每两个取一个：', L[:10:2]) # [0, 2, 4, 6, 8]
print('列表所有数，每五个取一个：', L[::5])
print('复制一个列表：', L[:])

# tuple 不可变的切换操作
print('tuple前3个数：', (0, 1, 2, 3, 4, 5)[:3]) # tuple前3个数： (0, 1, 2)

# 字符串 ‘xxx’ 也可看做一种list，每个元素是一个字符，切片操作后仍是字符串
print('字串前三个字符：', 'ABCDEFG'[:3])    # 'ABC'
print('每两个取一个字符：', 'ABCDEFG'[::2]) # 'ACEG'

# 上述切片对字符创的操作，可以看做是大多编程于洋中对字符串的各种截取函数，如取字串。
# Python中没有针对字符串的截取函数，只需一个切片即可完成。


############################################################
# 二、迭代

# for 循环遍历可称为迭代。
# Python 的 for 循环不仅可用于 list 或 tuple，还可以作用在其他可迭代对象上。
# 只要是可迭代对象，无论有无下标，均可以迭代，如 dict:
def traverseDict():
	print('迭代遍历 dict: ')	
	d = {'a': 10, 'b': 12, 'c': 18}
	for key in d:
		print(key)
# 注：dict 的存储是无序的，list是有序的，所以迭代结果顺序会不一致	
traverseDict()  

# 字符串也是可迭代对象：
def traverseString():
	print('迭代遍历String字符串: ')
	for ch in 'ABC':
		print(ch)	
traverseString()

# 如何判断一个对象是可迭代对象呢？通过 collections 模块的 Iterable 类型判断：
from collections import Iterable
print('abc is iterable ? ', isinstance('abc', Iterable))  # 字符串是否可迭代？True
print('123 is iterable ? ', isinstance(123, Iterable))  # 整数是否可迭代？False
print('(123) is iterable ? ', isinstance((1, 2, 3), Iterable))  # Tuple是否可迭代？True

# for 循环中同时引用两个变量：
for x, y in [(1, 1), (2, 4)]: # list中存放tuple
	print(x, y)   # 1, 2    2, 4

for x, y, z in [{'a': 11, 'b': 12, 'c': 13}, {'a': 21, 'b': 22, 'c': 23}]:
	print(x, y, z)  # a b c    a b c   打印 key 值，且必选满足对应3个元素


############################################################
# 三、列表生成式
# 即 List Comprehensions，Python内置的超强大简单的可用于创建 list的生成式。

# 示例一：
L0 = [1, 2, 3, 4, 5]
L1 = list(range(1, 6))
print('L1 =', L1)     # L1 = [1, 2, 3, 4, 5]

# 示例二：生成1-10的平方数组成的数组。
# 一般写法：
L = []
for x in range(1, 11):
	L.append(x * x)
print('普通创建列表方法：', L)	

print('列表生成式创建列表：', [x * x for x in range(1, 11)])
print('列表生成式+条件筛选创建偶数平方数组：', [x * x for x in range(1, 11) if x % 2 == 0])
#  ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print('列表生成式生成全排列：', [m + n for m in 'ABC' for n in 'XYZ'])

# 示例三：列出当前目录下的所有文件和目录
import os
print('', [d for d in os.listdir('.')])

# 示例四：列表生成时使用两个变量生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print('', [k + '=' + v for k, v in d.items()])  # ['x=A', 'y=B', 'z=C']

# 示例五：把一个list中所有字符串变成小写
print('', [s.lower() for s in ['Hello', 'World', 'Apple']]) # ['hello', 'world', 'apple']

# 练习：列表中存储混合元素，但是整数没有小写方法需要先剔除
L = ['Hello', 'World', 18, 'Apple', None]
print('混合: ', [s.lower() for s in L if isinstance(s, str)]) # 混合 ['hello', 'world', 'apple']


############################################################
# 四、生成器
# 在 Python 中，一边循环一边计算的机制，成为生成器。（不用创建完整list 从而节省大量空间）

# 1. 列表生成器 和 生成器 的区别：一个是[]，一个是() 
# 2. 遍历生成器两种方式：一是 for 循环，二是不断调用 next() ，知道抛出异常为止。

# 列表生成器
L = [x * x for x in range(10)]

# 生成器
G = (x * x for x in range(10))
print('Generator =', G)
# 如何打印 generator 的每一个元素呢？
print('use next() to print: ', next(G)) # 0
print('use next() to print: ', next(G)) # 1
print('use next() to print: ', next(G)) # 4
print('use next() to print: ', next(G)) # 9
print('use next() to print: ', next(G)) # 16

# 上述是通过每次调用 next(g) 计算出 g 的下一个元素的值，知道计算最后一个元素，没有更多元素时，抛错。
# 正确写法可以使用 for 循环，因为 generator 也是可迭代对象，所以需少使用 next() 方法。
for n in G:
	print(n)

# 当推算算法比较复杂时，用类似列表生成式的 for 循环无法实现时，使用函数实现 Generator。
# 如，斐波拉契数列，用列表生成式无法实现，用函数实现如下：

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		# t = (b, a + b)
		# a = t[0]
		# b = t[1]
		n = n + 1
	return 'done'
print(fib(6))

# 总结： fib 函数实际上定义了斐波拉契数列的推算规则，从第一个元素开始，推算出后续任意的元素，逻辑上很像 generator.

def fib0(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b   # generator 遍历时，每次遇到 yield就返回，再次执行时从上次返回的 yield语句处执行。
		a, b = b, a + b
		# t = (b, a + b)
		# a = t[0]
		# b = t[1]
		n = n + 1
	return 'done'
print(fib(6))


# 注： yield 说明
# 1）若一个函数定义中包含 yield 关键字，则该函数就不再是一个普通函数，而是一个 generator；
# 2）generator 和 函数执行流程不一，函数时顺序执行，遇到return就返回，
#    而变成 generator 的函数，每次调用 next() 时执行，遇到 yield 语句就中断返回，
#		再次执行时从上次返回的 yield 语句处继续执行；
# 3）一般不用 next() 一个个取值，而是使用 for 循环遍历。

def yield_test():
	print('step 1')
	yield 1
	print('step 2')
	yield 2
	print('step 3')
	yield 3

it = yield_test()
print(next(it))   # step 1   1
print(next(it))   # step 2   2
print(next(it))   # step 3   3
# print(next(it))   # 抛出异常


############################################################
# 五、迭代器
# 1. 可直接作用于 for 循环的数据类型：
#    一类是集合数据类型，如 list, tuple, dict, set, str 等；
#    一类是 generator，包括生成器和带 yield 的 generator function.

# 2. Iterable可迭代对象: 这些可以直接作用于 for 循环的对象称为可迭代对象。
#    判断一个对象是否是 Iterable 对象： isinstance(obj, Iterable)

# 3. Iterator迭代器: 可以被 next() 函数调用并不断返回下一个值的对象称为迭代器。
#    判断一个对象是否是 Iterator 对象： isinstance(obj, Iterator)
#    生成器都是 Iterator 对象，可使用 next() 方法，但 list\dict\str 虽是 Iterable 但不是 Iterator.
#    如何将上述非 Iterator 对象转化为 Iterator 对象？使用 iter(obj)强转。

# 4. 为什么 list\dict\str 等数据类型不是 Iterator ?
#	 ——Python中，Iterator 对象表示的是一个数据流，Iterator 对象可以被 next() 函数调用并不断返回下一个数据，
#    直到没有数据时抛出 StopIteration 错误。  
#    可以把这个数据流看做是一个有序序列，但不知道序列的长度，只能不断通过 next() 函数实现按需计算下一个数据，
#    所以 【 Iterator 的计算是有惰性的，只有在需要返回下一个数据时才会计算。】

#    Iterator 可以表示一个无限大的数据流，如全体自然数，而使用 list 是永远不可能存储全体自然数的。


# from collections import Iterable
print(isinstance([], Iterable))    # True
print(isinstance({}, Iterable))    # True
print(isinstance('ABC', Iterable)) # True
print(isinstance([x for x in range(10)], Iterable)) # True
print(isinstance((x for x in range(10)), Iterable)) # True

from collections import Iterator
print(isinstance([], Iterator))    # False
print(isinstance({}, Iterator))    # False
print(isinstance('ABC', Iterator)) # False
print(isinstance([x for x in range(10)], Iterator)) # False 列表生成式
print(isinstance((x for x in range(10)), Iterator)) # True  生成器

# 转换为 Iterator
print(isinstance(iter([]), Iterator))    # True
print(isinstance(iter('ABC'), Iterator))    # True

# Python for 循环本质就是通过不断调用 next() 函数实现，如：

for x in [1, 2, 3, 4, 5]:
	pass

it = iter([1, 2, 3, 4, 5])  # 获得 Iterator 对象
while True:
	try:
		x = next(it)
		print(x)
	except StopIteration:
		# 遇到异常就退出循环
		break		




	

















