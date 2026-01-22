group1 = {1,9,3,7,5,2,8,5}
group2 = {2,8,4,6,10,3,7,1}

print(f"Group1: {' '.join(map(str, sorted(group1)))}")
print(f"Group2: {' '.join(map(str, sorted(group2)))}")

print("\n1 Union\n2 Intersection\n3 Difference (Group1 - Group2)\n4 Symmetric Difference\n5 Exit\n")

while True:
    choice = int(input("Select 1/2/3/4/5: "))
    

    if choice == 1:
        merge = group1.union(group2)
        print(f"Union elements: {' '.join(map(str, sorted(merge)))}")
        print()

    elif choice == 2:
        common = group1.intersection(group2)
        print(f"Common elements: {' '.join(map(str, sorted(common)))}")
        print()

    elif choice == 3:
        unique = group1.difference(group2)
        print(f"Unique elements (Group1 only): {' '.join(map(str, sorted(unique)))}")
        print()

    elif choice == 4:
        symmetric = group1.symmetric_difference(group2)
        print(f"Symmetric elements: {' '.join(map(str, sorted(symmetric)))}")
        print()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
