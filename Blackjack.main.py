import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(logo)
print("Welcome to Blackjack!\n")
game = input("Do you want to play a game of Blackjack? Type 'Yes or 'No'\n").lower()

def start_deal():
    if game == 'yes':
        player_hand = random.sample(cards, 2)
        computer_hand = random.sample(cards, 2)

        def calculate_score(hand):
            score= sum(hand)
            while score > 21 and 11 in hand:
                hand.remove(11)
                hand.append(1)
                score =sum(hand)
            return score

        print(f"Your Cards: {player_hand} Current Score: {sum(player_hand)}\nComputers's first card: {computer_hand[0]}")


        continue_game = True

        while continue_game:
            next_hand = input("Type 'yes' to get another card, type 'no' to pass: ").lower()

            if next_hand == 'yes':
                player_deal = random.choice(cards)
                player_hand.append(player_deal)
                print(f"You drew: {player_deal}")
                print(f'Your cards: {player_hand} Current Score: {sum(player_hand)}')
                print(computer_hand[0])
                if sum(player_hand) > 21:
                    print("You went over 21, Game over")
                    continue_game = False

            elif next_hand == 'no':
                print(f"Your final hand is: {player_hand} Final Score:{sum(player_hand)}")
                print(f"Computer's hand: {computer_hand} Current Score:{sum(computer_hand)}")

                while sum(computer_hand) < 17:
                    comp_card = random.choice(cards)
                    computer_hand.append(comp_card)
                    print(f'Computer Drew: {comp_card} -> {computer_hand} Current Score: {sum(computer_hand)}')

                player_score = sum(player_hand)
                computer_score = sum(computer_hand)

                print(f"\nFinal Score\nYou: {player_score}\nComputer: {computer_score}")

                if computer_score > 21:
                    print("Computer over 21, You win!")
                elif player_score > 21:
                    print("You went over 21, You lose...")
                elif player_score > computer_score:
                    print("You Win!")
                elif player_score < computer_score:
                    print("You lose...")
                else:
                    print("It's a Draw WOMP WOMP")

                continue_game = False
            else:
             print("Invalid input. please type 'Yes' or 'No'.")

        play_again = input("Do you want to play again?: Type 'Yes' or 'No'").lower()
        if play_again == 'yes':

            print ("\n" * 50)
            print(logo)
            print("Thanks for playing Blackjack again!\n")
            start_deal()
        else:
            print("You chose not to play")


    else:
        print("You chose not to play")





start_deal()