""" names = ["Chandu", "Kushwanth","Babu", "Chandan", "Raju"]

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
    print(names[ind]) """


# Finding mutiple index for single value

# Method 1
""" print("Method 1")
nums = [1,2,3,4,9,3,6,7,3,8,9,3] 
print(nums)

for index, value in enumerate(nums):
    if value == 3:
        print(index)
print()        
 """
    
# method 2
""" print("method 2")
nums = [1,2,3,4,9,3,6,7,3,8,9,3] 
print(nums)

for i in range(len(nums)):
    if nums[i] == 3:
        print(i) """


# Removing Duplicate elements in list
print("Removing Duplicate elements in list")
# method 1
print("method 1")
nums = [2,3,4,3,6,3,8,3,10,3]
print(nums)
without_duplicate = []
for num in nums:
    if num !=3:
        without_duplicate.append(num)
      
print(without_duplicate)      
print()


#method 2
print("method 2")
nums = [2,3,4,3,6,3,8,3,10,3]
print(nums)
unique = []
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)        