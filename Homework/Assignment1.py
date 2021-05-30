import math

def calculate(p, r, t): #calculate monthly payments p is payment, r is rate, and t is time
    r_month = (r/12)*.01
    return math.ceil(p *  ( (r_month)*(1+(r_month))**t / (((1+(r_month))**t)-1) ) )
    
#Exercise 2
a = 50+ 50
b = 100-10
print(a+b)

print("Hello World")

print("Hello World : 10")

print("input data:")
print(800000, 6, 103)

print("answer")
print(calculate(800000, 6, 103))
