"""Six Turn Wordle!"""

__author__ = "730580489"

def contains_char(secret: str,  guess_char: str) -> bool:
    """"Searches to see if character mataches any index of the secret word."""
    assert len(guess_char) == 1
    index: int = 0
    misplaced: bool = False
    while misplaced is False and index < len(secret):
        if guess_char == secret[index]:
            misplaced = True
        else: 
            index = index + 1
    if misplaced is False:
        return False
    else: return True
def emojified(guess: str, secret: str) -> str:
    """Uses the contains_char function to determine the color emojis to return."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    accuracy: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            accuracy = accuracy + GREEN_BOX
            index = index + 1
        elif contains_char(secret, guess[index]) == True:
            accuracy = accuracy + YELLOW_BOX
            index = index + 1
        else:
            accuracy = accuracy + WHITE_BOX
            index = index + 1
    return accuracy
def input_guess(ex_len: int) -> str:
    """Ask user for a word that matches the designated length."""
    guess: str = input(f"Enter a {ex_len} character word: ").lower()
    while len(guess) < ex_len or len(guess) > ex_len:
        guess = input(f"That wasn't {ex_len} chars! Try again: ").lower()
    else: return guess
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    playing: bool = True
    GREEN_BOX: str = "\U0001F7E9"
    right = GREEN_BOX * 5
    while turn <= 6 and playing is True:
        print(f"=== Turn {turn}/6 ===")
        attempt = emojified(input_guess(5), "codes")
        print(attempt)
        if attempt == right:
            print(f"You won in {turn}/6 turns!")
            playing = False
        else: turn = turn + 1
    if turn > 6:
        print("X/6 - Sorry, try again tommorow!")
if __name__ == "__main__":
    main()