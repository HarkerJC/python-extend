#format
#coding=utf-8
import  math
s="hello world {}"
s1=s.format("name")
print(s1)
print(math.pi)

f=open("foo.txt","r")
content=f.read()
print(content)
f.close()

f=open("foo.txt","r")
str=f.readline()
print(str)
f.close()

f=open("foo.txt","r")
lines=f.readlines()
for line in lines:
    print(line)
f.close()

f=open("foo.txt","w")
num=f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
f.close()

#seek() f.seek(offset, from_what) from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾
#f.seek(1,0)
#f.seek(2,1)

#model pickle restore adn read object diff from file

import  pickle
data1=[1,2,3,4]
data2=[5,6,7,8]
output=open("data.pkl","wb")
pickle.dump(data1,output)# restore the object
pickle.dump(data2,output)
output.close()

pkfile=open("data.pkl","rb")
data1=pkfile.load(pkfile)
data2=pkfile.load(pkfile)
pkfile.close()

#file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入

#file.tell() return the location of the file 




