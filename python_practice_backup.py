# 问题：实现一款能备份所有重要文件的程序。

# 第一版

import os
import time

# 1. 需要备份的文件与目录被指定在一个列表中
source = ['/Users/xss/commonUtil/apk_tool']

# 2. 备份文件必须存储在一个主备份目录中
target_dir = '/Users/xss/commonUtil/backup'

# 3. 将备份文件打包成zip文件，以以当前时间命名
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 目标目录不存在则创建目录
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

# 4. 使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is: ')
print(zip_command)

print('Running:')
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup failed')	