print("Union Operations")
# 1 Union
print("1 Unionn")
'''
Union is ued combining the unique values
from the two tables/ variables

'''
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,4}
print(set1)
print(set2)
print(set1.union(set2))

print()
boys = {"chandu", "loki", "chandan", "raju", "madhu"}
girls = {"ramya", "swapna", "anu", "madhu", "geetha"}
print(boys)
print(girls)
students = boys.union(girls)
print(" ".join(students))
print()


#2 Intersection
print("2 Intersection")
'''
Intersection is used retutn the Common 
elements from two tables/variabes
'''
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,4}
print(set1)
print(set2)
print(set1.intersection(set2))

print()
boys = {"chandu", "loki", "chandan", "raju", "madhu"}
girls = {"ramya", "swapna", "anu","chandu", "madhu", "geetha"}
print(boys)
print(girls)
students = boys.intersection(girls)
print(" ".join(students))
print()

# 3 Difference
print("3 Difference")
'''
Meaning: The returned set contains items that
 exist only in the first set, and not in both sets.

return uniqe elements from left set only
'''
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,4}
print(set1)
print(set2)
print(set1.difference(set2))

print()
boys = {"chandu", "loki", "chandan", "raju", "madhu"}
girls = {"ramya", "swapna", "anu","chandu", "madhu", "geetha"}
print(boys)
print(girls)
students = boys.difference(girls)
print(" ".join(students))
print()

# 4 Symmetric Difference
print("4 Symmetric Difference")
'''
It removes matching/common values from two tables
and display unique values from both two tables

it is opposite of intersecton
'''
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,4}
print(set1)
print(set2)
print(set1.symmetric_difference(set2))

print()
boys = {"chandu", "loki", "chandan", "raju", "madhu"}
girls = {"ramya", "swapna", "anu","chandu", "madhu", "geetha"}
print(boys)
print(girls)
students = boys.symmetric_difference(girls)
print(" ".join(students))
print()

# 5 Disjoint
'''
It means it compare if both table/variable 
values are different 
if both set values are different then return True
if there is any one element have common then return False
'''

print("5 Disjoint")

data1 = {1,2,3}
data2 = {5,6,7}
print(data1)
print(data2)
print(data1.isdisjoint(data2))

# 6 issubset
# it means set2 must contains all set1 elements
# set2 must match the all elements of set1
 
print("6 issubset")
'''
“Is this set completely inside another set?”
It checks whether all elements of one set are present in another set.
'''
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
print(A.issubset(B))   # True # Because every element of A is in B.

# But
C = {1, 2, 9}
print(C.issubset(B))   # False Because 9 is not in B
print()

# 7 issuperset
print("7 issuperset")
'''
“Does this set contain all elements of another set?”
It checks whether a set has everything that the other set has.
'''
B = {1, 2, 3, 4, 5}
A = {1, 2, 3}
print(B.issuperset(A))   # True Because B contains all elements of A.

# But
print(A.issuperset(B))   # False Because A does not contain all elements of B.

'''
Easy way to remember
issubset → small set inside big set
issuperset → big set contains small set

'''
# example
print("Real-life example")
A = {"pen", "pencil"}
B = {"pen", "pencil", "book", "eraser"}
print(A)
print(B)
print(A.issubset(B)) #True
print(B.issuperset(A)) # True


#full exapmle 
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))    # True
print(A.issuperset(B)) # False

print(B.issubset(A))    # False
print(B.issuperset(A)) # True










