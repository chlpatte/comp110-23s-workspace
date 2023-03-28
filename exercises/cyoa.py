"""My own adventure!"""

__author__ = "730580489"

import random
player: str = ""
points: int = 0
fon: list[str] = ["face", "number"]
numbers: list[int] = [2, 3, 4, 5, 6, 7, 8, 9, 10]
faces: list[str] = ["Ace", "King", "Queen", "Jack"]
suits: list[str] = ["Spades", "Clubs", "Hearts", "Diamonds"]
color: list[str] = ["black", "red"]

def greet() -> None:
    global player
    print("Welcome, are you ready play the ultimate card guessing game? You will be guessing every aspect of a random card. The card's color, suit, number, or face. You will wage points based on how confident you are.")
    player = input("What is your name? ")
    ready = input(f"{player} are you ready? Please answer with yes or no. ").lower()
    while ready != "yes" and ready != "no":
        ready = input(f"{player} that was not yes or no please try again. ").lower()
    if ready == "no":
        out_opt()


def out_opt() -> None:
    global points
    print(f"Goodbye, you were able to accumulate {points} points")
    quit()


def default() -> None:
    global points
    points += 1000
    print(f"{player} you have selected to play using the default settings. You will begin with {points} points and will be guessing every possible aspect of the card.")
    ready = input(f"{player} are you okay with these settings? Please answer with yes or no. ").lower()
    while ready != "yes" and ready != "no":
        ready = input(f"{player} that was not yes or no please try again. ").lower()
    if ready == "no":
        points -= 1000
        cust_opt()


def game(num: int) -> int:
    global points
    num = points
    guessing_card = input(f"{player} did you select to guess what card value it is? Please answer with yes or no. ")
    while guessing_card != "yes" and guessing_card != "no":
        guessing_card = input(f"{player} that was not yes or no please try again. ").lower()
    guessing_fon = input(f"{player} did you select to guess whether the card is a face or number card? Please answer with yes or no. ")
    while guessing_fon != "yes" and guessing_fon != "no":
        guessing_fon = input(f"{player} that was not yes or no please try again. ").lower()
    guessing_suit = input(f"{player} did you select to guess what suit the card is? Please answer with yes or no. ")
    while guessing_suit != "yes" and guessing_suit != "no":
        guessing_suit = input(f"{player} that was not yes or no please try again. ").lower()
    guessing_color = input(f"{player} did you select to guess what color the card is? Please answer with yes or no. ")
    while guessing_color != "yes" and guessing_color != "no":
        guessing_color = input(f"{player} that was not yes or no please try again. ").lower()
    while guessing_color == "yes" and guessing_fon == "no" and guessing_suit == "no" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_color = "no"
            return points
    while guessing_fon == "yes" and guessing_color == "no" and guessing_suit == "no" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_fon = "no"
            return points
    while guessing_suit == "yes" and guessing_fon == "no" and guessing_color == "no" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
        answer = random.choice(suits)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_suit = "no"
            return points
    while guessing_card == "yes" and guessing_fon == "no" and guessing_suit == "no" and guessing_color == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        answer = random.choice(fon)
        if answer == "face":
            answer = random.choice(faces)
        else: 
            answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            return points
    while guessing_card == "yes" and guessing_fon == "yes" and guessing_suit == "no" and guessing_color == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        if answer == "face":
            answer = random.choice(faces)
        else: 
            answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_fon = "no"
            return points
    while guessing_card == "yes" and guessing_fon == "yes" and guessing_suit == "yes" and guessing_color == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
        answer = random.choice(suits)
        if guess == answer:
            guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
            answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        if answer == "face":
            answer = random.choice(faces)
        else: 
            answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_fon = "no"
            guessing_suit = "no"
            return points
    while guessing_card == "yes" and guessing_fon == "yes" and guessing_suit == "no" and guessing_color == "yes" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
            answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        if answer == "face":
            answer = random.choice(faces)
        else: 
            answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_fon = "no"
            guessing_color = "no"
            return points
    while guessing_card == "yes" and guessing_fon == "yes" and guessing_suit == "yes" and guessing_color == "yes" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
            if answer == "red":
                answer = suits[random.randint(2, 3)]
            else:
                answer = suits[random.randint(0, 1)]
        if guess == answer:
            guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
            answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        if answer == "face":
            answer = random.choice(faces)
        else: 
            answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_fon = "no"
            guessing_suit = "no"
            guessing_color = "no"
            return points
    while guessing_color == "yes" and guessing_fon == "no" and guessing_suit == "yes" and guessing_card == "yes" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
            if answer == "red":
                answer = suits[random.randint(2, 3)]
            else:
                answer = suits[random.randint(0, 1)]
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
            answer = random.choice(fon)
            if answer == "face":
                answer = random.choice(faces)
            else: 
                answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_suit = "no"
            guessing_color = "no"
            return points
    while guessing_color == "yes" and guessing_fon == "no" and guessing_suit == "no" and guessing_card == "yes" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
            answer = random.choice(fon)
            if answer == "face":
                answer = random.choice(faces)
            else: 
                answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_color = "no"
            return points
    while guessing_color == "no" and guessing_fon == "no" and guessing_suit == "yes" and guessing_card == "yes" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
        answer = random.choice(suits)
        if guess == answer:
            guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
            answer = random.choice(fon)
            if answer == "face":
                answer = random.choice(faces)
            else: 
                answer = random.choice(numbers)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_card = "no"
            guessing_suit = "no"
            return points
    while guessing_color == "yes" and guessing_fon == "no" and guessing_suit == "yes" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
            if answer == "red":
                answer = suits[random.randint(2, 3)]
            else:
                answer = suits[random.randint(0, 1)]
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_color = "no"
            guessing_suit = "no"
            return points
    while guessing_color == "yes" and guessing_fon == "yes" and guessing_suit == "yes" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} Is the card black or red? ").lower()
            answer = random.choice(color)
        if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
            if answer == "red":
                answer = suits[random.randint(2, 3)]
            else:
                answer = suits[random.randint(0, 1)]
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_color = "no"
            guessing_suit = "no"
            guessing_fon = "no"
            return points
    while guessing_color == "yes" and guessing_fon == "yes" and guessing_suit == "no" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} Is the card black or red? ").lower()
            answer = random.choice(color)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_color = "no"
            guessing_fon = "no"
            return points
    while guessing_fon == "yes" and guessing_color == "no" and guessing_suit == "yes" and guessing_card == "no" and num > 0:
        wage = int(input(f"{player} you have {num} points. How many points would you like to wage? "))
        if wage > num or wage < 1:
            wage = int(input(f"{player} you have enter an invalid number of points to wage, please try again. "))
        winnings: int = wage * 2
        guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)
        if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds ").lower()
            answer = random.choice(suits)
        if guess == answer:
            num += winnings
            points = num
            print(f"{player} you now have {num} points!")
        else:
            num -= wage
            points = num
            print(f"Wrong! {player} you now have {num} points!")
        con = input(f"{player} would you like to continue on these settings? Please answer with yes or no. ").lower()
        while con != "yes" and con != "no":
            con = input(f"{player} that was not yes or no please try again. ").lower()
        if con == "no":
            guessing_suit = "no"
            guessing_fon = "no"
            return points
    return points


