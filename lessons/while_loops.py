"""Demonstrates while loops by finding low value in string"""

cards: str = "5235"

card_idx:  int = 0
low_card: int = int(cards[0])
# look at each number in the string
while card_idx < 4:
    # check if current card is less than low card
    current_card: int = int(cards[card_idx])
    if (current_card < low_card):
        # update the low card to be the value of our current card
        low_card = current_card
    card_idx = card_idx + 1
print(low_card)

xs: str = "123"
ys: str = "45"

x_idx: int = 0

while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"{xs[x_idx]}, {ys[y_idx]}")
        y_idx = y_idx + 1
    x_idx = x_idx + 1
