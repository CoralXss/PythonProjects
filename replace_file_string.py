import re  


def replaceStr(file):
	f = open(file,'r')  
	content = f.read() 

	# print(content) 
	# \b@BindView(.*?)\b 

	content = '@BindView(R.id.k)'
	# /aa.+aa/

	p2 = re.compile('/@BindView(R.id..+)/')   # @BindView(R.id.[\s\S]*?)  \b@BindView(.*?)\b
	m2 = re.findall(p2, content) 

	print('m2 = ', m2)
 
	if m2:  
	    for i in m2:  
	        print(i) 

replaceStr('/Users/xss/Documents/GoodsFragment.java')
