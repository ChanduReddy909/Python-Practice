""" thisdict = {"brand" : "Ford", "model" : "Mustang", "year" : 1964}
print(thisdict)

#Accessing using keys
print(thisdict["brand"]) """

""" #data types
Mobile = {
    "brand" : "Oneplus",
    "model" : "Nord",
    "Price" : 30000,
    "foldable" : False,
    "colors" : ["Black", "Silver", "Blue"]

}
print("** Mobile details are ** \nBrand : ", Mobile["brand"],
      
"\nModel:", Mobile["model"],
"\nPrice:", Mobile["Price"],
"\nFoldable:", Mobile["foldable"],
"\nColors:", Mobile["colors"])

#the dict() Constructor
print("\n using Dict() Constructor")

student = dict(name = "Chandu", age = 22, brach = "MCA", sec = "A")
print("** student details **")
print("Name:", student["name"],
      "\nAge:", student["age"],
      "\nBrach:", student["brach"],
      "\nSection:", student["sec"]) """
      
""" #Methods
# College details
print("** College Details **")

college = {
    "Puc": ["HEBA", "EBACs", "PCMB", "PCMCs"],
    "Degree": ["BA", "BCOM", "BCA", "BBA"],
    "Engineering": ["ECE", "EEE", "AIML", "CS", "CIVIL", "MECHANICAL"]
}

# Direct Access
print("PUC:", college["Puc"],
      "\nDegree:", college["Degree"],
      "\nEngineering:", college["Engineering"])

# 1. get()
print("\n1. get() Method")
print("Degree details are:", college.get("Degree"))

# 2. items()
print("\n2. items()")
for branch, depts in college.items():
    print("Department:", branch, "→ Branches:", depts)

# 3. keys()
print("\n3. keys()")
print("Available Departments are:", list(college.keys()))

# 4. update()
print("\n4. update()")
college.update({"Masters": ["MA", "MCOM", "MCA", "MBA"]})
print("Updated College Dictionary:")
print(college)

#5.pop
print("\n5.pop method()")
pops = college.pop("Puc")
print("Poped key values are: ", pops)
print("Remaining data in college is : ", college)

#6.popitem
print("\n6.popitems method()")
popitems = college.popitem()
print("poped items are:", popitems)
print("Remaining data in college is : ", college)

#7.clear
print("\n7.Clear method()")
bike = {"Name" : "KTM", "Model" : "RC"}
print("Bike datails are:", bike)
clears = bike.clear()
print(clears)
print("bike details  are after clear: ", bike)

#8.copy
print("\n8.copy method()")

university = college.copy()
print("college deatils are:", college)
print("university details copied from college are: ", university) """

#9.fromkeys
print("\n9.fromkeys")

students = ["Akhil", "Bhanu", "Chandu", "Divya"]
attendance = dict.fromkeys(students, "Present")
print("students names are: ", students)

attendance["Bhanu"] = "Absent"

print("\nPresented students")
for name in attendance:
    if attendance[name] == "Present":
        print(name)

print("\nAbsent students")
for name in attendance:
    if attendance[name] == "Absent":
        print(name)


#10.setdefault
employees = {"Name" : "Chandu", "Dept" : "IT"}
print("Employee details : ", employees)

emp_details = employees.setdefault("Location", "Bengaluru")
print("emp details :",emp_details)
print(employees)

#11.values
print("\n11.values method()")
print("employee deatails are: ", employees.values())

#12. del
print("\n12.del method()")

movies = {"name" : "HIT", "Lang" : "telugu", "Hero" : "Nani", "Budget" : "20cr"}
print("movies details are: ", movies)

del movies["Budget"]
print(movies)

#13.length()
print("\n13.length()")
print("length of movies is:", len(movies))

#update with merge two dictionaries
print("\n")
d1 = {"name" : "chandu", "age" : 22 }
d2 = {"college" : "CIT", "Brach" : "MCA"}
print("d1 is :", d1)
print("d2 is:", d2)
d1.update(d2) # or d1|d2
print("d1 + d2 is: ", d1)


