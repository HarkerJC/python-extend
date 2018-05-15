# next() only go ahead not go back
import  sys
list=[1,2,3,4]
it=iter(list)
print(next(it))
print(next(it))

for i in it:
    print(i)

while True:
    try:
        next(it)
    except StopIteration:
        sys.exit(0)