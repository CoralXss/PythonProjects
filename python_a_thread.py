# 进程和线程
#	多进程
#	多线程
#	ThreadLocal
#	进程 vs 线程
#	分布式进程

############################################################
# 一、前言

# 多任务
# 1）操作系统可以同时运行多个任务，如同时上网和听音乐；
# 2）单核CPU是如何执行多任务呢？ 
#	 OS轮流让个任务交替执行，由于CPU执行速度很快，感觉所有任务都是同时执行一样。
# 3）真正并行 执行多任务只能在多核CPU上实现，但任务数量总是多于CPU核心数量，所以OS会自动把多任务轮流调度到每个核心上执行。

# 4）对于OS来说，一个任务就是一个进程（Process）；
#	有些进程在同一时间会干多件事情，在一个进程内部，同时运行多个“子任务”，称为线程（Thread）；

# 5）如何同时开启多个线程，执行多个任务呢？
# 	 三种方式：多进程模式；进程内多线程模式；多进程+多线程模式。

# 6）进程间通信 & 线程间通信

# 7）Python支持多进程和多线程。

# 8）线程是最小的执行单元，进程至少有一个线程组成；
#    如何调度进程和线程，完全由OS决定，程序不能自己决定什么时候执行，执行多长时间。


############################################################
# 二、多进程

# os模块系统调用 fork() 创建子进程：

import os

def fork_test():
	print('Process (%s) start...' % os.getpid())
	# only works on Unix/Linux/Mac，Windows doesn't have fork()
	pid = os.fork()
	if pid == 0:
		print('I am child process (%s) and parent is %s .' % (os.getpid(), os.getppid()))
	else:
		print('I (%s) just created a child process (%s) .' % (os.getpid(), pid))	

# fork_test()
# 打印结果如下：
# Process (82518) start...
# I (82518) just created a child process (82519) .
# I am child process (82519) and parent is 82518 .
# 说明：
# 1）fork() 不同于普通函数调用一次返回一次，而是调用一次返回两次；
#	 因为os自动把当前进程（父进程）复制了一份（得到子进程），然后分别在父进程和子进程内返回；
# 2）子进程永远返回 0，父进程返回子进程的 ID；
#	 如此，一个父进程可以 fork 出许多子进程，然后记录每个子进程的 ID，子进程通过 getppid() 可以获取父进程ID；
# 3）有了 fork() 调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务；
#	 如常见的 Apatch 服务器就是父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的 http请求。

# 1. multiprocessing
#	Python 是跨平台的，multiprocessing 模块便是提供跨平台版本的多进程模块。

# 实例：
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
	print('Run child process % s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args = ('test', ))
	print('Child process will start.')
	p.start()
	p.join()
	print('Child process end.')

# 打印结果如下：
# Parent process 82546.
# Child process will start.
# Run child process test (82547)...
# Child process end.

# 说明：
# 1）multiprocessing 模块提供一个 Process 类来代表一个进程对象；
# 2）创建一个子进程，也即创建一个 Process 实例，只需传入 一个执行函数 和 函数的参数；
# 3）start() 方法为启动进程；
# 4）join() 方法表示为 等待子进程结束后再继续往下运行，通常用于进程间同步。

# 2. Pool
#	若要启动大量的子进程，可以用 进程池 的方式批量创建子进程。

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid))
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print('Task %s runs %0.2f senconds.' % (name, (end - start)))

# if __name__ == '__main__':
# 	print('Parent process %s.' % os.getpid())
# 	pool = Pool(4)
# 	for i in range(5):
# 		pool.apply_async(long_time_task, args = (i, ))
# 	print('Waiting for all subprocesses done...')
# 	pool.close()
# 	pool.join()
# 	print('All subprocessed done.')		

