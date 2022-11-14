import random

number_random = random.randint(1, 1)
user_number = input("Ведите число ( от 1 до 5 ):")

if int(number_random) == number_random:
    print('Вы угодали')
    print(123)
else:
    print(f'вы не угодали, было число {number_random}')