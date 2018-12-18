from random import shuffle
from random import randint
from random import seed

seed(101)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(shuffle(mylist)) # return None
print(mylist)

print(randint(0, 100))
