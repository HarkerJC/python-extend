#coding=utf-8
import  sys
import  test
print(sys.path)
# dir 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print(dir(sys))
# if we don't want to run the model part we can use __name__=="__main__"

#package 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包 用户可以每次只导入一个包里面的特定模块
# __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。