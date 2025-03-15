from math import gcd
from functools import reduce

def input_congruences():
    """Функция для ввода системы сравнений с клавиатуры."""
    congruences = []

    while True:
        a = input("Введите значение a (оставьте пустым для завершения ввода): ")
        if a == "":
            break

        m = input("Введите значение m (оставьте пустым для завершения ввода): ")
        if m == "":
            break

        try:
            a = int(a)
            m = int(m)

            if m <= 0:
                print("Модуль m должен быть положительным числом. Попробуйте снова.")
                continue

            congruences.append((a, m))
        except ValueError:
            print("Некорректный ввод. Введите целые числа для a и m.")
            
    return congruences

def extended_gcd(a, b):
    """Расширенный алгоритм Евклида для нахождения НОД и коэффициентов Безу."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    """Нахождение обратного элемента по модулю."""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # Обратный элемент не существует, если a и m не взаимно просты
    else:
        return x % m

def chinese_remainder_theorem(congruences):
    """Решение системы сравнений с использованием КТО."""
    # Разделяем сравнения на списки a_i и m_i
    a_list, m_list = zip(*congruences)
    
    # Проверяем, что все модули попарно взаимно просты
    for i in range(len(m_list)):
        for j in range(i + 1, len(m_list)):
            if gcd(m_list[i], m_list[j]) != 1:
                return None, "Модули не попарно взаимно просты, система может не иметь решений."
    
    # Вычисляем общий модуль M
    M = reduce(lambda x, y: x * y, m_list)
    
    # Вычисляем промежуточные значения M_i и y_i
    x = 0
    for a_i, m_i in zip(a_list, m_list):
        M_i = M // m_i
        y_i = mod_inverse(M_i, m_i)
        if y_i is None:
            return None, f"Обратный элемент для {M_i} по модулю {m_i} не существует."
        x += a_i * M_i * y_i
    
    return x % M, "Решение найдено."

# Основная программа
print("Введите систему сравнений вида x = a mod m.")
print("Для завершения ввода оставьте a или m пустыми.")
congruences = input_congruences()

if not congruences:
    print("Система сравнений не введена.")
else:
    solution, message = chinese_remainder_theorem(congruences)

    if solution is not None:
        print(f"Решение системы: x = {solution}")
    else:
        print(message)