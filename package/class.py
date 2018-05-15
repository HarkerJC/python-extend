class  People:

    #base property
    name=""
    age=0
    #private property other object can not visit

    __weight=0
    def __init__(self,name,age,weight):
        self.name=name
        self.age=age
        self.__weight+weight
        pass
    #private function
    def __run(self):
        print("run")
class Person(People):
    grage=''
    def __init__(self,name,age,weight,grage):
        People.__init__(name,age,weight)
        self.grage=grage

# mutiple extend class Person(Base1,Base2)

'''
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

'''
运算符重载
def __add__(self,other):
    return self.a+other.a
    
def __str__(self):
    return '这个人的名字是%s,已经有%d岁了！' % (self.name, self.age)
'''


