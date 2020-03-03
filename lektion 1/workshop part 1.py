'''
if 1==0 or 1==1:
    print("hej123")
else:
    print("hej321")



for i in {"hej": 1, "hej2": 2, "hej3": 3}.items():
    print(i, end =" ")


i = 1
while i != 101:
    print(str(i), end ="")
    i +=1

for l in range(1,101):
    print(str(l), end ="")
    i +=1



#8
myList = [0,1,2,3,4,5,6,7,8,9,10]

print (myList[::2])

#9
for i in range(1, 33):
    if 33 % i == 0:
        print(i, end =" ")
'''
#10
strList = ["to", "be" , "or",  "not", "to", "be"]

hejDict = dict()
for i in strList:
    try:
        d = {i: hejDict.get(i)+1}
        hejDict.update(d)
    except :
        hejDict[i] =1

print(hejDict)