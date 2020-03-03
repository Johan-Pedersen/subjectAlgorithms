# tæl antal metode skridt for dynamisk løsning : n+1

#tidskompleksiteten: O(n)

# plads komplesksitet: værrer end den rekusive løsning fordi vi gemmer tallene

# iterativ løsning:

values = []


def fib_dyn(n):
    global values
    if len(values) == 0:
        values = [0]*(n+1)
        values[1] = 1
        values[2] = 1
    if values[n] != 0:
        return values[n]
    values[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return values[n]


valuesIt = []


def fib_dynIt(n):
    global valuesIt
    valuesIt = [0]*(n+1)
    valuesIt[1] = 1
    valuesIt[2] = 1

    for i in range(3, n+1):
        valuesIt[i] = valuesIt[i-1] + valuesIt[i-2]
        # print(valuesIt[i])
    return valuesIt[n]
# print(str(fib_dynIt(3)))


# opgaver rod cutting¨

def cut_rod_rek(prices, n):
    if n <= 0:
        return 0
    max_val = prices[n]
    for i in range(1, n):
        max_val = max(max_val, prices[i] + cut_rod_rek(prices, n-i))
    return max_val


prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print(cut_rod_rek(prices, 8))


arr = []


def cut_rod_dyn(prices, n):
    global arr

    if n <= 0:
        return 0

    if(len(arr) == 0):
        arr = [0] * (n+1)

    max_val = prices[n]

    for i in range(1, int(n)):
        if(arr[n-i] != 0):
            if(max_val < prices[i] + arr[n-i]):
                max_val = max(max_val, prices[i] + arr[n-i])
                print("pind skal skæres ved: ", len(arr) - 1 - i)

        else:
            temp = cut_rod_dyn(prices, n-i)
            if(max_val < prices[i] + temp):
                max_val = max(max_val, prices[i] + temp)
                print("pind skal skæres ved: ",  len(arr) - 1 - i)

    arr[n] = max_val
    return max_val


print(cut_rod_dyn(prices, 8))


# Hvor skal man skære pinden: Dette virker så længe pinden skal deles.


# Længeste fælles delstreng

# Delopgave 3:

str1 = "piskeris"
str2 = "malerisk"

a = [[0 for i in range(len(str1))] for i in range(len(str2))]

def printArr():
    print(" m  a  l  e  r  i  s  k")
    for row in a:
        print(row)

print("\n")
# delopgave 4:

def algo():

	for i in range(len(str1)):
		for l in range(len(str2)):
			if(str1[i] == str2[l]):
				a[i][l] = (a[i-1][l-1]) +1

algo()

printArr()