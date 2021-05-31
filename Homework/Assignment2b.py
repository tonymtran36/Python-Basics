#Warm-up
list = [1, "word", 3.14]

print(list)

l = [1,1,[1,2]]

print(l[2][1])

lst = ['a','b','c'] 
print(lst[1:])

my_dict = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
print(my_dict)

d={'k1':[1,2,3]} 
print(d['k1'][1])

list = [1,[2,3]]
t = list
print(t)

list1 = ['M','i','s','s','i','p','p','i']
s = set(list1)
print(s)

s.add('X')
print(s)

print(set([1,1,2,3]))

#problemset

#Question-1--------------------------------------------------------------
def findDiv7():
    for i in range(2000, 3200):
        if (i%7==0 and i%5!=0):
            print(i, end=", ")

findDiv7()

#Question-2--------------------------------------------------------------
def computeFactorial(num):
    if int(num) == 0:
        return 1
    return computeFactorial(num-1) * num

print("\nThis is question 2:")
x=input()
print(computeFactorial(int(x)))

#Question-3--------------------------------------------------------------
def dictIntegral(n):
    dict={}
    for i in range(1,n+1):
        dict[i] = i*i
    return dict


print("\nThis is question 3:")
x=input()
print(dictIntegral(int(x)))

#Question-4--------------------------------------------------------------
def to_list_tuple(str):
    list = str.split(",")
    t = tuple(list)
    return list, t


print("\nThis is question 4:")
x=input()
print(type(x))
print(to_list_tuple(x))

#Question-5--------------------------------------------------------------
class MyClass:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s=input()
    def printString(self):
        print(self.s)

q_five = MyClass()
q_five.getString()
q_five.printString()