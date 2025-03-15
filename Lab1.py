"""
№ 6 Реализовать программный продукт решения сравнений первой степени
с указанием всех промежуточных шагов вычисления (текущее значение
коэффициентов в расширенном алгоритме Евклида), программный продукт
так же должен реализовывать возможность того, что сравнение не имеет
решений или имеет больше одного решения. В первом случае сообщать
пользователю с пояснением, во втором строить все возможные решения.
"""
import math

def greatest_common_divider(a, b):
    """Нахождение НОДа"""
    d = b // a
    r = b - a * d
    
    print(f'{b} = {a} * {d} + {r}')

    if (r == 0):
        return a

    return greatest_common_divider(r, a)

def euler(n):
    """Нахождение значения функции Эйлера"""
    res = n
    p = 2

    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n = n // p
            res -= res // p

        p += 1

    if n > 1:
        res -= res // n

    return res

def solve_equasion(a, b, p):
    """Решение сравнения"""
    print(f'{a}x = {b} mod {p}')

    gcd = greatest_common_divider(a,p)

    print(f'НОД({a}, {p}) = {gcd}')

    """Проверка на наличие решений"""
    if b % gcd != 0:
        return 'b не делится без остатка на НОД(a, p). Решений нет'
    else:
        print(f'b делится без остатка на НОД(a, p). Количество решений сравнения: {gcd}')

    """Сокращение коэффициентов на НОД"""
    a = a // gcd
    b = b // gcd
    p = p // gcd

    print(f'{a}x = {b} mod {p}')

    euler_p = euler(p)

    """Нахождение нулевого корня и формирование результирующей строки"""
    x0 = int((math.pow(a, euler_p - 1) * b) % p)

    print(f'x0 = {a}^({euler_p} - 1) * {b} mod {p} = {x0}')

    res = f'Решения сравнения: {x0}'

    """Нахождение остальных корней и прибавление к результирующей строке"""
    for i in range(1, gcd):
        x = x0 + i * p
        print(f'x{i} = {x0} + {i} * {p} = {x}')
        res += f', {x}'
    
    return res

print('ax = b mod p')

a = int(input('Введите a: '))
b = int(input('Введите b: '))
p = int(input('Введите p: '))

print(solve_equasion(a, b, p))