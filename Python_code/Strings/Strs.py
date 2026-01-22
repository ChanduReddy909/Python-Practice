""" #str is collection characters

#single Qoutes
A = 'CHANDU REDDY'
print(A)
print(type(A)) """

""" #Double Qoutes
a = "Chandu Reddy's"
print(a)
print(type(a)) """

""" #Triple Quotes
b = '''Chandu "Reddy's"'''
print(b)
print(type(b)) """

# String Methods

""" #1.Upper()
name = " chandu REDDY "
print(name.upper()) #returns in upper case

names = name.isupper() # checking if all lettrs are in upper
print(names)  """

""" #2.lower()
name = " CHANDU REDDY "
print(name.lower())  # checking if all lettrs are in lower
name1 = name.islower() # checking if all letters are in lower
print(name1) """

""" #3.Endwith()
name = " CHANDU REDDY "
print(name.endswith("REDDY "))  # true REDDY IN CAPS AND ENDS WITH SPACE
name1 = name.endswith("reddy")  # FAlse reddy in small end but not mentioned with space
print(name1) """

""" #4.Startswith()
name = " CHANDU REDDY "
print(name.startswith(" CHANDU")) #true CHANDU in caps and starts with space
name1 = name.startswith("CHANDU") #false CHANDU in caps but not mentioned space
print(name1)
 """

#5.replace()
name = " CHANDU REDDY"
print(name)
print(name.replace("REDDY", "GOWDA"))   # DIRECTLY REPLCE WITHOUT ANOTHER VARIABLE
              #OR
name1 = name.replace("CHANDU", "LAKSHMANA")  # REPLACE WITH USING ANOTHER VARIABLE
print(name1)

#replace with three words
name = "chandu reddy soora reddy"
print(name)
print(name.replace("soora", "soorasaani"))

#multiple replaces
book = "This is new and new book"  # original string, this string new twice
print(book)
b1 = book.replace("new", "old")  # here old replce new but original string have 2 new so both new will be old
print(b1)

b2 = book.replace("new", "old", 1) # here old replce new but original string have 2 new but we asign only 1 old replace the new and other new will be same
print(b2)

c = "sri sri sri nayaka"
print(c)
d = c.replace("sri","mr",2) # here  mr will be replace the sri sri but not another sri because we asign only for 2 
print(d)

""" #6.Index()
name = "CHANDU REDDY"
print(name.index("D")) # retuns only first letter
print(name.index("")) # returns 0 because name starts with space
print(name.index("CHANDU")) #  returns 0 because chandu is first word in a variable
print(name.index("REDDY"))
 """



""" #7.Find()
name = "CHANDU REDDY"
print(name.find("CHANDU"))
print(name.find("venkat"))  # returns -1 becuase there is no "venkaat in variable name"
print(name.find("H"))
 """

""" #8.count()
name = "CHANDU CHANDU REDDY"
print(name.count("D")) #4 
print(name.count("CHANDU")) #2
print(name.count("REDDY")) """

""" #9.removeprifix()
name = "CHANDU CHANDU  REDDY"
print(name)
print(name.removeprefix("CHANDU")) 
print(name.removeprefix("C")) """

""" #10.removesuffix
name = "CHANDU REDDY REDDY"
print(name)
print(name.removesuffix("REDDY"))
print(name.removesuffix("Y")) """

""" #11.split()
name = "CHANDU REDDY REDDY"
print(name)
print(name.split("RE")) # removes RE
print(name.split()) """

""" #12.strip
name = "   CHANDU   REDDY  "
print(name)
print(name.strip())
 """
""" #13.rstrip
name = "   CHANDU   REDDY  "
print(name)
print(name.rstrip()) """

""" #14.lstrip
name = "   CHANDU   REDDY  "
print(name)
print(name.lstrip()) """

""" #15.capitalize()
name = "chandu reddy"
print(name)
print(name.capitalize()) """

""" #16.title()
name = "python program"
print(name.title()) """

""" #17.isalpha()
name = "chandu"
print(name)
print(name.isalpha())
 """

""" #18.isdigit()
num = 123
print(num)
print(num.is_integer()) """

""" #19.len()
name = "chandu reddy"
print(name)
print(len(name))"""

""" #20.join()
fruits = ["Apple", "Banana", "Mango", "Orange",]
print(fruits)
result = ' '.join(fruits) # values will separate with space
print(result)
print()
result1 = '*'.join(fruits) # values will separate with *(Star)
print(result1) """ 


""" #string Escaping characters
name = "chandu \"reddy\""
print(name) 

txt = 'My name is \'chandu reddy\' '
print(txt) 
""" 

""" # F-string
age = 24
txt = f'My name is \'Chandu Reddy\' {age} years old'
print(txt) """


""" #Placeholders or Format
Price = 49
value = f'price is {Price} dollars'
print(value)


#.2f
amount = 456
total = f'total amout is {amount:.3f}'
print(total) """

""" #placehilder with math operation
num = f'math operation is {20 * 30:.3f}'
print(num)
 """

#Sting slicing

""" strs = "Hello world!"
print(strs)
print("[2:5]", strs[2:5])
print("[:5]", strs[:5])
print("[2:]", strs[2:])
print("[-8:-5]", strs[-8:-5])
print("[0:12]", strs[0:12]) """

