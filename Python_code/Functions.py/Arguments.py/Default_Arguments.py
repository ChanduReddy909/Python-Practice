def user(name, greeting = "Hello"):
    return greeting + "," +  name + "!"

greeting1 = user("Bob")
greeting2 = user("Charlie", "Hi")

print(greeting1)
print(greeting2)

