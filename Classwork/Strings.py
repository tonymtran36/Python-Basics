#Strings
print("String")
print('string')
print("String don't only need single quotes")

s = "String"
#functions/indexing
print(len(s))
print(s[0])

#slicing
print(s[1:])
print(s[:2])
print(s[-1])
print(s[:-1])
print(s[:5])
print(s[::-1])
print("z"*10)

#built in methods
print(s.upper())
print(s.capitalize())
print("Become a list".split())
print("Become a list".split('e'))
print("Hellow World : {}".format("or the end"))

#String formatting
player = "Tony"
points = 5
print('Last night, '+player+' scored '+str(points)+' points.') #Concatenation
print(f'Last night, {player} scired {points} points.') #string formatting - most recent technique (3.6)
print("I'm going to inject %s here."%'talking') #modulo method
print("I'm going to inject %s text here, and %s text here."%('this', 'that'))
print("Here: %s"%points)

print("Hello %r"%"World")

#padding
print("Number %2.5f"%(3.1415991))
print("Number %2.5f"%(113.14))
print("Number %5.1f"%(3.1))
print("First: %s, Second %5.2f, Third; %r" %("hi", 3.1415, "bye!"))
print('The {2} {1} {0}'.format('fox','brown','quick'))

print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1,b='Two',c=12.3))
print('A {p} saved is a {p} earned.'.format(p='penny'))

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

name = 'Fred'

print(f"He said his name is {name}.")