# 打印结果如下：
# Parent process 82556.
# Waiting for all subprocesses done...
# Run task 1 (<built-in function getpid>)...
# Run task 2 (<built-in function getpid>)...
# Run task 0 (<built-in function getpid>)...
# Run task 3 (<built-in function getpid>)...
# Task 3 runs 0.17 senconds.
# Run task 4 (<built-in function getpid>)...
# Task 4 runs 0.03 senconds.
# Task 2 runs 0.82 senconds.
# Task 0 runs 1.91 senconds.
# Task 1 runs 2.93 senconds.
# All subprocessed done.

# 说明：
# 1）Pool(4) 表示进程池中最多同时执行4个进程，所以创建5个进程时，会等前四个进程中有一个执行完成才开始执第5个进程；
# 2）Pool 默认大小是 CPU 核数；
# 3）对 Pool 对象调用 join() 方法前必须先调用 close()方法，
#	因为 join() 方法会等待所有子进程执行完毕，调用 close() 可以保证之后不再继续添加新的 Process。

# 3. 子进程
#	

# 4. 进程间通信
#	Python 的 multiprocessing 模块包装了底层的机制，提供 Queue、Pipes 等多种方式交换数据。

# 实例：以 Queue 为例，在父进程中创建两个子进程，一个往 Queue 中写数据，一个从中读取数据。

from multiprocessing import Process, Queue
import os, time, random

# 写数据进程
def write(queue):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		queue.put(value)
		time.sleep(random.random())

def read(queue):
	print('Process to read: %s' % os.getpid())
	while True:
		value = queue.get(True)
		print('Get %s from queue.' % value)

# if __name__ == '__main__':
# 	# 父进程创建 Queue，并传给各个子进程
# 	queue = Queue()
# 	process_write = Process(target = write, args = (queue, ))
# 	process_read = Process(target = read, args = (queue, ))

# 	# 启动写入数据子进程，开始写入：
# 	process_write.start()
# 	# 启动读取数据子进程，开始读取：
# 	process_read.start()

# 	#  等待 process_write 结束
# 	process_write.join()

# 	# 因为 process_read 是死循环，无法等待其结束，只能强制停止
# 	process_read.terminate()

# 打印结果如下：
# Process to write: 82583
# Put A to queue...
# Process to read: 82584
# Get A from queue.
# Put B to queue...
# Get B from queue.
# Put C to queue...
# Get C from queue.

# 注：进程间通信传递的数据对象必须通过 pickle 序列化，不然会失败。

# 总结：
# 1）Unix/Linux平台下，可以使用 fork() 调用实现多进程；
# 2）要实现跨平台的多进程，可以使用 multiprocessing 模块；
# 3）进程间通信是通过 Queue、Pipes 等实现。


############################################################
# 三、多线程
#	Python 标准库提供了另个模块：_thread 和 threading，
#	 前者是低级模块，后者是高级模块，是对_thread 的封装，一般地，只需要用到 threading 这个高级模块。

# 实例：创建线程并启动。
import time, threading

