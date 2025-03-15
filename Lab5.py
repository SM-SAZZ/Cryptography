"""
№ 6 Реализовать алгоритм быстрого возведения в степень Показать его
эффективность.
"""
import time
import math

def fast_pow(a, n):
    result = 1
    while n > 0:
        if n % 2 == 1:  # Если степень нечетная
            result *= a
        a *= a  # Возводим a в квадрат
        n //= 2  # Уменьшаем степень вдвое
    return result

def naive_pow(a, n):
    result = 1
    for _ in range(n):
        result *= a
    return result

# Сравнение времени выполнения
a = 2
n = 1000000

start_time = time.time()
fast_pow(a, n)
end_time = time.time()
print(f"Быстрое возведение в степень: {end_time - start_time:.6f} секунд")

start_time = time.time()
naive_pow(a, n)
end_time = time.time()
print(f"Наивное возведение в степень: {end_time - start_time:.6f} секунд")