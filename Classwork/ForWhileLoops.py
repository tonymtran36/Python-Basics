list1 = [1,2,3,4,5,6,7,8,9,10]
for num in list1:
    if (num%2==0):
        print(num)
    else:
        print("Odd Number")

list_sum = 0
for num in list1:
    list_sum += num
print(list_sum)

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

for t1, t2 in list2:
    print(t1)

d = {'k1':1,'k2':2,'k3':3}

for key in d.keys(): #prints keys
    print(key)

for value in d.values(): #prints values
    print(value)

for item in d.items(): #prints both
    print(item)