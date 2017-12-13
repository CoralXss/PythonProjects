from datetime import datetime

class DateUtils(object):

	def __init__(self):
		pass

	# 获取当前时间
	def getCurrentTime(self):
		return datetime.now();

	# 获取指定日期和时间
	def getDate(self, year, month, day, hour, minute, hour):
		return datetime(year, month, day, hour, minute, hour)	

	# 将日期转换为时间戳	
	def getTimeStamp(self, date):
		return date.timestamp()

	# 将时间抽转换为日期(本地时间-当前os设定的时区)
	def getLocalDateTime(self, timestamp):
		return datetime.fromtimestamp(timestamp)

	# 将时间抽转换为日期(UTC时间-UTC标准时区)
	def getUTCDateTime(self, timestamp):
		return datetime.utcfromtimestamp(timestamp) 	

    # 将时间字符串转换为日期
	def getTimeFromString(self, dateString):
		return datetime.strtime(dateString, '%Y=%m-%d %H:%M:%S')

	def getTimeString(self, date):
		return datetime.strftime('')		