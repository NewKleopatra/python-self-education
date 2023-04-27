with open('input.txt', 'r') as f:
    f.readline()
    input_digit = f.readline().strip()
number = int(input_digit)
with open('output.txt', 'w') as out:
    out.write('Задача 1.1: \nВведите число: ' + str(number) + '\n')
    if 1 <= number <= 100 or 200 <= number <= 300:
        out.write('Число попадает в диапазон\n')
    else:
        out.write('Число не попадает в диапазон\n')


with open('input.txt', 'r') as f:
    for i in range(3):
        f.readline()
    input_digit = f.readline().strip()
    temperature = int(input_digit)
with open('output.txt', 'a') as out:
    out.write('\nЗадача 1.2: \nВведите температуру воды: ' + str(temperature) + '\n')
current_temperature = temperature
time = 0
while temperature < 100:
    temperature += 1
    time += 2
with open('output.txt', 'a') as out:
    out.write(f'Вода закипит через {time} минут\n')
    print(f'Вода закипит через {time} минут')


with open('output.txt', 'a') as out:
    out.write('\nЗадание 1.3:\n')
with open('input.txt', 'r') as f:
    for i in range(5):
        f.readline()
    x = f.readline().strip()
    row_count = int(x)
with open('output.txt', 'a') as out:
    for i in range(row_count):
        out.write(str(i+1) + ' 000\n')


with open('output.txt', 'a') as out:
    out.write('\nЗадание 1.4:')
with open('input.txt', 'r') as f:
    for i in range(7):
        f.readline()
    height = int(f.readline().strip())
with open('output.txt', 'a') as out:
    for i in range(height):
        out.write('*' * (i + 1) + '\n')


with open('output.txt', 'a') as out:
    out.write('\nЗадание 2.1:')
with open('input.txt', 'r') as f:
    for i in range(9):
        f.readline()
    a = int(f.readline().strip())
    b = int(f.readline().strip())
    c = int(f.readline().strip())
    m = int(f.readline().strip())
    k = int(f.readline().strip())
with open('output.txt', 'a') as out:
    if a <= m and b <= k or a <= k and b <= m or a <= m and c <= k or a <= k and c <= m or b <= m and c <= k or b <= k and c <= m:
        out.write('\nКоробка войдет в дверь')
    else:
        out.write('\nКоробка не войдет в дверь')


with open('output.txt', 'a') as out:
    out.write('\n\nЗадание 2.2: \n')
with open('input.txt', 'r') as f:
    for i in range(15):
        f.readline()
    height = int(f.readline().strip())
with open('output.txt', 'a') as out:
    for i in range(height):
        out.write(' ' * (height - i - 1) + '*' * (2 * i + 1) + '\n')


with open('output.txt', 'a') as out:
    out.write('\nЗадание 2.3: \n')
with open('input.txt', 'r') as f:
    for i in range(17):
        f.readline()
    n = int(f.readline().strip())
num = 1
with open('output.txt', 'a') as out:
    while num ** 2 < n:
        out.write(str(num ** 2) + '\n')
        num += 1


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
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
with open('output.txt', 'a') as out:
    out.write('\nСумма цифр числа 9543: ' + str(sum))