def vowels(sentence):
    vowel = "aeiouAEIOU"
    counts = 0
    for char in sentence:
        if char in vowel:
            counts += 1
    return counts
            
print("1 Add text")
print("2 break")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        sentence = input("Enter sentence: ")
        result = vowels(sentence)
        print("Total vowels:", result)
        
    
    elif choice == 2:
        break
    else:
        print("Invalid choice ")
            
      
vowels("I love my india")    

      