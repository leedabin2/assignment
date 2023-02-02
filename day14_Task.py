# 10.1

class Thing():
    pass
print(Thing)

example = Thing()
print(example)

# 10.2
class Thing2():
    letters = 'abc'

print(Thing2.letters)

# 10.3
class Thing3():
    letters = 'xyz'
print(Thing3.letters)

# 10.4, 10.6
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        result = self.name, self.symbol, self.number
        return result

a = Element('Hydrogen','H',1)
print(a.name)
print(a.symbol)
print(a.number)


# 10.5
el_dict = {'name':'Hydrogen','symbol':'H','number':1}

hydrogen = Element(el_dict['name'],el_dict['symbol'],el_dict['number'])

# 10.6

hydrogen = Element(**el_dict)
print(hydrogen.dump())

# 10.7
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return self.name

hydrogen = Element(**el_dict)
print(hydrogen)

# 10.8

class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol
        self.number = number

    @property
    def get_name(self):
        return self.name

    @property
    def get_symbol(self):
        return self.symbol

    @property
    def get_number(self):
        return self.number

# 10.9

class Bear():
    def eats(self):
        return  'berries'
class Rabbit():
    def eats(self):
        return 'clover'
class Octothorpe():
    def eats(self):
        return 'campers'

a = Bear()
b = Rabbit()
c = Octothorpe()
print(a.eats())
print(b.eats())
print(c.eats())

# 10.10

class Laser():
    def __init__(self):
        self.name = 'disintegrate'
    def does(self):
        return self.name
class Claw():
    def __init__(self):
        self.name = 'crush'
    def does(self):
        return self.name
class SmartPhone():
    def __init__(self):
        self.name = 'ring'
    def does(self):
        return self.name
class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return self.laser ,self.claw, self.smartphone


robot = Robot()
robot.does()









































































































