# Number
print(2+2)
print(5 - 3*6)
print((5*6 - 6)/3)

# Normal division returns float
print(8/5)
# To get quotient
print(8//5)
# To get reminder
print(8 % 5)

# Power operator
print(2**3)

# Assignment Operator
width = 20
height = 3*5
print(width*height)

# int operand converts to floating point if it used with floating point
print(2 + 3*4.2)


# Strings
print('spam eggs')
print('doesn\'t')
print("doesn't")
print('"yes," they said')
print("\"yes,\" they said")

print("First Line\nSecond Line")

# row string
print("C:\dir1\nirav")
print(r"C:\dir1\nirav")

# multi line string print, using triple double or single quotes
print("""
    Line-1
    Line-2
    Line-3 
""")

print(3*"un" + "ium")


# Direct concatenation only works with literals only, not with variables and expression.

print('Py' 'thon')

text = ('Put several things '
        'together in one line')
print(text)

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-2])

# String slicing
print(word[2:5])
print(word[-4:-1])

print(word[:2], word[2:])

# Strings are immutable
# word[5] = 'b' not allowed

s = 'supercalifragilisticexpialidocious'
print(len(s))

# Lists
squares = [1, 4, 9, 16]
print(squares)

print(squares[2])
print(squares[-3])
print(squares[2:])
print(squares[:])

squares = squares + [25, 36]

print(squares)

cubes = [1, 8, 26, 64]
cubes[2] = 27
print(cubes)

# len(letters)
print(len(cubes))

# Assignment to slice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

letters[2 : 5] = ['C', 'D', 'E']
print(letters)

letters[2:5] = []
print(letters)
letters[:] = []
print(letters)


# nested list
print(['a', 'b', [1, 2 , 3], 'c'])


# First Steps Towards Programming
a, b = 1, 1
while a <= 10:
     print(a, end= ', ')
     a, b = b, a+b