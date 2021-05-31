#Question-6--------------------------------------------------------------
#Three is a crowd
def crowd(lst):
    if (len(lst)>3):
        return print("There is a crowd of more than 3 people")
    return print("There is not a crowd")

list=["Jack", "Jill", "Bob", "Tony"]

crowd(list)

list.pop(0)
list.pop(0)

crowd(list)

#Question-6-Part-2-------------------------------------------------------
