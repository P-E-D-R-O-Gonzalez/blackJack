import random

# game class #
class Game:
	def play(self):
		game_number = 0;
		games_to_play = 0;
		while games_to_play <= 0:
			try:
				games_to_play = int(input("How many games do you want to play? "))
			except:
				print("You must enter a number.")

		while game_number < games_to_play:
			game_number += 1
			# deck in game
			deck1 = Deck()
			deck1.shuffle()
			# hand in game
			player_hand = Hand()
			dealer_hand = Hand(dealer=True)
			# deals starting cards
			for i in range(2):
				player_hand.add_card(deck1.deal(2))
				dealer_hand.add_card(deck1.deal(2))
			print()
			print("*" * 30)
			print(f"Game {game_number} of {games_to_play}")
			player_hand.display()
			dealer_hand.display()

			if self.check_winner(player_hand, dealer_hand):
				continue
			choice = ""
			while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
				choice = input("Please choose 'Hit' or 'Stand': ").lower()
				print()
				while choice not in ["h", "s", "hit", "stand"]:
					choice = input("Please enter 'Hit' or 'Stand' (or H/S): ").lower()
					print()
				if choice in ["h", "hit"]:
					player_hand.add_card(deck1.deal(1))
					player_hand.display()
			if self.check_winner(player_hand, dealer_hand):
				continue
			player_hand_value = player_hand.get_value()
			dealer_hand_value = dealer_hand.get_value()

			while dealer_hand_value < 17:
				dealer_hand.add_card(deck1.deal(1))
				dealer_hand_value = dealer_hand.get_value()
			# end of game all is revealed
			dealer_hand.display(show_all_dealer_cards=True)
			if self.check_winner(player_hand, dealer_hand):
				continue
			print("final results")
			print("your hand:",player_hand_value)
			print("Dealer's hand",dealer_hand_value)

			self.check_winner(player_hand, dealer_hand, True)
			print("\n\n\nGracias por jugar!!!")
			
	def check_winner(self, player_hand, dealer_hand,game_over=False):
		if not game_over:
			if player_hand.value > 21:
				print("You busted. Dealer wins!")
				return True
			elif dealer_hand.value > 21:
				print("Dealer busted. You win!")
				return True
			elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
				print("Both players have blackjack! Tie!")
				return True
			elif player_hand.is_blackjack():
				print("You have blackjack! You win!")
				return False
			elif dealer_hand.is_blackjack():
				print("Dealer has blackjach! Dealer wins!")
				return False
		else:
			if player_hand.value > dealer_hand.value:
				print("You win!")
			elif player_hand.value == dealer_hand.value:
				print("Tie!")
			else:
				print("Dealer wins!")
				return True
		return False
# Hand class #
class Hand:
	def __init__(self, dealer=False):
		self.cards = []
		self.value = 0
		self.dealer = dealer

	def add_card(self, card_list):
		self.cards.extend(card_list)
		
	def calculate_value(self):
		has_ace = False;
		self.value = 0
		for card in self.cards:
			card_value = int(card.rank["value"])
			self.value += card_value
			if card.rank["rank"] == "Ace":
				has_ace = True
		if has_ace and self_value + 10 <= 21:
			self_value -= 10
			
	def get_value(self):
		self.calculate_value()
		return self.value

	def is_blackjack(self):
		return self.get_value() == 21

	def display(self, show_all_dealer_cards=False):
		print(f'''{"Dealer's" if self.dealer else "Your"} hand:''')
		for index, card in enumerate(self.cards):
			if index == 0 and self.dealer \
			and not show_all_dealer_cards and not self.is_blackjack:
				print("hidden")
			else:
				print(card)
		if not self.dealer:
			print("Value", self.get_value())
# Card class #
class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
	def __str__(self):
		return f"{self.rank['rank']} of {self.suit}"

# Deck class #
class Deck:
	def __init__(self):
		# variables #
		self.cards = []
		suits = ["♥", "♦", "♣", "♠"]
		ranks = [
			{"rank": "A", "value": 11}, 
			{"rank": "2", "value": 2}, 
			{"rank": "3", "value": 3},
			{"rank": "4", "value": 4}, 
			{"rank": "5", "value": 5},
			{"rank": "6", "value": 6},
			{"rank": "7", "value": 7},
			{"rank": "8", "value": 8},
			{"rank": "9", "value": 9},
			{"rank": "10", "value": 10},
			{"rank": "J", "value": 10},
			{"rank": "Q", "value": 10},
			{"rank": "K", "value": 10},
			]
		# fills cards list #
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit,rank))
	# shuffles cards #
	def shuffle(self):
		if(len(self.cards)>1):
			random.shuffle(self.cards)
	
	def deal(self,number):
		cards_dealt = []
		for x in range(number):
			if(len(self.cards) > 0):
				card = self.cards.pop()
				cards_dealt.append(card)
			return cards_dealt

# start of program runnning #
g = Game()
g.play()