from classes import Chips, Deck, Hand

deck_of_cards = Deck()
deck_of_cards.shuffle()
user = Hand()
computer = Hand()


def take_bet():
    try:
        bet = int(input('Please enter your bet in number: '))
    except ValueError:
        print('Please make sure to enter a valid number.')
        take_bet()
    else:
        chip = Chips()
        chip.bet = bet


def new_game_setup():
    take_bet()
    for _ in range(2):
        dealt_cards = deck_of_cards.deal()
        user.add_card(dealt_cards[0])
        computer.add_card(dealt_cards[1])
    print(f'Computer has {computer.cards[-1]} and one more card')
    print(f'You have {user.cards[0]} and {user.cards[1]}')
    total = calculate_total(user.cards)
    print(f'Your total is: {total}')
    start_playing()


def start_playing():
    while True:
        check_for_blackjack()
        user_choice = input('Enter h for hit or s for stand: ')
        if user_choice == 'h':
            hit_or_stand('hit', user)
            user.adjust_for_ace()
            user_total = calculate_total(user.cards)
            print('Your cards are: ')
            for card in user.cards:
                print(card)
            print(f'Your new total is: {user_total}')
            if user_total > 21:
                print(calculate_total(user.cards))
                print(f'Computer wins with a total of: {calculate_total(computer.cards)}')
                play_again = input('Would you like to play again? Please enter "y" or "n"')
                if play_again == 'y':
                    reset()
                    new_game_setup()
                    break
                else:
                    break
        else:
            hit_or_stand('stand', user)
            while calculate_total(computer.cards) < 17:
                hit_or_stand('hit', computer)
            hit_or_stand('stand', computer)
            find_out_the_winner()
            break


def hit_or_stand(choice, player):
    match choice:
        case 'hit':
            player.add_card(deck_of_cards.hit())
        case 'stand':
            total = calculate_total(player.cards)
            if player == user:
                print('Your cards are: ')
                for card in user.cards:
                    print(card)
                print(f'Your new total is: {total}')
            else:
                print('Computer\'s cards are: ')
                for card in player.cards:
                    print(card)
                print(f'Computer\'s new total is: {total}')


def check_for_blackjack():
    user_total = calculate_total(user.cards)
    computer_total = calculate_total(computer.cards)
    if computer_total == 21:
        print(f'Computer wins with a blackjack: {computer_total}')
        reset()
    elif user_total == 21:
        print(f'You win with a blackjack: {user_total}')
        reset()


def calculate_total(cards):
    total = 0
    for card in cards:
        total += card.value
    return total


def find_out_the_winner():
    user_total = calculate_total(user.cards)
    computer_total = calculate_total(computer.cards)
    if computer_total == 21:
        print(f'Computer wins with a blackjack: {computer_total}')
    elif user_total == 21:
        print(f'You win with a blackjack: {user_total}')
    if computer_total > 21:
        print(f'Computer busts. It has a total of {computer_total} You win')
    elif user_total > 21:
        print(f'Computer wins! You went over 21. Your total was {user_total}')
    elif computer_total > user_total:
        print(f'Computer wins {computer_total} to {user_total}')
    elif user_total > computer_total:
        print(f'You win {user_total} to {computer_total}')
    else:
        print('It is a draw!')
    reset()


def reset():
    play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        user.reset()
        computer.reset()
        new_game_setup()


if __name__ == '__main__':
    new_game_setup()
