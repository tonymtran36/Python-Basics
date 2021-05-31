#1-------------------------------------------
def func():
    print('Hello World')

func()

#2-------------------------------------------
def func1(name):
    print(f"Hi my name is {name}")

func1("Google")

#3-------------------------------------------
def func3(x,y,z):
    if z == True:
        return x
    else:
        return y

print(func3('hello','goodbye',False))

#4-------------------------------------------
def func4(x,y):
    return x*y

print(func4(4,5))

#5-------------------------------------------
def is_even(val):
    if val%2==0:
        return True
    else:
        return False

print(is_even(4))

#6-------------------------------------------
def find_max(x, y):
    if x>y:
        return True
    else:
        return False

print(find_max(4,6))

#7-------------------------------------------
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(1,2,3,4,5,6,7))
#8-------------------------------------------
def lst_even(*args):
    lst=[]
    for i in args:
        if i%2==0:
            lst.append(i)
    return lst

print(lst_even(1,2,3,4,5,6,7))

#9-------------------------------------------
def capitalize(str):
    temp = ""
    for i in range(len(str)):
        if i%2==0:
            temp += str[i].upper()
        else:
            temp += str[i].lower()
    return temp
print(capitalize("sentENCED"))

#10------------------------------------------
def lesser(num1, num2):
    if num1%2==0 and num2%2==0:
        return (num1+num2)/10
    if num1%2!=0 or num2%2!=0:
        return (num1+num2)

print(lesser(40, 50))
print(lesser(41,50))

#11------------------------------------------
def same_start(str1, str2):
    if str1[0] == str2[0]:
        return True
    else:
        return False
    
print(same_start("start","stop"))
print(same_start("go","pass"))

#12------------------------------------------
def twice(val):
    return val * (2*7)

print(twice(4))

#13------------------------------------------
def capitalize(str):
    temp = list(str)
    temp[0] = str[0].upper()
    temp[4] = str[4].upper()
    return ''.join(temp)

print(capitalize("testing"))
#print(capitalize("str")) Should test for this