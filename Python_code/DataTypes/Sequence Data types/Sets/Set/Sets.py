

""" set1 = {1, 2.4, "chandu", True, 1, False, 0}
print(set1) """

""" set = {9,4,6,3,2,6}
print(set)

#add
print("\n**set add**")
set.add(8)
set.add(3)
set.add(7)
print(set)


#update |=
print("\n**set update**")
set.update({20,40,30,6,10})
print(set)

#pop
print("\n**set pop**")
set.pop()
set.pop()
print(set)

#remove
print("\n**set remove**")
set.remove(30)
print(set)

#discard
print("\n**discard**")
set.discard(20)
print(set)
print()



#clear
print("\n**set clear**")
set.clear()
print(set)    


#using for loop
for i in set:
    print(i)
 """


#set operators

""" #1.union() |
print("\n ** Union **")

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.union(set2)  # (OR) set3 = set1 | set2
print("\nset1 is : ", set1)
print("\nset2 is : ", set2)
print("\nset1 union set2 is : ", set3) """


""" #join multiple sets
a = {1,2,3,4}
b = {3,4,5,6}
c = {5,6,'a', 'b'}  
d = {'chandu', 'vrreddy'}
total = a.union(b,c,d)    # (OR)  total = a | b | c | d # (OR) a.update (a,b,c,d)
print("total is : ", total)
 """


""" #.2 Intersection &
print("\n** Intersection **")
set1 = {"apple","banana", "cherry", "mango", "orange"}
set2 = {"apple", "mango", "orange","papaya", "kiwi"}
print("set1 is : ", set1)
print("\n set2 is : ", set2)

set3 = set1.intersection(set2)
#set3 = set1 & set2
print("\nIntersection of set3 is : ", set3)

set1.difference_update(set2)
print("\nset1 difference set2 is : ",set1) """

""" #Difference() -
set1 = {"apple","banana", "cherry", "mango", "orange"}
set2 = {"apple", "mango", "orange","papaya", "kiwi"}

print("set1 is : ", set1)
print("\n set2 is : ", set2)

#set3 = set1 - set2
set1.difference_update(set2)
print("\nset1 difference set2 is : ",set1)

set3 = set1.difference(set2)
print("\nset1 difference set2 is : ",set3) """

""" #.4 Symmetric_difference
print("\n Symmetric_difference")

set1 = {"apple","banana", "cherry", "mango", "orange"}
set2 = {"apple", "mango", "orange","papaya", "kiwi"}

print("\nset1 is : ", set1)
print("\n set2 is : ", set2)

#set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print("\nSymmetric_difference is :", set3)

set1.symmetric_difference_update(set2)
print("\nsymmetric_difference_update of set1 and set2 is : ", set1)
 """

""" #5.isdisjoint
print("** Isdisjoint**")

set1 = {"apple","banana", "cherry", "mango", "orange"}
set2 = {"apple", "mango", "orange","papaya", "kiwi"}

print("\nset1 is : ", set1)
print("\n set2 is : ", set2)

set3 = set1.isdisjoint(set2)
print(set3) """

""" #6.issubset <=

set1 = {"apple", "mango", "orange"}
set2 = {"apple", "mango", "orange","papaya", "kiwi"}

print("\nset1 is : ", set1)
print("\n set2 is : ", set2)

#set3 = set1.issubset(set2)
set3 = set1 <= set2
print(set3)
 """


#7. issuperset >=
""" set1 = {"apple","banana", "cherry", "mango", "orange"}
set2 = {"apple", "mango", "orange"}

print("\nset1 is : ", set1)
print("\n set2 is : ", set2)

#set3 = set1.issuperset(set2)
set3 = set1 >= set2
print(set3) """

nums = [1,5,2,8,4,0,9,6,7,3]
print(nums)
num = set(nums)
num.add(12345)
num.add(3)
print(num)