"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730580489"
word: str = input("Enter a 5-character word: ").lower()
if (len(word) != 5):
    exit("Error: Word must contain 5 characters")
character: str = input("Enter a single character: ").lower()
if (len(character) != 1):
    exit("Error: Character must be a single character.")
print("Searching for " + character + " in " + word)
index = word.find(character)
index2 = word.rfind(character)
if (index == 0):
    if (index2 == 1):
        print(character + " found at index 0")
        print(character + " found at index 1")
    elif (index2 == 2):
        print(character + " found at index 0")
        print(character + " found at index 2")
    elif (index2 == 3):
        print(character + " found at index 0")
        print(character + " found at index 3")
    elif (index2 == 4):
        print(character + " found at index 0")
        print(character + " found at index 4")
    else: print(character + " found at index 0")
elif (index == 1):
    if (index2 == 2):
        print(character + " found at index 1")
        print(character + " found at index 2")
    elif (index2 == 3):
        print(character + " found at index 1")
        print(character + " found at index 3")
    elif (index2 == 4):
        print(character + " found at index 1")
        print(character + " found at index 4")
    else: print(character + " found at index 1")
elif (index == 2):
    if (index2 == 3):
        print(character + " found at index 2")
        print(character + " found at index 3")
    elif (index2 == 4):
        print(character + " found at index 2")
        print(character + " found at index 4")
    else: print(character + " found at index 2")
elif (index == 3):
    if (index2 == 4):
        print(character + " found at index 3")
        print(character + " found at index 4")
    else: print(character + " found at index 3")
elif (index == 4):
    print(character + " found at index 4")
if (index == -1):
    instances = 0
elif (index > -1):
    if (index2 > index):
        instances = 2
    else: instances = 1
if (instances == 1):
    print("1 instance of " + character + " found in " + word)
elif (instances == 2):
    print("2 instances of " + character + " found in " + word)
else: print("No instances of " + character + " found in " + word)
