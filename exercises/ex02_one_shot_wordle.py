"""One Shot Wordle"""
__author__ = "730580489"
SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ").lower()
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
accuracy: str = ""
while playing:
    if guess == SECRET:
        while index < len(SECRET):
            if guess[index] == SECRET[index]:
                accuracy = accuracy + GREEN_BOX
                index = index + 1
        print(accuracy)
        print("Woo! You got it!")
        playing = False
    elif len(guess) != len(SECRET):
            guess = input(f"That was not {len(SECRET)} letters! Try again: ")
    else:
        misplaced: bool = False
        secret_index: int = 0
        while index < len(SECRET):
            if guess[index] == SECRET[index]:
                accuracy = accuracy + GREEN_BOX
                index = index + 1
            while misplaced and secret_index < len(SECRET):
                if guess[index] == SECRET[secret_index]:
                    misplaced = False
                    accuracy = accuracy + YELLOW_BOX
                else:
                    secret_index = secret_index + 1
            if misplaced == True:
                accuracy = accuracy + WHITE_BOX
            index = index + 1
        print(accuracy)
        print("Not quite. Play again soon!")
        playing = False