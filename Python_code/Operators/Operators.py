""" #1.Arithmatic operators

#1.1 Addition
print("Addition : ")
print("10 + 4 = ", 10 + 4)

#1.2 Substaction
print("Substraction :")
print("10 - 4 = ", 10 - 4)

#1.3 multiplication
print("Multiplication :")
print("10 * 4 = ", 10 * 4)

#1.4 Division
print("Division :")
print("10 / 4 = ", 10 / 4)
print("15 / 4 = ", 15 / 4)
print("10 / 2 = ", 10 / 2)
print("10.5 / 2 = ", 10.5 / 2)
print("-19 / 5 = ", -19 / 5) """

""" #1.5 Modules
print("Modules : ")
print("10 % 4 = ", 10 % 4)
print("15 % 4 = ", 15 % 4)
print("10 % 5 = ", 10 % 5)
print("-19 % 5 = ", -19 % 5)
print("10.5 % 2 = ",10.5 % 2 )

#1.6 floor division
print("Floor division")
print("10 // 4 = ", 10 // 4)
print("15 // 4 = ", 15 // 4)
print("10 // 2 = ", 10 // 2)
print("10.5 // 2 = ", 10.5 // 2)
 """

""" #1.7 Exponentiation
print("	Exponentiation")
print("2 ** 3 = ", 2 ** 3) # 2 power 3 = 2*2*2* = 8
print("4 ** 5 = ", 4 ** 5) # 4 power 5 = 4*4*4*4*4 = 1024
print("Cube of 4 is", 4**3) # 4 power 3 = 4*4*4* = 64 """


""" #2 Assignment operator

a = 20
b = 5
print("a is :", a)
print("b is :", b)

#=+
a += b
print(a)

#-=
a -= b
print(a)

#*=
b *= a
print(b)

#/=
b /= a
print(b)

a /= b
print(a)

#%=
num1 = 10
num2 = 4
print("num1 is :", num1)
print("num2 is :", num2)
num1 %= num2
print("num1 %= is :",num1)

#//=
num2 //= num1
print("num2 //= num1 is :",num2)

#**=
nums1 = 2
nums2 = 4
nums1 **= nums2 
print("nums1 **= nums2 is :", nums1) """
""" 
#3 Comparision operator
print("Comparision operator")
print(" 3 == 3 is:", 3 ==3)
print(" 3 == 4 is:", 3 ==4)
print(" 3 != 4 is:", 3 != 4)
print(" 3 != 3 is:", 3 !=3)
print(" 3 < 4 is: ", 3 < 4)
print(" 3 > 4 is: ", 3 > 4)
print(" 3 <= 4 is: ", 3 <= 4)
print(" 3 >= 4 is: ", 3 >= 4) """

""" #4.Logical operator
# 4.1 And
n1 = 10
n2 = 20
n3 = n1 < n2 and n2 > n1
print(n3)
n4 = n1 > n2 and n2 < n1
print(n4)

#4.2 Or
n5 = n1 <n2 or n2 < n1
print(n5) 
print(8 > 6 and 6 < 8)


#4.3 not
n6 = (not(n1 < n2 and n2 > n1))
print(n6)
n7 = (not(n1 > n2 and n2 < n1))
print(n7)
 
print(not(8 < 6 and 6 > 8))
"""

"""
#5.identity operator
#5.1 is
print(' "identity is"')
values1 = ['chandu', 'venkat', 'mansoor', 'pradeep']
values2 = ['chandu', 'venkat', 'mansoor', 'pradeep']
values4 = ['reddy', 'venkat', 'mansoor', 'pradeep']
print("values1 are ",values1)
print("values2 are",values2)
values3 = values1
print("values3 is values1 :", values3 is values1)
print("values3 is values2 :", values3 is values2)
print( "vlaues2 == values1",values2 == values1)
print("Values4 == vaalues1: ", values4 is values1)

#5.2 is not
print(' "identity is not" ')
a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = [1,2,3,4,5]

a = b
print(a is not b)
print(b is not a)
print(c is not a)
print( c is not b)
c = a
print("a vlaues are : ", a)
print("b values are : ", b)
print("c = a : ", c is a)
print("c is not a : ", c is not a)
print("a is not b : ", a is not b) """

""" #.6 Membership operator

x = ['apple', 'banana', 'mango']
print("x values are : ", x)

#6.1 in
print("membership in")
print("mango in x : ", "mango" in x)
print("orange in x : ", "orange" in x)


#6.2 not in
print("\nMembership not in")
print("orange not in x : ", "orange" not in x)
print("apple not in x : ", "apple" not in x)

if "orange" not in x:
    print("your stasement is true")

else:
    print("your statement is false")  """  

#7.Bitwise operator
#7.1 ~compliment
print("7. 'Bitwise operator' ")
print(' "Bitwise ~compliment are : " ')
A = 12 # or A = 0b1100
print("7.1 Value of A is : ", A)
print("compliment of A is : ", ~A)


""" a = 12
b = 11
print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b) """

""" #7.5 left shift <<

num = 15
print("num", num)
print(num << 2)

print("4 << 1 is: ", 4 << 1) # 4 << 1 = 8  
print("4 << 1 is: ", 4 << 2) # 4 << 2 = 16
print("4 << 1 is: ", 4 << 3) # 4 << 1 = 32  
print("4 << 1 is: ", 4 << 4) # 4 << 1 = 64 
print("4 << 1 is: ", 4 << 5)  # 4 << 1 = 128    """

""" #7.6 Right shift >>

num = 15
print("num", num)
print(num >> 2)

print("4 >> 1 is: ", 4 >> 1) # 4 >> 1 = 8  
print("4 >> 2 is: ", 4 >> 2) # 4 >> 2 = 16
print("4 >> 3 is: ", 4 >> 3) # 4 >> 1 = 32  
print("4 >> 4 is: ", 4 >> 4) # 4 >> 1 = 64 
print("4 >> 5 is: ", 4 >> 5)  # 4 >> 1 = 128 """

""" #exercise
#1. 26 & 23
a1 = 26
b1 = 23
c1 = a1 & b1
print("26 & 23 is :", c1)

#2. 17 | 4
a2 = 17 
b2 = 24
c2 = a2 | b2
print("17 | 24 is :", c2) 

#3. 17 ^ 24
a3 = 17
b3 = 24
c3 = a3 ^ b3
print("17 ^ 24 is :", c3)

#4. ~45
a4 = 45
print("~45 is :", ~a4)

#5. 68 << 2
a5 = 68
b5 = 2
c5 = a5 << b5
print("68 << 2 is :", c5)

#6. 56 >> 3
a6 = 56
b6 = 3
c6 = a6 >> b6
print("56 >> 3 is :", c6)
 """