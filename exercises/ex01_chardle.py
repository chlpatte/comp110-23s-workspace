"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730580489"
word: str = input("Enter a 5-character word: ").lower()
if (len(word) != 5):
    print("Error Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ").lower()
if (len(character) != 1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character + " in " + word)
instances: int = 0
if (character == word[0]):
    instances = instances + 1
    if (character == word[1]):
        instances = instances + 1
        if (character == word[2]):
            instances = instances + 1
            if (character == word[3]):
                instances = instances + 1
                if (character == word[4]):
                    instances = instances + 1
                    print(character + " found at index 0")
                    print(character + " found at index 1")
                    print(character + " found at index 2")
                    print(character + " found at index 3")
                    print(character + " found at index 4")
                else: 
                    print(character + " found at index 0")
                    print(character + " found at index 1")
                    print(character + " found at index 2")
                    print(character + " found at index 3")
            elif(character == word[4]):
                instances = instances + 1
                print(character + " found at index 0")
                print(character + " found at index 1")
                print(character + " found at index 2")
                print(character + " found at index 4")
        elif (character == word[3]):
            instances = instances + 1
            if (character == word[4]):
                instances = instances + 1
                print(character + " found at index 0")
                print(character + " found at index 1")
                print(character + " found at index 3")
                print(character + " found at index 4")
            else: 
                print(character + " found at index 0")
                print(character + " found at index 1")
                print(character + " found at index 3")
        elif (character == word[4]):
            instances = instances + 1
            print(character + " found at index 0")
            print(character + " found at index 1")
            print(character + " found at index 4")
        else: 
            print(character + " found at index 0")
            print(character + " found at index 1")
    elif (character == word[2]):
        instances = instances + 1
        if (character == word[3]):
            instances = instances + 1
            if (character == word[4]):
                instances = instances + 1
                print(character + " found at index 0")
                print(character + " found at index 2")
                print(character + " found at index 3")
                print(character + " found at index 4")
            else: 
                print(character + " found at index 0")
                print(character + " found at index 2")
                print(character + " found at index 3")
        elif (character == word[4]):
            instances = instances + 1
            print(character + " found at index 0")
            print(character + " found at index 2")
            print(character + " found at index 4")
        else: 
            print(character + " found at index 0")
            print(character + " found at index 2")
    elif (character == word[3]):
        instances = instances + 1
        if (character == word[4]):
            instances = instances + 1
            print(character + " found at index 0")
            print(character + " found at index 3")
            print(character + " found at index 4")
        else: 
            print(character + " found at index 0")
            print(character + " found at index 3")
    elif (character == word[4]):
        instances = instances + 1
        print(character + " found at index 0")
        print(character + " found at index 4")
    else: print(character + " found at index 0")
elif (character == word[1]):
    instances = instances + 1
    if (character == word[2]):
        instances = instances + 1
        if (character == word[3]):
            instances = instances + 1
            if (character == word[4]):
                instances = instances + 1
                print(character + " found at index 1")
                print(character + " found at index 2")
                print(character + " found at index 3")
                print(character + " found at index 4")
            else: 
                print(character + " found at index 1")
                print(character + " found at index 2")
                print(character + " found at index 3")
        elif(character == word[4]):
            instances = instances + 1
            print(character + " found at index 1")
            print(character + " found at index 2")
            print(character + " found at index 4")
        else:
            print(character + " found at index 1")
            print(character + " found at index 2")
    elif (character == word[3]):
        instances = instances + 1
        if (character == word[4]):
            instances = instances + 1
            print(character + " found at index 1")
            print(character + " found at index 3")
            print(character + " found at index 4")
        else: 
            print(character + " found at index 1")
            print(character + " found at index 3")
    elif (character == word[4]):
        instances = instances + 1
        print(character + " found at index 1")
        print(character + " found at index 4")
    else: 
        print(character + " found at index 1")
elif (character == word[2]):
    instances = instances + 1
    if (character == word[3]):
        instances = instances + 1
        if (character == word[4]):
            instances = instances + 1
            print(character + " found at index 2")
            print(character + " found at index 3")
            print(character + " found at index 4")
        else: 
            print(character + " found at index 2")
            print(character + " found at index 3")
    elif(character == word[4]):
        instances = instances + 1
        print(character + " found at index 2")
        print(character + " found at index 4")
    else:
        print(character + " found at index 2")
elif (character == word[3]):
    instances = instances + 1
    if (character == word[4]):
        instances = instances + 1
        print(character + " found at index 3")
        print(character + " found at index 4")
    else: 
        print(character + " found at index 3")
elif (character == word[4]):
    instances = instances + 1
    print(character + " found at index 4")
if (instances == 5):
    print("5 instances of " + character + " found in " + word)
elif (instances == 4):
    print("4 instances of " + character + " found in " + word)
elif (instances == 3):
    print("3 instances of " + character + " found in " + word)
elif (instances == 2):
    print("2 instances of " + character + " found in " + word)
elif (instances == 1):
    print("1 instance of " + character + " found in " + word)
if (instances == 0): 
    print("No instances of " + character + " found in " + word)
