# if statements
x = 20
if x < 0:
    print('Negative')
elif x == 0:
    print("Zero")
else:
    print("Positive")

# for statement
words = ['cat', 'window', 'defenestrate']

for word in words:
    print(word, end=", ")

print()
# interate over copy and modify original

for word in words.copy():
    if word == 'window':
        words.remove(word)

print(words)

# range function

for i in range(5):
    print(i, end=", ")
print()

words = ['cat', 'window', 'defenestrate']
for i in range(len(words)):
    print(i, words[i])

# range function does not return list, it returns iterable object.
print(range(10))

# sum of all element in range
print(sum(range(10)))

# create list from range
print(list(range(10)))

# break and continue statements are same as JAVA

for i in range(2, 15):
    if i > 10:
        break
    if i % 2 == 0:
        print(i, " even")
        continue
    print(i, " odd")


# pass statement, It can be used when a statement is required syntactically but the program requires no action.
# It can be used when a statement is required syntactically but the program requires no action.

class Student:
    pass  # has to implement class


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(2000)

print(fib)

f = fib
f(100)


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib2(100)
print(f100)


# More on defining function
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# print(ask_ok('Yes or No : ', 5))

i = 5


def f(arg=i):
    print(arg)


i = 6
f()


# important warning : default value evaluated only once,
# than that variable used for subsequent calls

def f(a, L=[]):
    L.append(a)
    return L


print(f(1))
print(f(2))
print(f(3))


def f1(a, l1=None):
    if l1 is None:
        l1 = []
    l1.append(a)
    return l1


print(f1(1))
print(f1(2))
print(f1(3))


# Keyword argument

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)
parrot(voltage=1000)
parrot(1000, action='vroom')


# *args which receives a tuple containing the positional arguments.
# **args which receives a dictionary containing all
# keyword arguments except fot those corresponding to formal parameter.


def cheeseShop(kind, *args, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we'r all out of ", kind)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseShop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


#  Positional-or-Keyword Arguments
def standard_arg(arg):
    print(arg)


standard_arg(5)
standard_arg(arg=5)


# positional only
# parameters passed before / is positional args only.

def pos_only_arg(arg, /):
    print(arg)


pos_only_arg(5)


# pos_only_arg(arg = 5)

# keyword only
#

def kwd_only_arg(*, arg):
    print(arg)


# kwd_only_arg(5)
kwd_only_arg(arg=5)


# combined
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


combined_example(5, kwd_only=2, standard=20)
combined_example(5, 20, kwd_only=2)
# combined_example(5, kwd_only=2, 20)

# Arbitrary argument list


def concat(*args, sep="/"):
    return sep.join(args)


print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# Unpacking Argument Lists
print(list(range(3, 6)))   # normal call with separate arguments
args = [3, 6]
print(list(range(*args)))   # call with arguments unpacked from a list


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end='\n')
    print("if you put", voltage, "volts through it.", end='\n')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}

parrot(**d)

# Lambda Expressions


def make_incrementor(n):
    return lambda x: x+n


f = make_incrementor(42)
print(f(0))
print(f(2))

# Documentation Strings


def my_function():
    """
    Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass


print(my_function.__doc__)


def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + " and " + eggs


print(f('spam'))
