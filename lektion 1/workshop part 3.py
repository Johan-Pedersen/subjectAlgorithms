from functools import reduce
#1
def apply_all(i, flist):
    result = i
    for l in flist:
        result = l(result)
    return result 

def add1(i):
    return i+1

def sub1(i):
    return i-1

print("#1",apply_all(1,[sub1,add1,add1, add1]))

#2
def mymap(func, vlist):

    myList = list()
    for i in vlist:
        myList.append(func(i))
    return myList

print ("#2",mymap(sub1, [1,2,3,4]))

#3
def myFilter(func, vlist):
    myList = list()

    for i in vlist:
        if(func(i)):
            myList.append(i)
    return myList

def even(i):
    return i %2 == 0

print("#3", myFilter(even, [1,2,3,4,5]))

#5

result = reduce((lambda x,y: x+y), range(1,101))

print("#5 ",result)

#6
def twice(func):
    def func2(a):
        b = func(a)
        return func(b)
    return func2

f = twice(add1)
print("#6 ", f((8)))


#7
add2 = lambda x: x+2
sub2 = lambda x: x-2

print("#7.1" ,apply_all(1, [add2, add2]))

def make_function(n):

    return lambda a: a+n

f = make_function(8)     
res = f(5)     
print("#7.3",res)

def twice2(func):
    return lambda x: func(func(x))

f = twice2(add1)
print("#7.4 ", f((8)))

#8
s=["hej", "heeeej", "hj", "heej"]
print("#8 ", sorted(s,key = lambda x: x.count("e"),reverse = True))