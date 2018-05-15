import  sys
# if a function has yield it will be a generator and  return a iterator
def f():
    list=[1,2,3,4]
    for i in list:
        yield i
f=f() #return a iterator
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()