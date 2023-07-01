from classes import Chips, Deck, Hand

deck_of_cards = Deck()
deck_of_cards.shuffle()
user = Hand()
computer = Hand()
chips = Chips()


def take_bet():
    try:
        bet = int(input('Please enter your bet in number: '))
    except ValueError:
        print('Please make sure to enter a valid number.')
        take_bet()
    else:
        chips.place_bet(bet)


def new_game_setup():
    print('\nWelcome to Blackjack! \n')
    take_bet()
    for _ in range(2):
        dealt_cards = deck_of_cards.deal()
        user.add_card(dealt_cards[0])
        computer.add_card(dealt_cards[1])
    print(f'Computer has {computer.cards[-1]} and one more card')
    print(f'You have {user.cards[0]} and {user.cards[1]}')
    print(f'Your cards\' sum is: {user.value}')
    start_playing()


def start_playing():
    while True:
        if check_for_blackjack():
            break
        user.adjust_for_ace()
        computer.adjust_for_ace()
        user_choice = input('Enter h for hit or s for stand: ')
        if user_choice == 'h':
            hit_or_stand('hit', user)
            if user.value > 21:
                find_out_the_winner()
                break
        else:
            hit_or_stand('stand', user)
            while computer.value < 17:
                hit_or_stand('hit', computer)
            else:
                hit_or_stand('stand', computer)
                break


def hit_or_stand(choice, player):
    match choice:
        case 'hit':
            player.add_card(deck_of_cards.hit())
            if player == user:
                print(f'Your cards are: \n{user}')
                print(f'Your new total is: {player.value}')
        case 'stand':
            if player == computer:
                print(f'Computer\'s cards are: \n{computer}')
                print(f'Computer\'s new total is: {player.value}')
                find_out_the_winner()


def check_for_blackjack():
    if computer.value == 21:
        print(f'Computer wins with a blackjack: {computer.value}')
        chips.lose_bet()
        print(f'Total chips => {chips.total}')
        reset()
        return True
    elif user.value == 21:
        print(f'You win with a blackjack: {user.value}')
        chips.win_bet()
        print(f'Total chips => {chips.total}')
        reset()
        return True


def find_out_the_winner():
    if computer.value > 21:
        print(f'Computer busts. It has a total of {computer.value} You win!')
        chips.win_bet()
        print(f'Total chips => {chips.total}')
    elif user.value > 21:
        print(f'Computer wins! You went over 21. Your total was {user.value}')
        chips.lose_bet()
        print(f'Total chips => {chips.total}')
    elif computer.value > user.value:
        print(f'Computer wins {computer.value} to {user.value}')
        chips.lose_bet()
        print(f'Total chips => {chips.total}')
    elif user.value > computer.value:
        print(f'You win {user.value} to {computer.value}')
        chips.win_bet()
        print(f'Total chips => {chips.total}')
    else:
        print('It is a tie!')
    reset()


def reset():
    play_again = input('Would you like to play again? (y/n): ')
    if play_again == 'y':
        user.reset()
        computer.reset()
        chips.bet = 0
        deck_of_cards.reset()
        deck_of_cards.shuffle()
        new_game_setup()


if __name__ == '__main__':
    new_game_setup()
