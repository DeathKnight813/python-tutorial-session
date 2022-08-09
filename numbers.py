from cmath import exp
import math
from random import choice, random, randrange, seed, shuffle, uniform

a = -12.6
b = 0.007
c = 6


print(abs(a))
print(math.ceil(b))
print(exp(a))
print(math.fabs(a))
print(math.floor(a))
print(math.log(b))
print(math.log10(b))
print(max(a, b))
print(min(a, b))
print(math.modf(a))
print(pow(a, c))
print(round(a))
print(math.sqrt(b))
# print()

# random numbers

seq = [10, 20, 30, 40]
string = "Random numbers"

print(choice(seq))
print(choice(string))
print(randrange(1, 100, 2))
print(random())
print(seed(1))
print(random())
print(shuffle(seq))
print(seq)
print(uniform(b, c))

# trigonometric functions

print(math.acos(b))

print(math.pi)
print(math.e)
