from classes import Deck, Player

player_one = Player('player_one')
player_two = Player('player_two')
deck_of_cards = Deck()
deck_of_cards.shuffle()

for _ in range(26):
    player_one.add_cards(deck_of_cards.deal())
    player_two.add_cards(deck_of_cards.deal())


def play_one_card():
    is_war = False
    while not is_game_over() and not is_war:
        player_one_card = player_one.remove_one()
        player_two_card = player_two.remove_one()
        cards_on_the_table = [player_one_card, player_two_card]

        if player_one_card.value > player_two_card.value:
            player_one.add_cards(cards_on_the_table)
        elif player_one_card.value < player_two_card.value:
            player_two.add_cards(cards_on_the_table)
        else:
            is_war = True
            print('Entering war')
            if have_sufficient_cards(game_state='war'):
                play_war_card(cards_on_the_table)
            else:
                edge_case_comparison()


def play_war_card(table):
    player1_cards = []
    player2_cards = []
    for _ in range(5):
        player1_cards.append(player_one.remove_one())
        player2_cards.append(player_two.remove_one())
        table.append(player1_cards[-1])
        table.append(player2_cards[-1])

    if player1_cards[-1].value > player2_cards[-1].value:
        player_one.add_cards(table)
        if not is_game_over() and have_sufficient_cards(game_state='normal'):
            play_one_card()
    elif player1_cards[-1].value < player2_cards[-1].value:
        player_two.add_cards(table)
        if not is_game_over() and have_sufficient_cards(game_state='normal'):
            play_one_card()
    else:
        print('Entering war again')
        if not is_game_over() and have_sufficient_cards(game_state='war'):
            play_war_card(table)


def have_sufficient_cards(game_state):
    match game_state:
        case 'normal':
            return len(player_one.cards) > 0 and len(player_two.cards) > 0
        case 'war':
            return len(player_one.cards) >= 5 and len(player_two.cards) >= 5


def is_game_over():
    if len(player_one.cards) == 0:
        print('Player two wins!')
        return True
    elif len(player_two.cards) == 0:
        print('Player one wins!')
        return True
    else:
        return False


def edge_case_comparison():
    if len(player_one.cards) > len(player_two.cards):
        print(f'Player two, you can\'t afford to go to war. You only have {len(player_two.cards)} cards')
        print(f'Player one wins with {len(player_one.cards)} cards!')
    else:
        print(f'Player one, you can\'t afford to go to war. You only have {len(player_one.cards)} cards')
        print(f'Player two wins with {len(player_two.cards)} cards!!')


if __name__ == '__main__':
    play_one_card()
