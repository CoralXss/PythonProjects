import re
import os
import zipfile
import shutil


# 在 AndroidManifest.xml 文件中定义 meta-data，对不同的包替换该元素的 value，
# 最后在代码中可通过获取meta-data值渠道名称
# def replace_channel(channel, manifest):
# 	pattern = r'(<meta-data\s+android:name="channel"\s+android:value=""\s+/>)'
#     replacement = r'(<meta-data\s+android:name="channel"\s+android:value="{channel}"\s+/>)'
#     return re.sub(pattern, replacement, manifest)


# 'a' append追加模式
# zipped = zipfile.ZipFile('apk/app-release.apk', 'a', zipfile.ZIP_DEFLATED) 
# empty_channel_file = "original/META-INF/mtchannel_{channel}".format(channel='baidu')
# zipped.write('app-release/original/META-INF', "original/META-INF/mtchannel_{channel}".format(channel='baidu'))


# 解压缩apk
# os.system('apktool d -s apk/app-release.apk')
# replace_channel('_360', './apk/AndroidManifest.xml')

# 1. apktool解压 apk

# 美团多渠道混淆方案V1签名实现：
# 原理：向apk文件的 META-INF 目录下写一个空文件，可以不用重新签名应用；
#		通过为不同的渠道应用添加不同的空文件，可以标识一个渠道；
# 好处：因为不用重新签名，所以节省了解压重签名的时间；另外不同于原始的多渠道打包方案，build每次只打一个渠道包，构建时间很长
# 坏处：对于使用V2签名得到的apk进行修改，v2签名就会失效，此时安装到 7.0手机，会直接提示：检测使用V2签名，但是没有这样的签名；6.0手机安装时OK的。
# 解决方式：改成 V1 签名。

def buildChannelApk(apkFile, distChannelApks):
	print('---begin to write empty file into META-INF---')
	empty_file = "1.txt"
	f = open(empty_file, 'w')
	f.close()
	print('---write empty file into META-INF end---')

	orignialApkName = apkFile.split('apk')[0]
	os.mkdir(distChannelApks)

	# 读取文件中的 channels
	with open('channel', 'r') as f:
		channels = f.readlines()
		for c in channels:
				# 读取文件中的渠道id，strip()去除换行符
				# newFileName = "app-release-{channel}.apk".format(channel=c.strip()) 
				destApkFile = '%s/%s_%s.apk' % (distChannelApks, orignialApkName, c.strip())
				shutil.copy(apkFile, destApkFile) # 把原来的apk文件复制一份

				zipped = zipfile.ZipFile(destApkFile, 'a')
				empty_channel_file = "META-INF/ycchannel_{channel}".format(channel=c.strip())
				zipped.write(empty_file, empty_channel_file)
				zipped.close()

# V2签名失效
# buildChannelApk('apk/app-release-v2.apk', './channel_release_v2')

# V1签名
# buildChannelApk('apk/app-release-v1.apk', './channel_release_v1')

buildChannelApk('apk/app-huawei-release.apk', './channel_release_v4')


# # 2. 重新打包
# print('---begin to rebuild .apk---')
# channel_apk = "app-release-{channel}".format(channel='_360')
# os.system("apktool b app-release -o {channel_apk}.apk")
# print('---rebuild .apk end---')



# def getChannelsFromFile(fileName, manifest, buildSh):
	# 写法一：繁琐
	# try:
	# 	f = open(fileName, 'r')
	# 	print(f.read())
	# finally:
	# 	if f:
	# 		f.close()

# 	# 写法二：
	# with open('channel', 'r') as f:
	# channels = f.readlines()


