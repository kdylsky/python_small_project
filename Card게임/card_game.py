import random
from collections import deque

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
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

class Player:
    def __init__(self, name):
        self.name = name
        self.play_card_list = deque()
    
    def add_card(self, new_cards):
        if type(new_cards) == type([]):
            self.play_card_list.extend(new_cards)
        else:
            self.play_card_list.append(new_cards)

    def remove_card(self):
        return self.play_card_list.popleft()

    def __str__(self):
        return f"Player {self.name} has {len(self.play_card_list)} cards"


print("start card game")
new_deck =Deck()
new_deck.shuffle_card()

game_on = True
round = 0
player_one = Player("Tim")
player_two = Player("Kim")

for i in range(26):
    player_one.add_card(new_deck.deal_one())
    player_two.add_card(new_deck.deal_one())

while game_on:
    round += 1
    print(f"stard {round}th")

    if len(player_one.play_card_list) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
    
    if len(player_two.play_card_list) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    player_game_card_list = []
    player_one_game_card = []
    player_two_game_card = []

    player_one_game_card.append(player_one.remove_card())
    player_two_game_card.append(player_two.remove_card())

    player_game_card_list.extend(player_one_game_card)
    player_game_card_list.extend(player_two_game_card)

    war_on = True
    while war_on:
        if player_one_game_card[-1].value > player_two_game_card[-1].value:
            random.shuffle(player_game_card_list)
            player_one.add_card(player_game_card_list)
            war_on = False

        elif player_one_game_card[-1].value < player_two_game_card[-1].value:
            random.shuffle(player_game_card_list)
            player_two.add_card(player_game_card_list)
            war_on = False

        else:
            print("war")
            if len(player_one.play_card_list) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break
            
            elif len(player_two.play_card_list) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player Two Loses!")
                game_on = False
                break
                
            else:
                player_game_card_list.clear()
                for i in range(5):
                    player_one_game_card.append(player_one.remove_card())
                    player_two_game_card.append(player_two.remove_card())

                player_game_card_list.extend(player_one_game_card) 
                player_game_card_list.extend(player_two_game_card)
                
    if round > 50:
        print("It is a tie game")
        print(f"Player One Card : {len(player_one.play_card_list)}")
        print(f"Player Two Card : {len(player_two.play_card_list)}")
        break
