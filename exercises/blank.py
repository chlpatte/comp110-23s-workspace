guess = input(f"{player} Is the card black or red? ").lower()
        answer = random.choice(color)

guess = input(f"{player} Is the card a face card or number card? Please answer face or number ").lower()
        answer = random.choice(fon)

guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds").lower()
        answer = random.choice(suits)

guess = input(f"{player} What card value is it? Please answer a number 2-10, King, Queen, Ace, or Jack").lower()
        answer = random.choice(fon)
        if answer == "face":
            answer = random.choice(faces)
        else: answer = random.choice(numbers)
if guess == answer:
            guess = input(f"{player} What is suit of the card? Please answer Spades, Clubs, Hearts, or Diamonds").lower()
            if answer == "red":
                answer = suits[random.randint(2, 3)]
            else:
                answer = suits[random.randint(0, 1)]