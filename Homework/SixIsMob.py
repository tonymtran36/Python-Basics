#Question-6-Part-2-------------------------------------------------------
#Three is a crowd
def crowd(lst):
    if (len(lst)>5):
        return print("There is a mob of people in the room")
    elif (len(lst)>2 and len(lst)<5):
        return print("The room is crowded")
    elif (len(lst) == 1 or len(lst) == 2):
        return print("It is not very crowdy")
    else:
        return print("The room is empty")
list=["Jack", "Jill", "Bob", "Tony","Nick","Isabella"]

crowd(list) #First Case

list.pop(0)
list.pop(0)
crowd(list) #Second Case

list.pop(0)
list.pop(0)
crowd(list) #Third Case

list.pop(0)
list.pop(0)
crowd(list) #Fourth Case

