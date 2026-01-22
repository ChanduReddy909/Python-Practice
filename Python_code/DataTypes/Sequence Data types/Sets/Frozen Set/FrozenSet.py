# Create a frozenset

f = frozenset([2, 1])
print("frozenset f is:", f)

# Iteration through frozenset
print("\nIterating over frozenset f:")
for items in f:
    print(items)

# Create two frozensets for operations
s1 = frozenset([1, 2, 3])
s2 = frozenset([3, 4, 5])
print("\ns1 is:", s1)
print("s2 is:", s2)

# Union of s1 and s2
print("\nUnion of s1 and s2 is:", s1 | s2)

# Intersection of s1 and s2
print("Intersection of s1 and s2 is:", s1 & s2)

# Difference of s1 and s2 (elements in s1 not in s2)
print("Difference of s1 and s2 is:", s1 - s2)

# Symmetric difference (elements in either s1 or s2, but not both)
print("Symmetric difference of s1 and s2 is:", s1 ^ s2)

# Membership test
print("\nMembership test:")
print("Is 3 in s1?", 3 in s1)

# Sorting a regular list (frozenset itself cannot be sorted directly)
ss = [2, 1, 3, 6, 5]
print("\nSorted list is:", sorted(ss))

# Check if s1 is a superset of s2
print("\nIs s1 a superset of s2?", s1.issuperset(s2))

# Check if s1 is a subset of s2
print("Is s1 a subset of s2?", s1.issubset(s2))

# Maximum value in s2
print("\nMaximum value in s2:", max(s2))

# Minimum value in s1
print("Minimum value in s1:", min(s1))

# Disjoint check (True if s1 and s2 have no elements in common)
print("\nAre s1 and s2 disjoint?", s1.isdisjoint(s2))

# Length of the frozensets
print("\nLength of s1 is:", len(s1))
print("Length of s2 is:", len(s2))

# Type of the frozensets
print("\nType of s1 is:", type(s1))
print("Type of s2 is:", type(s2))
