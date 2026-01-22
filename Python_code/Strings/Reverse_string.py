print("1 String reverse")
word = input("Enter word: ")
print(f"Original word: {word}")

reverse_string = ""
for w in word:
    reverse_string = w + reverse_string
print(f"Reverse string is: {reverse_string}\n")  

print("2 Reverse string using list")
sentence = input("Enter word: ")
print(f"Original word: {sentence}")
word = list(sentence)
word.reverse()
print(f"Reverse word: {"".join(word)}\n")

print("3 Reverse string using slicing")
sentence = input("Enter word: ")
print(f"Original word: {sentence}")
print("Reverse string: ", sentence[::-1])