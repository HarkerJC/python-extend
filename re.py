import re
#re.match(pattern,string,flags)  in the begining location if suc return object else return none
'''
import re 
print(re.match("www","www.baidu.com")) #
print(re.match("com","www.baidu.com")) #None
'''

'''
import re 
line="Cats are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?) .*',lines,re.M|re.I)
if matchObj:
    print(group())
    print(group(1))
    print(group(2))
else:
    print("no match")
    
    run result:
    
    matchObj.group() :  Cats are smarter than dogs
matchObj.group(1) :  Cats
matchObj.group(2) :  smarter
    
'''

'''
re.search 扫描整个字符串并返回第一个成功的匹配

re.search(pattern,string flags)

group(num=0) 匹配的整个表达式的字符串
groups()返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。


import re
print(re.search("www","www.runoob.com").span()) 
print(re.search("com","www.runoob.com").span())

以上实例运行输出结果为：

(0, 3)
(11, 14)
'''

'''
import re
line="Cats are more smarter than dogs"
searchObj=re.search(r'(.*) are (.*?) .*',line,re.M|re.I)
if searchObj:
    print(group()) #group(0)
    print(group(1))
else:
    print("not found")
    
    searchObj.group() :  Cats are smarter than dogs
searchObj.group(1) :  Cats
searchObj.group(2) :  smarter


'''

'''
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''

'''
re.sub 替换字符串中的匹配项。
re.sub(pattern,repla,string,count=0)
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

import re
phone = "2004-959-559 # 这是一个电话号码"

num=re.sub(r'#.*$',"",phone)
print(num)
num=re.sub(r'\D',"",phone)
print(num)

电话号码 :  2004-959-559 
电话号码 :  2004959559

repl 参数是一个函数

import re
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
'''

'''
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
re.compile(pattern,[flags])
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和' # '后面的注释

group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
span([group]) 方法返回 (start(group), end(group))。
'''

'''
findall
re.findall(pattern,start,end)
pos 可选参数，指定字符串的起始位置，默认为 0。
endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列

re.finditer
 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
 re.finditer(pattern, string, flags=0)
 import re
 
it = re.finditer(r"\d+","12a32bc43jf3") 
for match in it: 
    print (match.group() ) #match all
    
'''

'''
split 方法按照能够匹配的子串将字符串分割后返回列表
re.split(pattern, string[, maxsplit=0, flags=0])
maxsplit 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
>>>import re
>>> re.split('\W+', 'runoob, runoob, runoob.')
['runoob', 'runoob', 'runoob', '']
>>> re.split('(\W+)', ' runoob, runoob, runoob.') 
['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
>>> re.split('\W+', ' runoob, runoob, runoob.', 1) 
['', 'runoob, runoob, runoob.']
 
>>> re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
['hello world']
'''


'''
正则表达式对象

re.RegexObject
re.compile() 返回 RegexObject 对象。


re.MatchObject
group() 返回被 RE 匹配的字符串。

start() 返回匹配开始的位置
end() 返回匹配结束的位置
span() 返回一个元组包含匹配 (开始,结束) 的位置

'''