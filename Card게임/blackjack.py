import random
playing = True
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.card_list_all = []

        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.card_list_all.append(card)

    def shuffle_card(self):
        random.shuffle(self.card_list_all)
    
    def deal_one(self):
        return self.card_list_all.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value = 10
            self.aces -= 1

class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bets? "))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you not enough chips!! You have : {chips.total}")
            else:
                break

def hit(deck, hand):
    single_card = deck.deal_one()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Hit or Stand? Enter h or s? ")

        if x[0].lower() == "h":
            hit(deck, hand)
        
        elif x[0].lower() == "s":
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, please enter h or s only")
            continue
        break

def show_some(player, dealer):
    print("\nDealer Hand: ")
    print("First card hidden")
    print(dealer.cards[1])


    print("\nPlayer Hand: ")
    for card in player.cards:
        print(card)
    print(player.value)

def show_all(player, dealer):
    print("\nDealer Hand: ")
    for card in dealer.cards:
        print(card)
    print(f"Value of Dealer's hand is:{dealer.value}")
    print(dealer.value)

    print("\nPlayer Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of Player's hand is:{player.value}")
    print(player.value)

def player_busts(player,dealer,chips):
    print("Bust Player")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player Wins! Dealer Busted")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Bust Player")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player Tie!")


while True:
    print("Welcome to BlackJack")

    deck = Deck()
    deck.shuffle_card()

    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)  

    print(f"Player total chipa are at {player_chips.total}")

    new_game = input("would you like play another hand? y/n ")

    if new_game[0].lower() == "y":
        playing =True
        continue
    else:
        print("good bye")
        break