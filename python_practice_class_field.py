# 实例变量 和 类变量  实例方法 和 类方法

class Robot:

	# 统计机器人数量
	count = 0

	def __init__(self, name):
		self.name = name
		print('Initializing {}'.format(self.name))
		Robot.count += 1

	def die(self):
		print('{} is being destroyed!'.format(self.name))
		Robot.count -= 1

		if Robot.count == 0:
			print('{} was the last one.'.format(self.name))
		else:
			print("There are still {:d} robots working".format(Robot.count))	

	def say_hi(self):
		print("Greetings, my name is {}".format(self.name))

	@classmethod
	def get_count(cls):
		print('We have {:d} robots'.format(cls.count))			


# 调用
if __name__ == '__main__':
	robot1 = Robot('R1-01')
	robot1.say_hi()
	Robot.get_count()
	# Initializing R1-01
	# Greetings, my name is R1-01
	# We have 1 robots

	robot2 = Robot('R2-02')
	robot2.say_hi()
	Robot.get_count()
	# Initializing R2-02
	# Greetings, my name is R2-02
	# We have 2 robots

	print('\nRobots do some work here.\n')
	print('Robots hav finished their work. Destroy them.')

	robot1.die()
	# R1-01 is being destroyed!
	# There are still 1 robots working

	robot2.die()
	# R2-02 is being destroyed!
	# R2-02 was the last one.

	Robot.get_count()
	# We have 0 robots






