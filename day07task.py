# 10.1
class Thing:
    pass

a = Thing()
example = Thing()

# 10.2
class Thing2:
    def __init__(self,letter):
        self.letter = letter
    def info(self):
        print(f'{self.letter}')

b = Thing2('abc')
b.info()

# 10.3

class Thing3:
    def __init__(self):
        self.letter = 'xyz'
    def info(self):
        print(f'{self.letter}')

c = Thing3()
c.info()

# 10.4
class Element:
    def __init__(self):
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.number = 1
#     def info(self):
#         print(f'{self.name}, {self.symbol}, {self.number}')
# d = Element()
# d.info()

# 10.5

el_dict = {'name': 'Hydrogen','symbol': 'H', 'number': 1}
class Element:
    def __init__(self,el_dict) :
        self.name = el_dict['name']
        self.symbol =el_dict['symbol']
        self.number =el_dict['number']
#     def __str__(self) :
#         return f'name: {self.name}, symbol: {self.symbol}, number: {self.number}'
#
# hydrogen = Element(el_dict)
# print(hydrogen)


# 10.6

class Element():
    def dump(self):
        import pprint
        pprint.pprint(vars(self))

hydrogen = Element()
hydrogen.name = 'Hydrogen'
hydrogen.symbol = 'H'
hydrogen.number = 1
hydrogen.dump()

# 10.7
print(hydrogen)
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'name: {self.name} symbol: {self.symbol} number: {self.number}'


hydrogen = Element('hydrogen','H','1')
print(hydrogen)


# 10.9
class eats():
    def __init__(self,animal,word):
        self.animal = animal
        self.word = word

    def says(self):
        return f"'{self.word}'"
    def who(self):
        return f'({self.animal})'
class Bear(eats):
    def who(self):
        return f'({self.animal})'
class Rabbit(eats):
    def who(self):
        return f'({self.animal})'
class Octothorpe(eats):
    def who(self):
        return f'({self.animal})'
big = eats('berries','Bear')
big1 = eats('clover', 'Rabbit')
big2 = eats('campers', 'Octothorpe')

print(big.who(),big.says())
print(big1.who(),big1.says())
print(big2.who(),big2.says())

# 10.10










































































































