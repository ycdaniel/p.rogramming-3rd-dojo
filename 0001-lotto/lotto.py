import random

numbers = random.sample(range(1, 46), 7)

lucky_numbers = numbers[0:6]
bonus_number = numbers[6]

lucky_numbers.sort()

print('당첨번호')
print(lucky_numbers)
print('보너스')
print(bonus_number)

