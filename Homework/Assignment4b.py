#Exercise 9 -------------------------------------------------------
from functools import reduce

def separate(lst):
    t1 = () #Order Number and product
    t2 = () #Quantity and ppi


# table = ( [["Order Number", 34587, 98762, 77226, 88112]["Book Title and Author", "Learning Python, Mark Lutz", "Head First Python, Paul Barry", 
#     "Einführung in Python3, Bernd Klein"]["Quantity", 4, 5, 3, 3]["Price per Item", 40.95, 56.80, 24.99]]
# )

table = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],["98762", "Programming Python, Mark Lutz", 5, 56.80],["77226", "Head First Python, Paul Barry", 3,32.95],["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]

converted = list(map(lambda x: x if x[1] >= 100 else (x[0], x[1] +10),map(lambda x: (x[0],x[2] * x[3]), table)))
print(converted)

orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)],[2, ("5464", 9, 9.99), ("9744", 9, 44.95)],[3, ("5464", 9, 9.99),
    ("88112", 11, 24.99)],[4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]

total_orderings = list(map(lambda k: k if k[1]>=100 else (k[0],k[1]+10),map(lambda x:(x[0],reduce(lambda a,b:a+b,list(map(lambda y:y[1]*y[2] ,x[1:])))),orders)))

print(total_orderings)
