class House():
    counter = 0 # class variable

    def __init__(self, address, area, price):
        self.addres = address
        self.area = area
        self.price = price
        House.counter += 1

        House.quality = 'low' # class variable that always takes a default value in the constructor
        self.quality = 'medium' # instance variable
        quality = 'high' # local variable

        print(House.quality, self.quality, quality)

    def present(self):
        print('The house at', self.addres, 'has an area of', self.area, 'and costs', self.price)
    

solo_house = House('zona 17 GT', 130, 540_000)
solo_house.present()

print(House.counter) # 1
print(House.quality) # low
print(solo_house.quality) # medium
print()


# Changing class variables
House.counter = 10
House.quality = 'way worse than before'


new_house = House('zona 11', 150, 600_00)
new_house.present()

print(House.counter) # 11 > changes because the definition of this variable is outside the constructor
print(House.quality) # low > this class variable gets again the value of 'low' because its definition is inside the constructor
print(solo_house.quality) # medium
