# 模块 ######
#    使用模块
#		作用域
#    安装第三方模块

# 模块说明：
# 1）为了式代码可维护，把很多函数分组，分别放在不同的文件中，
#		这样，每个文件包含的代码相对较少。
# 2）在 Python 中，一个 .py文件就称为一个模块（Module）。

# 模块的好处：
# 1）大大提高代码的可维护性；
# 2）当一个模块编写完毕，可以被其他地方引用；
# 3）避免函数名和变量名冲突（注意不要与内置函数名冲突）

# 为避免模块名有冲突，引入 包（package）.
# 说明：
# 1）创建顶层报名后，module.py文件代表的模块名 变成了 packageName.文件名；
# 2）注意每一个包目录下都会有一个 __init__.py 文件，该文件必须存在，否则 Python 会把该目录当成普通目录。


############################################################
# 一、使用模块

# 以下两行注释为标准注释
#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 表示模块的文档注释，任何模块代码的第一个字符串会被看为模块的文档注释
' a test module '         

# __author__ 变量写进作者，开源代码时可以看见作者名
__author__ = 'Coralline'

# 导入 sys 模块，使用 sys 变量可访问 sys模块的所有功能
import sys

def test():
	# sys.argv变量用 list 存储了命令行的所有参数，至少一个元素，第一个参数永远是 .py 名称
	args = sys.argv  
	if len(args) == 1:
		print('Hello, world!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

# 调用
if __name__ == '__main__':   
	test()


# 执行：python python_5_module.py , 返回：Hello, world!
# 执行：python python_5_module.py , 返回：Hello, world!

# 解释调用为什么要判断 函数名 = main ?
# 说明：在命令行运行 python_5_module 模块文件时，Python 解释器把一个特殊变量 __name__ 置为 __main__，
#		如果在其他地方 import python_5_module 时，该 if 判断会失效，类似 Java 中的 main() 运行测试。

# 如何调用导入模块中的函数？
# import python_5_module 声明后，调用 import python_5_module.test() 可调用 test() 函数。

# 1. 作用域
# 在一个 module 中，会定义很多函数和变量，但有的函数和变量希望能使用其他人提供，
#	有的仅希望在 module 内部使用，Python 中，通过 _ 前缀实现非公开的函数或变量。

# 1）类似 abc, PI 等正常的函数和变量名是公开的，可直接被引用；
# 2）类似 _xxx 和 __xxx 的函数和变量是非公开的，不能直接被引用；
# 3）类似 __xxx__ 的变量是特殊变量，可被直接引用，但是为特殊用途，如文档注释，一般变量不要用这种。

# 示例一：类似 Java 中只在本类调用的方法，可以声明为 private ，仅在本类中封装。
#		同理，Python 中的这种 private 函数，可将内部细节隐藏，是一种代码封装和抽象的方法。

# 仅内部调用
# def _isGirl(id):
# 	if id == 1:
# 		return True
# 	return False

# # 供外部调用
# def printGender(id):
# 	if _isGirl(id):
# 		print('She is a girl.')
# 	else:
# 		print('He is a boy.')	

############################################################


# 引入模块时会导致模块中能执行的语句全都执行，所以模块中一般都是函数和变量，没有函数调用
# import python_4_functional_programming

# 若没有加模块调用，抛异常：NameError: name '_isGirl' is not defined
# print(_isGirl(1))  

# 此种写法依旧是能运行成功的，Python中并没有严格限制访问 private 函数或变量，
#  只是一种编程习惯，最好不要出现如下写法
# print(python_4_functional_programming._isGirl(1))

# python_4_functional_programming.printGender(1)  # She is a girl.


# 二、安装第三方模块
# 简要介绍如何引用第三方模块











