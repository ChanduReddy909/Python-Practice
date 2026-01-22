num = int(input("Enter Table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
    
    
print()

start = int(input("Enter starting table: "))
end = int(input("Enter ending table: "))
for i in range(start, end+1):
    for j in range(1,11):
        
        print(f"{i} x {j} = {i * j}")
    print()