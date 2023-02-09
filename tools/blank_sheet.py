SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ").lower()
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
accuracy: str = ""
misplaced: bool = False
secret_index: int = 0
while index < len(SECRET):
    if guess[index] == SECRET[index]:
        accuracy = accuracy + GREEN_BOX
        print(index)
        print(accuracy)
        print(misplaced)
        index = index + 1
    else:
        misplaced = False
        secret_index = 0
        while misplaced == False and secret_index < len(SECRET):
            if guess[index] == SECRET[secret_index]:
                misplaced = True
                accuracy = accuracy + YELLOW_BOX
                print(index)
                print(accuracy)
                print(misplaced)
            else: secret_index = secret_index + 1
        if misplaced == False:
            accuracy = accuracy + WHITE_BOX
            misplaced = False
        index = index + 1
print(accuracy)
