import fibo as fibonacci, sys


# import fibo --also true

fibonacci.fib(1000)
print(fibonacci.fib2(1000))
print("Name of module : ", fibonacci.__name__)

# dir lists all types of names: variables, modules, functions, etc.
print(dir(fibonacci))
print(dir(sys))
print(dir())

# dir() list variables and function in current module but it does not lists builtin funnctions and variables.
import builtins
print(dir(builtins))