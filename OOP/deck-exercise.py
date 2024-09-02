class Deck:
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]
    
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
    
    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        return [card.present() for card in self.cards]
    
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def present(self):
        return f'{self.value} of {self.suit}'


my_deck = Deck()
my_deck.shuffle()
print(my_deck.get_remaining())
print(my_deck.count_remaining())
print(my_deck.deal())
print(my_deck.deal())
print(my_deck.deal())
print(my_deck.deal())
print(my_deck.get_remaining())
print(my_deck.count_remaining())