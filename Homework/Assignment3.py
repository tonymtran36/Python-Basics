#Question 7 a ---------------------------------------------------------------------------------------------------
def findDiv7():
    for i in range(1500,2701):
        if (i%7==0 and i%5==0):
            print(i, end=", ")
    print()

findDiv7()

#Question 7 b ---------------------------------------------------------------------------------------------------
def convert(temp_str):
    degree = temp_str[-1]
    temp = int(temp_str[:2])
    if(degree=="C"):
        print(f"{temp_str} is {(int)((temp*(9/5))+32)} in Fahrenheit")
    elif(degree=="F"):
        print(f"{temp_str} is {(int)((temp-32)*(5/9))} in Celcius")

convert("60C")
convert("45F")

#Question 7 c ---------------------------------------------------------------------------------------------------
import random

def guess():
    target = random.randint(1, 9)
    while(True):
        x=input("Guess a number between 1 and 9\n")
        if int(x)==target:
            print("Well Done!")
            break
        else:
            print("Try Again")

guess()

#Question 7 d ---------------------------------------------------------------------------------------------------
def stars():
    for i in range(5):
        for j in range(i):
            print("*",end=" ")
        print()
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()

stars()
#Question 7 e ---------------------------------------------------------------------------------------------------
def reverse(str):
    print(str[::-1])

reverse(input("Enter a string to be reversed\n"))

#Question 7 f ---------------------------------------------------------------------------------------------------
def count(lst):
    evenCount = 0
    oddCount = 0
    for i in lst:
        if i%2==0:
            evenCount+=1
        else:
            oddCount+=1
    return evenCount, oddCount

numbers = (1,2,3,4,5,6,7,8,9)
print(count(numbers))

#Question 7 g ---------------------------------------------------------------------------------------------------
def printType(list):
    for i in list:
        print(f"{i} : {type(i)}")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
printType(datalist)

#Question 7 h ---------------------------------------------------------------------------------------------------
def except_three_six():
    for i in range(6):
        if i==3 or i==6:
            continue
        else:
            print(f"{i} ", end="")

except_three_six()