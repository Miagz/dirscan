# eccoding:utf-8
import os
import platform
os_system=platform.system()
if os_system != "Windows":
	path=os.path.abspath(os.path.dirname(__file__))
	dirscan_file=path+"/dirscan.py"
	try:
		oss="""echo  "alias dirscan='python3 %s'"  >>  ~/.bash_profile """%(dirscan_file)
		os.system(oss)
		os.system("source ~/.bash_profile")
	except:
		print("创建软连接失败")
	os.system("python3 -m pip install --upgrade pip")
	os.system("python3 -m pip install requests")
else:
	os.system("python3 -m pip install --upgrade pip")
	os.system("python3 -m pip install requests")
