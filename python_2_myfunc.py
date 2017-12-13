# 定义函数

def my_print(msg):
	print('msg = ', msg)


# 完善：对参数类型做检查，只允许整数和浮点数，类型检查使用内置 isinstance()
def my_abs(n):
	# 检查参数类型，不符合抛出错误
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if n >= 0:
		return n
	else:
		return -n

def my_sum(n):
	sum = 0
	i = 1
	while i < n:
		sum = sum + i
		i = i + 1
	print('1 + 2 + ... + %d = %d' % (n, sum))





