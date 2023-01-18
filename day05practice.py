#8.10

squares = {i:i ** 2 for i in range(10)}
print(squares)

# 8.11

set_odd = {number for number in range(10) if number % 2 == 1}
print(set_odd)

# 8.13

a = 'optimist','pessimist','troll'
b = 'The glass is half full', 'The glass is half empty', 'How did you get a glass'

print(dict(zip(a,b)))

# 8.14
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']

print(dict(zip(titles,plots)))

# 9.1

def good():
    return ['Harry','Ron','Hermione']
print(good())


































































