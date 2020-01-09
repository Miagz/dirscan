# dirscan
dirscan-web目录扫描工具<br>
&nbsp;&nbsp;dirscan是由python3编写，使用非常的灵活方便，dirscan是使用六个多线程扫描(由于本人比较懒,就没有自定义设置使用多少线程进行扫描，还望大家谅解~)<br>
<br>
&nbsp;&nbsp;dirscan能在linux和windows下面正常使用，但是在linux的环境下才能体现出它的强大功能(毕竟windows环境下有比这方便的工具.... )<br>
<br>
&nbsp;&nbsp;为了使用方便，我为大家准备了自动化配置脚本(必须有python3的环境下)。只需在dirscan目录下面执行 python3 setup.py就会自动配置dirscan所需的环境了
<br>
<br>linux的小伙伴如果想创建软连接，那么还需执行 soruce ~/.bash_profile 那么就会创建一个dirscan的快捷方式，如果想修改成别的，那请在setup.py里面修改
## 使用参数
 <br>-h,&nbsp;--help&nbsp;&nbsp;&nbsp;show this help message and exit
 <br>-u&nbsp;U&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;添加 url
 <br>-s&nbsp;S&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(可选)要添加的后缀名
 <br>-f&nbsp;F&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(可选)添加字典
