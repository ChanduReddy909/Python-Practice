
""" #int 
A = 10
B = -750
print(A)
print(B)
print("A  tpye is : ", type(A), " B tpye is : ", type(B)) """


""" #float
a = 10.5
print(a)
print(type(a))
"""

""" b = 33E1
print(b)
print(type(b))  """

""" #Boolean  True = 1 and False = 0
d = 10
e = 20
print(d > e) # 10 > 20 = false
print(e > d) # 20 > 10 = true

print(" True == 0", True == 0)  #false
print(" False == 1", False == 1)  #false

print(" True == 1", True == 1)   #true
print(" False == 0",False == 0)  #true

if d > e:  # 10 > 20
    print("Your condition True")
else:
    print("Your condition False") """


""" 
# Complex

f = 10+2j
print("f is : ",f)
print("2+2j is : ", type(f))
print()

# Complex operations
g = 8 + 4j
h = 4 + 2j

print(g,h)
print("g + h",g + h)
print("g - h",g - h)
print("g * h",g * h)
print("g / h",g / h)


 """

#Tpye Conversion


""" # 1. implicit (Automatic)
i = 4       #int 
j = 5.8     #float
result = i + j #int + float = float
print(" i + j Is : ",result, "Type is : ", type(result))

print(float(i)) # int i became flaot like 4 to 4.0
print(int(j))   # flaot f becames int like 5.8 to 5
print() """


# 2. explicit (manual)

""" # srt to int
k = "10"
k_int = int(k)
print("k is : ",k)
print("K_int is : ", k_int); 
print("Type of k is : ", type(k))
print("Type of k_int is : ", type(k_int))
print()

#int to str
age = 20
new_age = str(age)
print("age is : ", age, "type of age is : ",type(age))
print("new_age is : ", new_age, "type of new_age is : ", type(new_age))
print()

#3. int to complex
m = 7
print("m is : " ,m , "type of m is : " , type(m))

m_complex = complex(m)
print("m_complex is : " , m_complex , "type of m_complex is : " , type(m_complex))

# complex to int
m_int = int(m_complex.real) 
print("m_int is : ", m_int , "type of m_int is : ", type(m_int))
 """
# To get all methods
print([method for method in dir(str) if not method.startswith("__")])
