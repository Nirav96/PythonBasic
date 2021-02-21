# Fancier Output formatting

year = 2016
event = 'Referendum'

print(f'Result of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:9} YES votes {:2.2%}'.format(yes_votes, percentage))


s = 'Hello, world'

#  str() function is meant to return representations of values which are fairly human-readable
print(str(s))
# repr() is meant to generate representations which can be read by the interpreter
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))


# Formatted string literals
import math
print(f'The value of pi is approx {math.pi:.3f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ===> {phone:10d}')

# !r - repr, !a - ascii, !s -str
animal = 'eels'
print(f'My hovercraft is full of {animal}')
print(f'My hovercraft is full of {animal!r}')

# String format() method

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# positional formatting
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# keyword formatting
print('This {food} is {adjective}'.format(food='spam', adjective='absolutely horrible'))

# positional and keyword
print('The story of {0}, {1} and {other}'.format('Bill', 'Manfred', other='Georg'))


# Passing the dict and using square brackets [] to access the keys
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# This could also be done by passing tale as keyword arguments with the ** notation
print('Jack :{Jack:d}, Sjoerd :{Sjoerd:d}, Dcab :{Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x**2, x**3))


# Manual String Formatting

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x**2).rjust(3), end=' ')
    print(repr(x**3).rjust(4))

# str.zfill(n)
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('-3.14159265329'.zfill(7))

# Reading and Writing Files

f = open('data.txt')
print(f.read())
f.close()

f = open('data.txt')
print(f.readline())
f.close()

f = open('data.txt')
for line in f:
    print(line, end='')
f.close()

f = open('write.txt', 'w')
f.write('This line written by program')
f.close()

f = open('write.txt')
print(f.read())
f.close()

import json
print(json.dumps([1, 'simple', 'list']))

f = open('json.txt', 'w')
json.dump([1, 'simple', 'list'], f)
f.close()

f = open('json.txt')
x = json.load(f)
print(x)
f.close()