import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11
}

player_money = 500

def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = sum(values[card[0]] for card in hand)
    
    # ----- Ace -----
    num_aces = sum(1 for card in hand if card[0] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1

    return value

def start_new_game():
    global player_hand
    global dealer_hand
    global deck

    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

def player_hit():
    player_hand.append(deck.pop())
    print("Player draws:", " of ".join(str(item) for item in player_hand[-1]))
    return calculate_hand_value(player_hand)

def dealer_play():
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealer draws:", " of ".join(str(item) for item in dealer_hand[-1]))
        return calculate_hand_value(player_hand)

def check_winner():
    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    if player_score > 21:
        print("Player bust; dealer wins")
        return "BUST! You lose!"
    elif dealer_score > 21:
        print("Dealer bust; player wins")
        return "Dealer BUST! You win!"
    elif player_score == dealer_score:
        print("Push (tie)")
        return "TIE!"
    elif player_score > dealer_score:
        print("Player wins by score")
        return "You win!"
    else:
        print("Dealer wins by score")
        return "Dealer wins!"

def money_count(result):
    global player_money

    if result == "You win!" or result == "Dealer BUST! You win!":
        player_money += 50
    elif result == "Dealer wins!" or result == "BUST! You lose!":
        player_money -= 50

    return player_money

