""" favorite_place = {
    "Chandu" : {"location1" : "Marathahalli", "location2" : "Bommnahalli", "location3" : "Koramangala"},
    "Raju" : {"location1" : "Hosakote", "location2" : "Avalahalli", "location3" : "Toguru"},
    "Bharath" : {"location1" : "Batrahalli", "location2" : "TC Palya", "location3" : "KR Pura"},

}

for name in favorite_place:
    print(name, "Favorite locations are ")
    for place, key in favorite_place[name].items():
        print(place,":", key)
    print("")    

 
 """

 

""" data = {}

# Step 1: Ask how many people
limit = int(input("Enter number of students: "))
count = 1
# Step 2: Loop for each person
for i in range(limit):
    name = input(f"Enter person name{count}: ")
    print(f"Enter {name}'s favorite locations:")
    print("")

    # Step 3: Ask for 3 locations
    l1 = input("Enter location 1: ")
    l2 = input("Enter location 2: ")
    l3 = input("Enter location 3: ")
    print("")

    # Step 4: Store in a sub-dictionary
    location = {
        'location1': l1,
        'location2': l2,
        'location3': l3
    }

    # Step 5: Add to main dictionary
    data[name] = location
    count += 1

# Step 6: Display results
print("\n--- Favorite Locations ---\n")
for name, place in data.items():
    print(f"{name}'s favorite locations are:")
    for key, value in place.items():
        print(f"{key}: {value}")
    print("")  # Blank line after each person
 """


""" favorate = {
    'Chandu' : [3,7,4],
    'loki' : [2,6,8],
    'kiran' : [3,5,7]
}

for name, nums in favorate.items():
    print(name)
    for num in favorate[name]:
        print(f"{num} ", end = "")
    print(" \n") """


cities = {}
count = 1

limit = int(input("Enter number of cities: "))

for _ in range(limit):
    city = input(f"Enter city{count}: ").capitalize()
    print("")
    country = input("Enter country: ").capitalize()
    population = input("Enter population: ")
    fact = input(f"Write fact about {city}: ").capitalize()
    print(" ")

    city_info = {
        'city' : city,
        'country' : country,
        'population' : population,
        'fact' : fact
    }

    cities[city] = city_info
    count += 1




for city, city_details in cities.items():
    #print(f"City: {city}")
    for key,value in city_details.items():
        print(f"{key}: {value}")
    print()