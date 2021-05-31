x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

#4 Scopes
#local
#enclosing
#global
#built-in
f = lambda x:x**2

print(f)

name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'
    
    def hello():
        print('Hello '+name)
    
    hello()

greet()
print(name)
print(len)

print(globals())
print(locals())