import art
import random



def computerhand():
    while sum(computer_card) < 21:
        computer_choice_card = random.choice(cards)
        computer_card.append(computer_choice_card)
        if sum(computer_card) >= 17:
            return computer_card

def computervsyou():
    if sum(player_card) > 21 and sum(computer_card) > 21:
        print("Draw.")
    elif sum(player_card) > 21 and sum(computer_card) < 21:
        print("You lose...")
    elif sum(player_card) <= 21 and sum(computer_card) <= 21 and sum(player_card) == sum(computer_card):
        print("Draw.")
    elif sum(player_card) <= 21 and sum(computer_card) <= 21 and sum(player_card) > sum(computer_card):
        print("You win!!!")
    elif sum(player_card) <=21 and sum(computer_card) <= 21 and sum(player_card) < sum(computer_card):
        print("You lose...")
    elif sum(player_card) <=21 and sum(computer_card) > 21:
        print("You win!!!")


def owarinotoki():
    finished = True
    computerhand()
    print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
    computervsyou()

game = True

while game:
    gamestart = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_card = []
    computer_card = []
    finished = False

    if gamestart == "y":
        print(art.logo)
        choice_cards_first = random.choices(cards, k=2)
        player_card.extend(choice_cards_first)
        print(f"Your cards:{choice_cards_first}, current score: {sum(player_card)}")
        computer_choice_card_first = random.choice(cards)
        computer_card.append(computer_choice_card_first)
        print(f"Computer's first card: {computer_choice_card_first}")
        game_finished = input("Type 'y' to get another card, type 'n' to pass: ")

        while not finished:
            if game_finished == "y":
                choice_cards = random.choice(cards)
                player_card.append(choice_cards)
                print(f"Your cards:{player_card}, current score: {sum(player_card)}")

                if sum(player_card) > 21:
                    finished = True
                    computerhand()
                    print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
                    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
                    computervsyou()

                elif sum(player_card) == 21:
                    finished = True
                    computerhand()
                    print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
                    print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
                    computervsyou()

                elif sum(player_card) < 21:
                    print(f"Computer's first card: {computer_choice_card_first}")
                    game_finished = input("Type 'y' to get another card, type 'n' to pass: ")

            if game_finished == "n":
                finished = True
                computerhand()
                print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
                print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
                computervsyou()