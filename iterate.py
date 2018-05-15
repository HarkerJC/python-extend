a=[1,2,3,4]
b=[4,5,6,7]
for i,v in enumerate(a):
    print(i,v)
#iterate two or more serize can use zip()
for a_item,b_item in zip(a,b):
    print(a_item,b_item)

# sorted() return a sorted list but no change value

c=[4,3,2,1]
for c_item in sorted(c):
    print(c_item)
for c_item in c:
    print(c_item)