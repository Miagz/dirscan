# encoding:utf-8
import requests
import argparse
import sys
import re
from mode import main,mains,mainf
parser=argparse.ArgumentParser()
parser.add_argument('-u',type=str,help='添加 url')
parser.add_argument('-s',type=str,help='(可选)要添加的后缀名')
parser.add_argument('-f',type=str,help='(可选)添加字典')
args=parser.parse_args()
files = re.search(r"^http://(.*)$|^https://(.*)",args.u)
pd=re.search(r"/$",args.u)
if files==None:
    print("请添加 http:// 或 https:// !")
    sys.exit()
if pd==None:
    args.u=args.u+"/"
ok="""
                             ^
         .                   |                     .
 .                           |
                             |       .                       o
          .                  .              
                             |       
                          <==O==>
                             |
                             。   
                          dirscan
		       web目录扫描工具
         .        
                                                   .
        o                 
                            
"""
print(ok)
try:
	if args.u and args.f and args.s:
		print("suffix:%s"%(args.s))
		mainf(args.u,args.f,args.s)
		print("爆破完成")
		sys.exit()
	if args.u and args.f :
		mainf(args.u,args.f)
		print("爆破完成")
		sys.exit()
	if args.u and args.s:
		print('suffix:%s'%(args.s))
		main(args.u,args.s)
		print("爆破完成!")
		sys.exit()
	if args.u:
		mains(args.u)
		print('爆破完成')
		sys.exit()
except:
	print("程序出现了无法描述的错误\n可能是以下原因:\n  1.此域名没有添加 ssl证书\n  2.指定文件路径出现了问题")
	sys.exit()
