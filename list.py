# list can be modified but a tuple or a string can not
#append() add a element
list=[1,2,3,4]
list.append(5)
print(list)
#extend() add a list
list2=[6,7,8]
list.extend(list2)
print(list)
#insert(i,value) in the index i insert a value

list.insert(0,0)
print(list)
#pop([i]) remove the element in the index i and return else remove the last and return
pop1=list.pop(0)
print(list,pop1)
pop2=list.pop()
print(list,pop2)

#index(value) return the index that equals value
print(list.index(2))

#count(value) return the count in the list
print(list.count(3))

#sort()
list.sort()
print(list)
#reverse()
list.reverse()
print(list)
#copy()
#l=list.copy()
#print(l)

#clear() clear all the elements

#list.clear()

#stack append() and  pop()
#deque append() and pop(0) or append() and popleft()

vec=[2,4,6]
vec2=[x**2 for x in vec]
print(vec2)

#add if

vec3=[x**3 for x in vec if x>3]
print(vec3)


vec4=[x*y for x in vec for y in vec]
print(vec4)

#del del a bianliang

list=[1,2,3,4]
del list[0]
print(list)
a=3
#del a
print(a)