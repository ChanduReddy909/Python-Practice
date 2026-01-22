names = ["Chandu", "Kushwanth","Babu", "Chandan", "Raju"]

# finding index value with name
key = input("Enter name find index values: ").capitalize()
if key in names:
    print(f"{key} index is {names.index(key)}")
else:
    print(f"{key} not found")

# findex name with index value  
ind = int(input("Enter index to find name: "))
if ind < 0 and ind > len(names):
    print(f"{ind} not found")
else:
    print(names[ind])