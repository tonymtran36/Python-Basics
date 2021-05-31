from typing import Text

#Reading a file
myfile=open('test.txt')

print(myfile.read())
print(myfile.read())

myfile.seek(0)
print(myfile.read())

myfile.seek(0)
print(myfile.readlines())

myfile.close()

#Writing to a file
file = open('test.txt', "w+")

file.write("I am taking over!")

print(file.read())

file.close()

#Append to a file
file_two=open('test.txt',"a+")
file_two.write("\nThis is text being appended to test.txt")
file_two.write("\nAnd another line here.")

file_two.seek(0)
print(file_two.read())

file_two.close()

#Iterating over a file
print("Iterating over a file")
for line in open('test.txt'):
    print(line)

