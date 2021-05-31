my_list=[1,2,3,4,5,8,6,7]
list_two = ['A string',23,100.232,'o']

print(my_list)
print(len(list_two))
print(my_list[0])
print(my_list + ["four"])

print(my_list.pop())
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

matrix = [lst_1,lst_2,lst_3]
print(matrix)
print(matrix[0])
print(matrix[0][0])

first_col = [row[0] for row in matrix]
print(first_col)