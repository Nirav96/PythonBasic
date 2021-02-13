# Lists
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.count('banana'))

print(fruits.index('banana'))
print(fruits.index('banana', 4))
fruits.reverse()
print(fruits)
fruits.append('grape')
fruits.sort()
print(fruits)
print(fruits.pop())
print(fruits)

# Using list as stack
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)

# Using list as queues
from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

# List Comprehensions

squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

squares = [x ** 2 for x in range(10)]
print(squares)

pairs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(pairs)


vec = [-4, -2, 0, 2, 4]

# filter list
print([x*2 for x in vec if x >= 0])
# apply function to each element
print([abs(x) for x in vec])
# call a method on each element
freshFruit = ['  banana', '  loganberry ', 'passion sfruit  ']
print([weapon.strip() for weapon in freshFruit])
# create a list of two tuples
print([(x, x*x) for x in range(10)])
# flatten list using a list comprehensions using two for
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Transpose matrix using list comprehension
print([[row[i] for row in matrix] for i in range(4)])

# The following list comprehension will transpose rows and columns
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# list(zip(*matrix))
print(list(zip(*matrix)))

# del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[3:5]
print(a)

del a[:]
print(a)

del a
# print(a)

# Tuples and sequences
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable
# t[0] = 88888
# But they contain mutable objects
v = ([1, 2, 3], [4, 5, 6])
print(v)
v[0].append('Nirav')
print(v)

# empty tuple
empty = ()
print(len(empty))

singleton = 'hello',    # <-- note trailing comma
print(len(singleton))

# Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('abc' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)    # letters in a but not in b
print(a | b)    # letters in a or b or in both
print(a & b)    # letters in a and b both
print(a ^ b)    # letters in a or b but not both

# Similarly list comprehension, set comprehensions are also supported
print({x for x in 'abracadabra' if x not in 'abc'})

# Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
print(tel)
tel['irv'] = 4127
print(tel)
print(list(tel))
print(sorted(tel))
print('guido' in tel)
print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

print({x: x**2 for x in (2, 4, 6)})

# when keys are simple string sit is easier to specify pairs using keyword args
print(dict(sape=4139, guido=4127, jack=4098))


# Looping Techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using
# the enumerate() function.
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'quest', 'favorite color']
answer = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answer):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop sequence in reversed order
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop sequence in sorted order use sorted() function
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