def cust_opt() -> None:
    """Here the player will choose how difficult the guessing game will be by determining which aspects of the card they want to guess. Depending on how difficult they make it determines how many points they start with."""
    global points
    global player
    print(f"{player} you have entered the custom settings, where you control which aspects of the card you will be guessing.")
    print(f"{player} you currently have {points} points. For each aspect you want to guess you will recieve points based on its difficulty.")
    print(f"{player} please answer the following questions with either yes or no.")
    color = input(f"{player} do you want to guess the color of the card? ").lower()
    while color != "yes" and color != "no":
        color = input(f"{player} that was not yes or no please try again. ").lower()
    if color == "yes":
        points += 100
        print(f"+ 100 points")
    suit = input(f"{player} do you want to guess the suit of the card? ").lower()
    while suit != "yes" and suit != "no":
        suit = input(f"{player} that was not yes or no please try again. ").lower()
    if suit == "yes":
        points += 300
        print(f"+ 300 points")
    fon = input(f"{player} do you want to guess if the card is a face card (includes aces) or a number card? ").lower()
    while fon != "yes" and fon != "no":
        fon = input(f"{player} that was not yes or no please try again. ").lower()
    if fon == "yes":
        points += 200
        print(f"+ 200 points")
    card = input(f"{player} do you want to guess what the card value is? ").lower()
    while card != "yes" and card != "no":
        card = input(f"{player} that was not yes or no please try again. ").lower()
    if card == "yes":
        points += 400
        print(f"+ 400 points")
    print(f"{player} you currently have {points} points to start the game with.")
    ready = input(f"{player} would you like to continue with this amount of points? ").lower()
    while ready != "yes" and ready != "no":
        ready = input(f"{player} that was not yes or no please try again. ").lower()
    if ready == "no":
        greet()


def main() -> None:
    """The entrypoint and main game loop!"""
    global points
    global player
    greet()
    custom = input(f"{player} would you like to customize your experience or use the default difficulty? Please answer with custom or default. ").lower()
    while custom != "custom" and custom != "default":
        custom = input(f"{player} that was not custom or default please try again. ").lower()
    if custom == "custom":
        cust_opt()
    else:
        default()
    game(points)
    print(f"{player} you have {points} points")
    set_or_quit = input(f"{player} would you like to change your settings or quit? Please answer with settings or quit. ").lower()
    while set_or_quit != "settings" and set_or_quit != "quit":
        set_or_quit = input(f"{player} that was not settings or quit please try again. ").lower()
    if set_or_quit == "quit":
        out_opt()
    else:
        main()



if __name__ == "__main__":
    main()