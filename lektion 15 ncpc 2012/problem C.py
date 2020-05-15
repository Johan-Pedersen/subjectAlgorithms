

#Line == String (starter med et mellemrum)

def bread(line: str):
    cookie = ""
    index = 0

    c = []
    c.append(" ")

    for i in range(len(line)):
        if line[i] == '#':

            #Send til packeting

            if len(c)-1 %2 == 0:
                index = (len(c) //2) +1
                cookie = c[index]
            else:
                index = (len(c) +1) //2
                cookie = c[index]

            c.pop(index)
            print(cookie)
        else:
            c.append(line[i])

bread("1234####")
print("\n")
bread("1#2#3#4#")