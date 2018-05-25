# question 7
def shippingCosts(n):
    # n cannot be 0
    cost = 0
    return 3+0.75*(n-1)

def totalCost(n, price):
    shipping = shippingCosts(n)
    books = price*60/100
    return shipping+books

def getTotal(price):
    n = input('How many books?')
    n = int(n)
    #print(n, type(n))
    return totalCost(n, price)

#print(getTotal(30))

# question 8
def toSeconds(h,m,s):
    return h*3600+m*60+s

def fromSeconds(s):
    import math
    h = math.floor(s / 3600)
    s = s % 3600
    m = math.floor(s / 60)
    s = s % 60
    return h,m,s

#print(toSeconds(2,30,20))
#print(fromSeconds(int(input('how many seconds? > '))))

def right_justify(str):
    #len(str) cannot be higher then 70
    n=70-len(str)
    return ' '*n + str

print(right_justify("what's up"))
