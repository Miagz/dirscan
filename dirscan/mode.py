# encoding:UTF-8
import threading
import requests
import os
import re
path=os.path.abspath(os.path.dirname(__file__))
dict_path=path+"/bpdict/"
def mode1(url,cs):
        file=open('%slist1.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mode2(url,cs):
        file=open('%slist2.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mode3(url,cs):
        file=open('%slist3.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mode4(url,cs):
        file=open('%slist4.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mode5(url,cs):
        file=open('%slist5.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mode6(url,cs):
        file=open('%slist6.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s.%s"%(file,cs)
            new_url=url+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def main(url,cs):
    t1 = threading.Thread(target=mode1,args=(url,cs))
    t1.start()
    t1.join()    

    t2 = threading.Thread(target=mode2,args=(url,cs))
    t2.start()
    t2.join()

    t3 = threading.Thread(target=mode3,args=(url,cs))
    t3.start()
    t3.join()

    t4 = threading.Thread(target=mode4,args=(url,cs))
    t4.start()
    t4.join()

    t5 = threading.Thread(target=mode5,args=(url,cs))
    t5.start()
    t5.join()

    t6 = threading.Thread(target=mode6,args=(url,cs))
    t6.start()
    t6.join()
    
"""............................................................................................................................................."""
def file1(url):
        gets=url
        file=open('%slist1.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status>= 200:
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def file2(url):
        gets=url
        file=open('%slist2.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def file3(url):
        gets=url
        file=open('%slist3.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def file4(url):
        gets=url
        file=open('%slist4.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))

def file5(url):
        gets=url
        file=open('%slist5.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :  
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def file6(url):
        gets=url
        file=open('%slist6.txt'%(dict_path))
        new_file=file.readlines()
        for files in new_file:
            file=files.strip()
            code="%s"%(file)
            new_url=gets+code
            new_get=requests.get(new_url)
            status=new_get.status_code
            if 400>status >= 200 :
                print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
def mains(url):
    i1 = threading.Thread(target=file1,args=(url,))
    i1.start()
    i1.join()    

    i2 = threading.Thread(target=file2,args=(url,))
    i2.start()
    i2.join()

    i3 = threading.Thread(target=file3,args=(url,))
    i3.start()
    i3.join()

    i4 = threading.Thread(target=file4,args=(url,))
    i4.start()
    i4.join()

    i5 = threading.Thread(target=file5,args=(url,))
    i5.start()
    i5.join()

    i6 = threading.Thread(target=file6,args=(url,))
    i6.start()
    i6.join()

"""-------------------------------------------------------------------------------------------------------"""

def modefile(url,fileoption,suffix):
    if suffix =="":
        suffixs=suffix
    else:
        suffixs="."+suffix
    print("url:"+url)
    file=open("%s"%(fileoption),encoding="latin-1")
    print("filepath:"+fileoption)
    new_file=file.readlines()
    for files in new_file: 
        file_path=files.strip()
        file_path=re.sub(r"^/","",file_path)
        new_url=url+file_path+suffixs
        new_get=requests.get(new_url)
        status=new_get.status_code
        if 400>status >= 200 :
            print("[+] STATUS:[%d]  URL:%s"%(status,new_url))
    
        
def mainf(url,fileoption,suffix=""):
    modefile(url,fileoption,suffix)



