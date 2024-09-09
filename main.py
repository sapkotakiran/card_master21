import random

# Initialize the base card dictionary with values
base_card_dict = {i: i for i in range(2, 11)}
base_card_dict.update({'j': 11, 'q': 12, 'k': 13})
base_card_dict['A'] = 1


# Create and shuffle a full deck (4 sets of cards)
def shuffle_deck():
    full_deck = []
    for _ in range(4):
        full_deck.extend(base_card_dict.items())
    random.shuffle(full_deck)
    return full_deck


# Function to simulate the computer's turn with decision making
def computer_turn(deck_index, full_deck):
    computer_sum = 0
    computer_cards = []

    # Draw the initial 2 cards for the computer
    for _ in range(2):
        card = full_deck[deck_index]
        deck_index += 1
        computer_sum += card[1]
        computer_cards.append(card)

    print(f"\nComputer's turn:")
    for card in computer_cards:
        print(f"Computer drew: {card[0]} with value {card[1]}")
    print(f"Computer's total sum after initial draw: {computer_sum}")

    # Computer decision making: draw cards if sum <= 16, stop otherwise
    while computer_sum <= 16 and deck_index < len(full_deck):
        card = full_deck[deck_index]
        deck_index += 1
        computer_sum += card[1]
        computer_cards.append(card)

        print(f"Computer drew: {card[0]} with value {card[1]}")
        print(f"Computer's total sum so far: {computer_sum}")

        if computer_sum >= 17:
            print("Computer decides to stop.")
            break

    print(f"Computer's final total sum: {computer_sum}")
    return computer_sum, deck_index


# Function to draw cards until the user says 'stop'
def draw_cards(full_deck):
    total_sum = 0
    deck_index = 0
    user_cards = []

    # Draw the initial 2 cards for the user
    for _ in range(2):
        card = full_deck[deck_index]
        deck_index += 1
        total_sum += card[1]
        user_cards.append(card)
        print(f"You drew: {card[0]} with value {card[1]}")

    print(f"Total sum after initial draw: {total_sum}")

    # Keep drawing cards until the user says stop or the total sum exceeds 21
    while True:
        if total_sum > 21:
            print("You lose!")
            return None, deck_index

        another_card = input("Do you want to draw another card? Type 'yes' to continue or 'stop' to finish: ").lower()

        if another_card == 'stop':
            break

        if another_card == 'yes':
            if deck_index >= len(full_deck):
                print("No more cards left in the deck.")
                return total_sum, deck_index
            card = full_deck[deck_index]
            deck_index += 1
            total_sum += card[1]
            user_cards.append(card)

            print(f"You drew: {card[0]} with value {card[1]}")
            print(f"Total sum so far: {total_sum}")
        else:
            print("Invalid input. Please type 'yes' to continue or 'stop' to finish.")

    return total_sum, deck_index


# Main game loop
def main():
    while True:
        print("Welcome to the card game!")

        # Shuffle the deck for a new game
        full_deck = shuffle_deck()

        user_sum, deck_index = draw_cards(full_deck)

        if user_sum is not None and user_sum <= 21:
            print(f"\nUser sum after drawing cards: {user_sum}")
            print(f"Deck index after user turn: {deck_index}")

            # If the user did not lose, the computer takes its turn
            print("\nNow it's the computer's turn.")
            computer_sum, deck_index = computer_turn(deck_index, full_deck)

            print(f"\nComputer sum after its turn: {computer_sum}")

            # Determine the winner
            if computer_sum > 21:
                print("Computer loses! You win!")
            elif user_sum > computer_sum:
                print("You win!")
            elif user_sum < computer_sum:
                print("Computer wins!")
            else:
                print("It's a tie!")
        else:
            print("Game over.")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? Type 'yes' to play again or 'no' to quit: ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break



main()
