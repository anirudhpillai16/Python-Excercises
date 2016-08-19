# Write a program (function!) that takes a list and returns a new list that contains all the 
# elements of the first list minus all the duplicates.

a = [1,2,6,7,1,4,3,1,8,2,8]
b = []
def remdup(a,b):
    for i in a:
        if i not in b:
            b.append(i)
    print "List after removing duplicate values is --> " + str(b)
remdup(a,b)