a = float(input('ведите первое число'))
b = float(input('ведите вервое число'))

operator = input('Что сделать ? (+, -) ')

result = 0

if operator == '+':
    result = a + b
    print(f'получаеться {result}')
elif operator == '-':
    result = a - b
    print(f'получаеться {result}')
