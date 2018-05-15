#CGI程序可以是Python脚本，PERL脚本，SHELL脚本，C或者C++程序等
'''
进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序

设置好CGI目录：
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
AddHandler 中添加 .py 后缀，这样我们就可以访问 .py 结尾的 python 脚本文件：
AddHandler cgi-script .cgi .pl .py
ontent-type:text/html"发送到浏览器并告知浏览器显示的内容类型为"text/html"。
默认情况下 cgi-bin 目录只能存放脚本文件
'''

'''
简单的url实例：GET方法
import cgi
form=cgi.FieldStorage()
#get data
site_name=form.getvalue("name")
site_url=form.getvalue("url")

print ("<h2>%s官网：%s</h2>" % (site_name, site_url))

'''

'''
在 http 协议一个很大的缺点就是不对用户身份的进行判断，这样给编程人员带来很大的不便， 而 cookie 功能的出现弥补了这个不足。

cookie 就是在客户访问脚本的同时，通过客户的浏览器，在客户硬盘上写入纪录数据 ，当下次客户访问脚本时取回数据信息，从而达到身份判别的功能，cookie 常用在身份校验中。


'''