import random

file_content = open('burgerking.txt', 'r').read()
lines = tuple(file_content.splitlines())

print('고민하지말고 ...')
print(random.choice(lines))
