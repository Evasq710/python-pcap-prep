class House():
    counter = 0

    def __init__(self, address, area, price):
        self.addres = address
        self.area = area
        self.price = price
        House.counter += 1

        House.quality = 'low'
        self.quality = 'medium'
        quality = 'high'

        print(House.quality, self.quality, quality)

    def present(self):
        print('The house at', self.addres, 'has an area of', self.area, 'and costs', self.price)

    def __reduce_price(self):
        self.price -= self.price*0.1
        print('New price:', self.price)
    
    # This is a special method that can be used to set what we want to display when the user does something like print(<object>)
    def __str__(self):
        return 'HOUSE OBJECT: This is the ' + str(House.counter) + ' house'
    
solo_house = House('zona 17 GT', 130, 540_000)
solo_house.present()
# solo_house.__reduce_price() # attribute error
solo_house._House__reduce_price() # accesing to a "private" method

print(House.__dict__)

# Without the __str__ method: <__main__.House object at 0x000002064A5F6870>
# With the __str__method: HOUSE OBJECT: This is the 1 house
print(solo_house)