'''
#1
def myfunc(a):
    print("This is the parameter: " + str(a))

myfunc(8)

myfunc([1,2,3])

def more(a, b):
    print("a is " + a)
    print("b is " + b)

more(a ="aa", b ="bb")

#2
def upto(n):
    result = 0
    i = 0
    for i in range(n+1):
        result +=i
    return result

print(upto(2))


#3
def addall(alist):
    result = 0
    for i in alist:
        if type(i) == int:
            result += i
    return result

print(addall(["hello world", 1,2,3,4,5,6]))

#4:
def reverse(alist):
    return alist[::-1]

print(reverse([1,2,3,4]))



#5
minmax = lambda alist : (min(alist),  max(alist))

print(minmax([1,2, 99,3]))

#6
def evennumbers(alist):
    blist = list()
    for i in alist:
        if(i %2 == 0):
            blist.append(i)
    return blist

print(evennumbers([1,2,3,5,4]))


#skal laves om i morgen
#7
def fib(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return fib(n-1)+fib(n-2)

print(fib(3))

list1 = [1,2,3]
list2 = list1
list1[0] = 99

print(list2)



#spørg om Jørn kan forklare dette:
def f(list):
    print(list)    
    list[0] = 99    
    print(list)

numbers = [1,2,3]
print('numbers:', numbers)
f(numbers)
print('numbers:', numbers)

def f2(list):
    print(list)
    list = [7,3,2]
    print(list)

numbers = [1,2,3]
print('numbers:', numbers)
f2(numbers)
print('numbers:', numbers)


#10
def inc_list(alist):
    listReturn = list()
    for i in alist:
        listReturn.append(i+1)

    return listReturn

print(inc_list([1,2,3,4]))
'''


#12
def countwords(alist):
    hejDict = dict()
    for i in alist:
        try:
            d = {i: hejDict.get(i)+1}
            hejDict.update(d)
        except :
            hejDict[i] =1
    return hejDict

d = countwords(["to","be","or", "not", "to", "be"])

print(d)
