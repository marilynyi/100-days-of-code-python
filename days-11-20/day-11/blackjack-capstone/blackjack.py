import random
import os
from art import logo

os.system("clear")

def main():

    end_game = False

    # Loop while user wants to keep playing
    while not end_game:

        # Initialize user and dealer hands
        user_cards = []
        dealer_cards = []

        # Deal two cards each for user and dealer
        for _ in range(2):
            user_cards.append(deal_card())
            dealer_cards.append(deal_card())

        first_turn_over = False

        # User starts turn
        while not first_turn_over:

            # Show project header
            print(logo)

            # Total up points in both hands
            user_points = sum_cards(user_cards)
            dealer_points = sum_cards(dealer_cards)

            # Display cards to user
            print(f"\n---- You: {user_points} points with {user_cards}")
            print(f"---- Dealer: {dealer_cards[0]} points with [🂠][{dealer_cards[0]}]")

            # Check if game is over
            if user_points == 0 or dealer_points == 0 or user_points > 21:
                first_turn_over = True
            else:
                # Ask user to draw another card or end turn
                continue_game = int(input("\nType 1 to Hit or 0 to Stand: "))
                if continue_game == 1:
                    user_cards.append(deal_card())
                    os.system("clear")
                else:
                    first_turn_over = True

        os.system("clear")
        print(logo)

        # Dealer's turn
        while dealer_points < 17 and dealer_points != 0:
            dealer_cards.append(deal_card())
            dealer_points = sum_cards(dealer_cards)

        # Display final cards
        print(f"\n---- You: {user_points} points with {user_cards}")
        print(f"---- Dealer: {dealer_points} points with {dealer_cards}")

        # Check both hands for win conditions
        print(f"\n{check_scores(user_points, dealer_points)}")

        # Ask user to continue or quit the game
        play_again = int(input("\nType 1 to Play Again or 0 to Quit: "))
        if play_again == 1:
            pass
        else:
            end_game = True

        os.system("clear")


def deal_card():
    """Deal random card"""
    ## Use the following list as the deck of cards:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def sum_cards(cards):
    """Sum up total points in card hand"""
    # Blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    # Ace value of 1 instead of 11 if points over 21
    if 11 in cards and sum(cards) > 21:
        ace_index = cards.index(11)
        cards[ace_index] = 1
    return sum(cards)


def check_scores(user_points, dealer_points):
    """Check user points against computer points for win conditions"""
    # Win conditions in order
    if user_points == dealer_points and user_points == 0:
        return "No winner. It's a draw."
    elif user_points == 0:
        return "You got a Blackjack. You win."
    elif dealer_points == 0:
        return "Dealer got a Blackjack. You lose."
    elif user_points > 21:
        return "You went over. You lose."
    elif dealer_points > 21:
        return "Dealer went over. You win."
    elif user_points == dealer_points:
        return "No winner. It's a draw."
    elif user_points > dealer_points:
        return f"You win with {user_points} points."
    else:
        return f"Dealer wins with {dealer_points} points."


if __name__ == "__main__":
    main()
