with open('input.txt', 'r') as f:
    f.readline()
    input_digit = f.readline().strip()
number = int(input_digit)
with open('output.txt', 'w') as out:
    out.write('Задача 1.1:\nВведите число: {}\n'.format(number))
    if 1 <= number <= 100 or 200 <= number <= 300:
        out.write('Число попадает в диапазон\n')
    else:
        out.write('Число не попадает в диапазон\n')

with open('output.txt', 'w') as out:
    out.write(f'Задача 1.1:\nВведите число: {number}\n')
    if number in range(1, 101) or number in range(200, 301):
        out.write('Число попадает в диапазон\n')
    else:
        out.write('Число не попадает в диапазон\n')


with open('input.txt', 'r') as f:
    temperature = int(f.readlines()[3])

time = (100 - temperature) * 2

with open('output.txt', 'a') as out:
    out.write(f'\nЗадача 1.2:\nВведите температуру воды: {temperature}\n')
    out.write(f'Вода закипит через {time} минут\n')

print(f'Вода закипит через {time} минут')


with open('input.txt', 'r') as f:
    row_count = int(f.readlines()[5])

with open('output.txt', 'a') as out:
    out.write('\nЗадание 1.3:\n')
    for i in range(1, row_count+1):
        out.write(f'{i} 000\n')


with open('input.txt', 'r') as f:
    height = int(f.readlines()[7])

with open('output.txt', 'a') as out:
    out.write('\nЗадание 1.4:\n')
    for i in range(1, height+1):
        out.write('*' * i + '\n')


with open('input.txt', 'r') as f:
    lines = f.readlines()[9:14]
    a, b, c, m, k = map(int, lines)

with open('output.txt', 'a') as out:
    out.write('\nЗадание 1.5:\n')
    if (a + b <= k or a + c <= k or b + c <= k) and max(a, b, c) <= m:
        out.write('Коробка войдет в дверь')
    else:
        out.write('Коробка не войдет в дверь')

with open('output.txt', 'a') as out:
    out.write('\n\nЗадание 2.2: \n')

with open('input.txt', 'r') as f:
    height = int(f.readlines()[15].strip())

with open('output.txt', 'a') as out:
    for i in range(height):
        out.write(' ' * (height - i - 1) + '*' * (2 * i + 1) + '\n')

import math

with open('output.txt', 'a') as out:
    out.write('\nЗадание 2.3:\n')

with open('input.txt', 'r') as f:
    for i in range(17):
        f.readline()
    n = int(f.readline().strip())

with open('output.txt', 'a') as out:
    for i in range(1, math.isqrt(n) + 1):
        out.write(str(i ** 2) + '\n')


with open('output.txt', 'a') as out:
    out.write('\nЗадание 3.1:\n')
with open('input.txt', 'r') as f:
    for i in range(19):
        f.readline()
    k = int(f.readline().strip())
    with open('output.txt', 'a') as out:
        if k % 3 == 0 or k % 5 == 0 or k % 3 + k % 5 == 5:
            out.write("Можно купить ровно " + str(k) + " шариков мороженного")
        else:
            out.write("Нельзя купить ровно " + str(k) + " шариков мороженного")


with open('output.txt', 'a') as out:
    out.write('\n\nЗадание 3.2:\n')
with open('input.txt', 'r') as f:
    for i in range(21):
        f.readline()
    x = int(f.readline().strip())
    y = int(f.readline().strip())
    z = int(f.readline().strip())
years = 0
while x < z:
    x = x * (1 + y / 100)
    years += 1
with open('output.txt', 'a') as out:
    out.write("Через " + str(years) + " лет сумма вклада превысит " + str(z) + " тысяч гривен")



with open('output.txt', 'a') as out:
    out.write('\n\nЗадание 3.3:')

with open('input.txt', 'r') as f:
    for i in range(25):
        f.readline()

    n = int(f.readline().strip())

sum_digits = sum(int(digit) for digit in str(n))

with open('output.txt', 'a') as out:
    out.write('\nСумма цифр числа {}: {}'.format(n, sum_digits))