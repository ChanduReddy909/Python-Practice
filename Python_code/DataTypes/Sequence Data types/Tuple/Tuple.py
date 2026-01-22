""" #Tuple 

a = ("a",)
print(type(a))

#Slicing
t = (1, 2.3, "chandu", True,9, 8.5, "RSL")
print(t[0::2])

#Built-in functions
t1 = (2, 35, 29, 19, 43)
print(min(t1))
print(max(t1))
print(sum(t1))
print(len(t1))

#update 
x = ("Apple", "Banana", "Cherry")
print(x)
y = list(x)
y.append("Mango")
y[3] = "Orange"
x = tuple(y)
print(x)

#Add tuple with tuple

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
print(t1)
print(t2)
t1 += t2
print(t1)

#Delete
td = ('a', 'b', 'c')
print("td is : ", td)
#del td
#print(td)

#Multiply Tuples

z = (1,2,3,1)
print(z * 2)

#Count
print(z.count(1))

#index
print(z.index(1))

#membership IN
print(2 in z)

#Membership NOT IN
print(5 not in z)

#Identify IS
is1 = (2, 4, 6, 8)
is2 = (2, 4, 6, 8)
is3 = (1, 3, 5, 7)

print(is1 is is2)
print(is1 not in is3) """

#Packing tuple
fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))

#Unpacking tuple 
print("***Unpacking tuple***")
fruits1 =  ("apple", "banana", "cherry")
print("Fruits are : ", fruits1)

green, yellow, red = fruits1
print("Green is : ", green)
print("Yellow is : ", yellow)
print("Red is : ", red)

#Asterisk*
#exapmle 1
print("\n ---Asterisk*---")
print("##Example 1##")
marks = (100, 90, 80, 70, 60, 50, 40, 30)
grade1, grade2, grade3, *grade4, justpass, fail = marks 
print("Orginal marks are : ", marks) 
print("Grade1 is : ", grade1)
print("Grade2 is : ", grade2)
print("Grade3 is : ", grade3)
print("Grade4 is : ", grade4)
print("Passmark is : ", justpass)
print("Fail is : ", fail)


#exaple 2
print("\n##Example 2##")
values = (
    (1, 2, 3, 4, 5, 6),
    ('a', 'b', 'c', 'd', 'e'),
    ('I', 'II', 'III', 'VI', 'V'),
    ('@', '#', '$', '%', '^')
)

print("Original values are : ", values)

# Unpacking the outer tuple into 4 inner tuples
numbers, alphabets, romans, special = values

print("Integer Numbers are : ", numbers)
print("Alphabets are : ", alphabets)
print("Roman Numbers are : ", romans)
print("Special Characters are : ", special)


#slicing in Unpacking
print(values[0][0])
print(values[0][1])
print(values[1][0])
print(values[1][1])
print(values[2][4])
print(values[3][0])
