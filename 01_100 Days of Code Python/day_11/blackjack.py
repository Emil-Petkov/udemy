import random


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)

    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return 'It\'s a draw.'

    elif dealer_score == 0:
        return 'Lose, opponent has Blackjack'

    elif player_score == 0:
        return 'Win with a Blackjack'

    elif player_score > 21:
        return 'You went over. You Lose'

    elif dealer_score > 21:
        return 'Opponent went over. You Win'

    elif player_score > dealer_score:
        return 'You Win'

    else:
        return 'You Lose'


def play_game():
    player_cards = []
    dealer_cards = []

    is_game_over = False

    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f'Your cards: {player_cards}, current score: {player_score}')
        print(f'Dealer first card: {dealer_cards[0]}')

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True

        player_should_deal = input("Type 'y' to get another card or type 'n' to pass: ")

        if player_should_deal == 'y':
            player_cards.append(deal_card())

        else:
            is_game_over = True

        while dealer_score != 0 and dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

        print(f'Your final hand: {player_cards}, final score: {player_score}')
        print(f'Dealer final hand: {dealer_cards}, final score: {dealer_score}')
        print(compare(player_score, dealer_score))


while input('Do you want to play a game of Blackjack? (y/n): ') == 'y':
    play_game()
