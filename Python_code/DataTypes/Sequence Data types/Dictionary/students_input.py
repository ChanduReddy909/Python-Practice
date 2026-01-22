

Students = {}

count = 1

while True:
  
  print(f"\nEnter Student{count} details")
  
  name = input("Enter Name: ")
  print(f"{name} Added successfully!")
  
  usn = input("Enter USN: ")
  print(f"{usn} Added successfully!")
  
  section = input("Enter section: ")
  print(f"{section} Added successfully")
  
  dept = input("Enter Department: ")
  print(f"{dept} Added successfully!")
  
  confirm = input("confirm to push data (YES/NO): ").strip().lower()
  if confirm == 'yes':
    Students[f"Student{count}"] = {
      "name" : name,
      "usn" : usn,
      "section" : section,
      "dept" : dept
      
    }
    
    print(f"Student{count} data added successfully!")
    count += 1
  else:
    print("Data not saved for this student...")
    
    cont = input("Do you continue (YES/NO): ").strip().lower()
    if cont == 'no':
      print("Exiting program...")
      break
print("Final Result...")
for key, details in Students.items():
    print(f"\n {key}\n Name: {details['name']}\n USn: {details['usn']}\n section: {details['section']}\n Department: {details['dept']}")
    print(" ")  
  
  
  
  
  