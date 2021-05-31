def square(num):
    return num**2

my_nums = [1,2,3,4,5]

map(square,my_nums)

# To get the results, either iterate through map() 
# or just cast to a list
print(list(map(square,my_nums)))

def splicer(mystring):
    if len(mystring) % 2 == 0:
        return 'even'
    else:
        return mystring[0]
mynames = ['John','Cindy','Sarah','Kelly','Mike']
print(list(map(splicer,mynames)))


def check_even(num):
    return num % 2 == 0

nums = [0,1,2,3,4,5,6,7,8,9,10]
filter(check_even,nums)

print(list(filter(check_even,nums)))

def square(num): #1st
    result = num**2
    return result

print(square(2))

def square(num): #2nd
    return num**2

print(square(2))

def square(num): return num**2 #3rd

print(square(2))

square = lambda num: num ** 2 #4th lambda
print(square(2))

lst1=list(map(lambda num: num ** 2, my_nums))
print(lst1)

lst2=list(filter(lambda n: n % 2 == 0,nums))
print(lst2)

str = lambda s: s[0]
print(str("Tony"))

a =lambda x,y : x + y
print(a(1,2))