import random
n = input("Enter length of list:")
a = random.sample(range(1,100),n)
print a
print [a[0],a[len(a)-1]]