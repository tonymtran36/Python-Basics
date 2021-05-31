#Question-6-Part-2-------------------------------------------------------
#Three is a crowd
def crowd(lst):
    if (len(lst)>3):
        return print("There is a crowd of more than 3 people")
    else:
        return print("It is not very crowdy")

list=["Jack", "Jill", "Bob", "Tony"]

crowd(list)

list.pop(0)
list.pop(0)

crowd(list)