def loop():
	print('Thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('Thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(1)
	print('Thread %s ended.' % threading.current_thread().name)

# print('Thread %s is running...' % (threading.current_thread().name))
# thread0 = threading.Thread(target = loop, name = 'LoopThread')
# thread0.start()
# thread0.join()
# print('Thread %s ended.' % (threading.current_thread().name))	

# 打印结果如下：
# Thread MainThread is running...
# Thread LoopThread is running...
# Thread LoopThread >>> 1
# Thread LoopThread >>> 2
# Thread LoopThread >>> 3
# Thread LoopThread >>> 4
# Thread LoopThread >>> 5
# Thread LoopThread ended.
# Thread MainThread ended.

# 说明：
# 1）创建一个线程，就是把一个函数传入并且创建 threading.Thread 实例；
# 2）任何进程默认会启动一个主线程 MainThread，主线程可以启动新的线程；
# 3）threading.current_thread() 方法返回当前线程实例。

# 1. Lock
#	多进程和多线程的区别：
#	1）多进程中，同一个变量，各自有一份拷贝在每个进程中，互不影响；
#	2）多线程中，同一个变量都由所有线程共享；
#	3）所以，线程间共享数据最大危险在于多个线程同时修改一个变量的问题。（线程安全问题）

# 实例：多线程同时操作一个变量造成的线程安全问题。
import time, threading

# 银行当前存款
balance = 0

def change_it(n):
	# 先存后取，最后得到的余额不变为0
	global balance   # 定义一个全局变量
	balance = balance + n
	balance = balance - n

def run_multi_thread(n):
	for i in range(1000000):
		change_it(n)

lock = threading.Lock()	
def run_multi_thread_with_lock(n):
	for i in range(1000000):
		# 先获取锁
		lock.acquire()
		try:
			change_it(n)
		finally:
			# 执行完一定要释放锁
			lock.release()			

t1 = threading.Thread(target = run_multi_thread_with_lock, args = (5, )) 
t2 = threading.Thread(target = run_multi_thread_with_lock, args = (8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance) # 理论上结构为0，但是会因为多线程操作同一个变量而造成每次结果不一样

# 说明：
# 1）当 t1 t2 交替执行时，只要循环次数足够多，balance 结构就不一定为0；
# 2）原因在于高级语言中一条语句在 CPU 执行时是若干条语句，先计算后赋值给balance；
# 3）确保 balance 计算正确，需要给 change_it() 方法加锁，其他线程需要等待锁被释放后才能执行；

# 加锁防止线程安全问题：
# 1）如上，修改 target 方法为 run_multi_thread_with_lock；
# 2）加锁好处是保证线程安全，坏处是阻止了多线程并发执行，包含锁的代码只能单线程执行；
# 3）在存在多个锁的情况下，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能造成死锁，
#	导致多个线程全部挂起，不能执行也无法结束，只能强制终止。

# 2. 多核 CPU
# 1）如何在多核 CPU 时实现一个死循环？ 要想把 N核CPU全部跑满，则需要启动N个循环死线程。
# 2）Python 中，多线程只能交替执行，即使100个线程在100核CPU上，也只能用到1个核。
#	原因：Python解释器执行代码时，有一个 GIL（Global Interpreter Lock）锁，
#		 在执行线程前，必须先获得 GIL锁，然后每执行100条字节码，解释器就会自动释放 GIL锁，
#		 让别的线程有机会执行，这个 GIL全局锁实际上把所有线程的执行代码都上了锁，因此只会用到1核。
# 3）Python 中岁不能使用多线程实现多核任务，但是可以通过多进程实现，每个进程有独立的GIL锁。


############################################################
# 四、ThreadLocal

# 多线程情况下，使用线程局部变量 比 全局变量好，全局变量需要加锁。

# ThreadLocal，不用 dict 映射线程对应的变量，可保证当前线程维持自己的变量存副本。

import threading

# class Student(object):

# 创建全局 ThreadLocal 对象
local_school = threading.local()

def process_studet():
	# 获取当前线程关联的 student
	std = local_school.student
	print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
	# 绑定ThreadLocal的student
	local_school.student = name	
	process_studet()

t1 = threading.Thread(target = process_thread, args = ('Alice', ), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob', ))
t2.name = 'Thread-B'
t1.start()
t2.start()
t1.join()
t2.join()

# 打印结果如下：
# Hello, Alice (in Thread-A)
# Hello, Bob (in Thread-B)

# 说明：
# 1）全局变量 locak_school 为一个 ThreadLocal 对象，每个线程对其都可以读写 student 属性，互不影响；
# 2）可以将 ThreadLocal 对象理解为一个 dict，可以绑定其他变量；
# 3）ThreadLocal 常用于 为每个线程绑定一个数据库链接，Http请求，用户身份信息等。
# 4）一个 ThreadLocal 变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰，
# 5）ThreadLocal 解决了参数在一个线程中各个函数间互相传递的问题。













