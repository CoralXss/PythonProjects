# Python 内建模块
#   datetime
#   collections
#   base64
#   struct
#   hashlib
#   hmac
#   itertools
#   urllib
#   XML
#   HTMLParser

# 一、datetime

# 说明：Python 处理日期和时间的标准库。

from datetime import datetime

# 实例一：获取当前日期和时间。
def getCurrentTime():
	now = datetime.now()
	print(now)    # 2017-11-24 17:28:41.316997
getCurrentTime()

# 实例二：获取指定某个日期和时间。
def getDate(year, month, day, hour, minute, second):
	dt = datetime(year, month, day, hour, minute, second)
	return dt
print(getDate(2017, 11, 24, 17, 53, 50))   # 2017-11-24 17:53:50

# 实例三：将 datetime 转换为 timestamp .
def getTimeStamp(date):
	return date.timestamp()
dt = getDate(2017, 11, 24, 17, 53, 50)	
print(getTimeStamp(dt))  # 1511517230.0


# 说明：
# 1）from datetime import datetime - 从 datetime 模块导入 datetime 类；


