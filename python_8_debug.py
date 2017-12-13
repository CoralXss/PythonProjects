# 错误、调试和测试
#    错误处理
#    调试
#    单元测试
#    文档测试


############################################################
# 一、错误处理

# 1. try...except...raise...else...finally 机制
# 实例一：

import logging

class MyDivideError(ValueError):
	pass

def try_test():
	try:
		print('try...')
		r = 10 / 0
		print('result:', r)
	except ZeroDivisionError as e:
		print('catching error:', e)
		logging.exception(e)
		raise MyDivideError('invalid value: 0')
	else:
		print('no erro ! will be executed when there are no errors!')
	finally:
		print('finally... will always be executed whenever catching errors!')
	
# try_test()

# 打印结果如下：
# try...
# catching error: division by zero
# finally... will always be executed whenever catching errors!
# 异常捕获后抛出打印结果：
# __main__.MyDivideError: invalid value: 0

# 使用说明：
# 1）try 代码块防止代码出错，
#		出错后使用 except 代码块捕获，若没有错误则执行 else语句；
#			若想将错误抛给外层处理则使用 raise 抛出异常；
#	finally 语句块不管有没有发生错误均会执行该语句块。

# 2）except 代码块同于 catch，若错误类型包含父子关系，则父类会捕获该错误；
#	 所有的错误类型都继承 BaseException。

# 3）except...else... 发生了错误则执行 except 代码块，否则执行 else 语句；

# 4）logging.exception(e) 可以记录错误信息，便于事后排查；


############################################################
# 二、调试

# 方式一：使用 print() 打印；
# 方式二：使用断言 assert 替代用 print() 辅助查看的地方；
#			不同于 print()，断言可以在启动 Python解释器时通过 -o 关闭 assert;
# 方式三：使用 logging，此种方式不会抛出错误，而是将错误输出到文件；
# 方式四：使用调试器 pdb，让程序单步运行。（pdb调试暂时不学）

# 实例：使用断言调试。
def foo(s):
	n = int(s)
	# 该断言意思是，若 n!=0 则执行return语言，否则断言失败，assert语句抛出 AssertionError .
	assert n != 0, 'n is zero!' 
	return 10 / n

# foo('0')  # AssertionError: n is zero!
# 注：断言可以在运行时关闭： python -o python_8_debug.py

# 实例：使用 logging.
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 上述代码仅抛出 ZeroDivisionError，再没有其他信息
# 使用下属配置查看出错的堆栈信息：
logging.basicConfig(level=logging.INFO)

# logging 好处：允许指定记录信息的级别（debug, info, warning, error）		


############################################################
# 三、单元测试


############################################################
# 四、文档测试










